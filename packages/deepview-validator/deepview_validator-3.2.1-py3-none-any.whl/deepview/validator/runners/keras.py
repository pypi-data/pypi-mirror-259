# Copyright 2022 by Au-Zone Technologies.  All Rights Reserved.
#
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential.
#
# This source code is provided solely for runtime interpretation by Python.
# Modifying or copying any source code is explicitly forbidden.

from __future__ import annotations
from typing import TYPE_CHECKING, Tuple, Union
if TYPE_CHECKING:
    from deepview.validator.evaluators import Parameters

from deepview.validator.exceptions import NonMatchingIndexException
from deepview.validator.exceptions import MissingLibraryException
from deepview.validator.datasets.utils import resize
from deepview.validator.runners.core import Runner
from time import monotonic_ns as clock_now
import numpy as np
import os

class DetectionKerasRunner(Runner):
    """
    Runs the Keras (h5) models using the tensorflow library.
    
    Parameters
    ----------
        model: str or tf.keras.Model
            The path to the model or the loaded keras model.

        parameters: Parameters
            These are the model parameters set from the command line.

        labels: list
            Unique string labels.

    Raises
    ------
        NonMatchingIndexException
            Raised if the model outputs an index
            that is out of bounds to the labels list passed or the labels
            contained within the model itself.

        MissingLibraryException
            Raised if the tensorflow library is not installed.
    """
    def __init__(
        self,
        model,
        parameters: Parameters,
        labels: list=None
    ):
        super(DetectionKerasRunner, self).__init__(model)

        try:
            os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
            import tensorflow as tf
        except ImportError:
            raise MissingLibraryException(
                "tensorflow is needed to load the model.")
        
        if isinstance(model, str):
            model = self.validate_model_path(model)
            self.loaded_model = tf.keras.models.load_model(model, compile=False)
        else:
            self.loaded_model = model
            self.model = "Training Model"
        
        self.parameters = parameters
        self.labels = []
        if labels is not None:
            self.labels = labels
        self.parameters.nms = "tensorflow"
        
        if len(tf.config.list_physical_devices('GPU')):
            self.parameters.engine = "gpu"
        elif len(tf.config.list_physical_devices('CPU')):
            self.parameters.engine = "cpu"
        else:
            self.parameters.engine = "unknown"

    def run_single_instance(
            self, 
            image: Union[str, np.ndarray]
        ) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        """
        Runs the model to produce bounding box predictions on a 
        single image and records the timing information of the model.

        Parameters
        ----------
            image: str or np.ndarray
                This can either be the path to an image or a numpy array
                image.

        Returns
        -------
            boxes: np.ndarray
                The prediction bounding boxes.. [[box1], [box2], ...].

            classes: np.ndarray
                The prediction labels.. [cl1, cl2, ...].

            scores: np.ndarray
                The prediction confidence scores.. [score, score, ...]
                normalized between 0 and 1.
        """
        start = clock_now()
        # Take only the (height, width).
        image = resize(image, self.get_input_shape()[1:])
        tensor = self.apply_normalization(image, self.parameters.normalization)
        load_ns = clock_now() - start
        self.loading_input_timings.append(load_ns * 1e-6)

        start = clock_now()
        outputs = self.loaded_model.predict(tensor, verbose=0)
        infer_ns = clock_now() - start
        self.inference_timings.append(infer_ns * 1e-6)

        start = clock_now()
        boxes, classes, scores = self.postprocessing(outputs)
        boxes_ns = clock_now() - start
        self.box_timings.append(boxes_ns * 1e-6)
        return boxes, classes, scores

    def postprocessing(
            self, 
            outputs: np.ndarray
        ) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        """
        Extracts the boxes, labels, and scores using tensorflow NMS.

        Parameters
        ----------
            outputs: np.ndarray
                This contains bounding boxes, scores, labels.

        Returns
        -------
            boxes: np.ndarray
                The prediction bounding boxes.. [[box1], [box2], ...].

            classes: np.ndarray
                The prediction labels.. [cl1, cl2, ...].

            scores: np.ndarray
                The prediction confidence scores.. [score, score, ...]
                normalized between 0 and 1.

        Raises
        ------
            MissingLibraryException
                Raised if the tensorflow library is not installed.

            NonMatchingIndexException
                Raised if the model label index is
                out of bounds to the input labels list.
        """
        try:
            os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
            import tensorflow as tf
        except ImportError:
            raise MissingLibraryException(
                "tensorflow is needed to perform NMS operations.")

        boxes = outputs[-2]
        if self.parameters.label_offset > 0:
            scores = outputs[-1][..., self.parameters.label_offset:]
        else:
            scores = outputs[-1]

        if self.parameters.max_detections is None:
            self.parameters.max_detections = 100
        
        nmsed_boxes, nmsed_scores, nmsed_classes, valid_boxes = \
            tf.image.combined_non_max_suppression(
                boxes,
                scores,
                self.parameters.max_detections,
                self.parameters.max_detections,
                iou_threshold=self.parameters.detection_iou,
                score_threshold=self.parameters.detection_score,
                clip_boxes=False)

        nmsed_boxes = nmsed_boxes.numpy()
        nmsed_classes = tf.cast(nmsed_classes, tf.int32)

        nms_predicted_boxes = [nmsed_boxes[i, :valid_boxes[i], :]
                               for i in range(nmsed_boxes.shape[0])][0]
        nms_predicted_classes = [nmsed_classes.numpy()[i, :valid_boxes[i]]
                                 for i in range(nmsed_classes.shape[0])][0]
        nms_predicted_scores = [nmsed_scores.numpy()[i, :valid_boxes[i]]
                                for i in range(nmsed_scores.shape[0])][0]

        if len(self.labels) > 0:
            string_nms_predicted_classes = list()
            for cls in nms_predicted_classes:
                try:
                    string_nms_predicted_classes.append(self.labels[int(cls)])
                except IndexError:
                    raise NonMatchingIndexException(cls)
            nms_predicted_classes = np.array(string_nms_predicted_classes)
        return nms_predicted_boxes, nms_predicted_classes, nms_predicted_scores

    def get_input_type(self):
        """
        Returns the model input type.
        
        Returns
        -------
            type: str
                The model input type.
        """
        return 'float32'

    def get_output_type(self):
        """
        Returns the model output type.

        Returns
        -------
            type: str
                The model output type.
        """
        return 'float32'

    def get_input_shape(self):
        """
        Grabs the model input shape.

        Returns
        -------
            type: tuple or list
                The model input shape.
        """
        return self.loaded_model.input.shape

class SegmentationKerasRunner(Runner):
    """
    Runs Keras models to produce segmentation masks.
  
    Parameters
    -----------
        model: str, tf.keras.Model
            The path to the Keras model or the loaded keras model object.

        parameters: Parameters
            This object contains the model parameters configured from the
            command line.

    Raises
    ------
        MissingLibraryException:
            Raised if the the tensorflow library
            which is used to load and run a keras model is not installed.
    """
    def __init__(
            self, 
            model,
            parameters: Parameters
        ):
        super(SegmentationKerasRunner, self).__init__(model=model)

        try:
            os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
            import tensorflow as tf
        except ImportError:
            raise MissingLibraryException(
                "Tensorflow is needed to load Keras models.")
        
        if isinstance(model, str):
            model = self.validate_model_path(model)
            self.loaded_model = tf.keras.models.load_model(model, compile=False)
        else:
            self.loaded_model = model
            self.model = "Training Model"

        self.parameters = parameters

        if len(tf.config.list_physical_devices('GPU')):
            self.parameters.engine = "gpu"
        elif len(tf.config.list_physical_devices('CPU')):
            self.parameters.engine = "cpu"
        else:
            self.parameters.engine = "unknown"

    def run_single_instance(self, image: Tuple[str, np.ndarray]):
        """
        Runs the loaded Keras model on a single image 
        to produce a mask for the image.

        Parameters
        ----------
            image: str or np.ndarray
                This can either be the path to an image or a numpy array
                image.

        Returns
        -------
            mask: np.ndarray
                This is the segmentation mask of the image 
                where each pixel is represented by a class in
                the image.

        Raises
        ------
            MissingLibraryException
                Raised if the tensorflow library 
                is not installed which is needed
                to run a Keras model.
        """
        try:
            os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
            import tensorflow as tf
        except ImportError:
            raise MissingLibraryException(
                "Tensorflow i needed to load Keras models.")

        start = clock_now()
        image = resize(image, self.get_input_shape())
        tensor = self.apply_normalization(image, self.parameters.normalization)
        load_ns = clock_now() - start
        self.loading_input_timings.append(load_ns * 1e-6)
    
        start = clock_now()
        output = self.loaded_model.predict(tensor, verbose=0)
        infer_ns = clock_now() - start
        self.inference_timings.append(infer_ns * 1e-6)

        start = clock_now()
        mask = tf.argmax(output, axis=-1)[0].numpy().astype(np.uint8)
        boxes_ns = clock_now() - start
        self.box_timings.append(boxes_ns * 1e-6)
        return mask

    def get_input_shape(self):
        """
        Returns the input shape of the Keras model.
        
        Returns
        -------
            input shape: tuple
                This is the model input shape (height, width).
        """
        _, model_height, model_width, _ = self.loaded_model.input.shape
        return (model_height, model_width)

class PoseKerasRunner(Runner):
    """
    Runs Keras pose models.

    Parameters
    ----------
        model: str
            The path to the Keras model or the loaded keras model object.

        parameters: Parameters
            This object contains the model parameters configured from the
            command line.

    Raises
    -------
        MissingLibraryException
            Raised if the tensorflow library is not installed.
    """
    def __init__(
            self, 
            model, 
            parameters: Parameters
        ):
        super(PoseKerasRunner, self).__init__(model)

        try:
            os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
            import tensorflow as tf
        except ImportError:
            raise MissingLibraryException(
                "Tensorflow is needed to load the model.")
        
        if isinstance(model, str):
            model = self.validate_model_path(model)
            self.loaded_model = tf.keras.models.load_model(model, compile=False)
        else:
            self.loaded_model = model
            self.model = "Training Model"

        self.parameters = parameters
        
        if len(tf.config.list_physical_devices('GPU')):
            self.parameters.engine = "gpu"
        elif len(tf.config.list_physical_devices('CPU')):
            self.parameters.engine = "cpu"
        else:
            self.parameters.engine = "unknown"

    def run_single_instance(self, image: Tuple[str, np.ndarray]):
        """
        Runs the model to produce angle predictions on a single image and 
        records the timing information of the model.

        Parameters
        ----------
            image: str or np.ndarray
                This can either be the path to an image or a numpy array
                image.

        Returns
        -------
            angles: list
                The Euler angles roll, pitch, yaw.

            None
                Place for supposed labels. TODO Replace None with actual labels.
        """
        start = clock_now()
        image = resize(image, self.get_input_shape())
        tensor = self.apply_normalization(image, self.parameters.normalization)
        load_ns = clock_now() - start
        self.loading_input_timings.append(load_ns * 1e-6)

        start = clock_now()
        outputs = self.loaded_model.predict(tensor, verbose=0)
        infer_ns = clock_now() - start
        self.inference_timings.append(infer_ns * 1e-6)

        start = clock_now()
        boxes_ns = clock_now() - start
        self.box_timings.append(boxes_ns * 1e-6)
        return outputs[0], None

    def get_input_shape(self):
        """
        Returns the model input shape.
       
        Returns
        -------
            type: tuple or list
                The model input shape.
        """
        return self.loaded_model.input.shape[1:]