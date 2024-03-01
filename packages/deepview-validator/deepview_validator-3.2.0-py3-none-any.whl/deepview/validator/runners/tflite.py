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
from deepview.validator.writers import logger
from time import monotonic_ns as clock_now
from timeit import timeit
import numpy as np

class TFliteRunner(Runner):
    """
    Runs TensorFlow Lite models.
    
    Parameters
    ----------
        model: str or tflite interpreter.
            The path to the model or the loaded tflite model.

        parameters: Parameters
            These are the model parameters set from the command line.

        labels: list
            Unique string labels.

    Raises
    ------
        MissingLibraryException
            Raised if tflite_runtime library is not intalled.

        ValueError
                Raised if the provided image is
                neither a string path that points to the image nor is it a
                numpy.ndarray. Furthermore it raise if the
                provided image path does not exist.
    """
    def __init__(
        self,
        model,
        parameters: Parameters,
        labels: list=None
    ):
        super(TFliteRunner, self).__init__(model)
        try:  # https://coral.ai/docs/edgetpu/tflite-python/#update-existing-tf-lite-code-for-the-edge-tpu
            from tflite_runtime.interpreter import ( 
                Interpreter, 
                load_delegate
            ) 
        except ImportError:
            try:
                import tensorflow as tf
                Interpreter, load_delegate = ( # NOSONAR
                    tf.lite.Interpreter,
                    tf.lite.experimental.load_delegate,
                )
            except ImportError:
                raise MissingLibraryException(
                    "tensorflow or tflite_runtime is needed to load the model.")

        if isinstance(model, str):
            model = self.validate_model_path(model)
            self.interpreter = Interpreter(model_path=model)  # load TFLite model
        else:
            self.interpreter = model
            self.model = "Training Model"

        self.interpreter.allocate_tensors()  # allocate
        self.parameters = parameters

        self.labels = []
        if labels is not None:
            self.labels = labels
    
        if self.parameters.warmup > 0:
            logger("Loading model and warmup...", code="INFO")
            t = timeit(self.interpreter.invoke, number=self.parameters.warmup)
            logger("model warmup took %f seconds (%f ms avg)" %
                           (t, t * 1000 / self.parameters.warmup), code="INFO")
              
    def run_single_instance(
            self, 
            image: Union[str, np.ndarray]
        ) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        """
        Produce tflite predictions on one image and records the timings. 
        This method does not pad the images to match the input shape of the 
        model. This is different to yolov5 implementation where images are 
        padded: https://github.com/ultralytics/yolov5/blob/master/val.py#L197

        Tflite runner functionality was taken from:: \
        https://github.com/ultralytics/yolov5/blob/master/models/common.py#L579

        Parameters
        ----------
            image: str or np.ndarray
                The path to the image or numpy array image

        Returns
        -------
            nmsed_boxes: np.ndarray
                The prediction bounding boxes.. [[box1], [box2], ...].

            nmsed_classes: np.ndarray
                The prediction labels.. [cl1, cl2, ...].

            nmsed_scores: np.ndarray
                The prediction confidence scores.. [score, score, ...]
                normalized between 0 and 1.
        """

        """Input Preprocessing"""
        start = clock_now()
        # Take only the (height, width).
        image = resize(image, self.get_input_shape()[1:3]) 
        tensor = self.apply_normalization(
            image, self.parameters.normalization, self.get_input_type())
        input_details = self.interpreter.get_input_details()
        output_details = self.interpreter.get_output_details()
        self.interpreter.set_tensor(input_details[0]['index'], tensor)
        load_ns = clock_now() - start
        self.loading_input_timings.append(load_ns * 1e-6)
        
        """Inference"""
        start = clock_now()
        self.interpreter.invoke()
        y = []
        for output in output_details:
            # is TFLite quantized uint8 model.
            int8 = input_details[0]["dtype"] == np.uint8  
            x = self.interpreter.get_tensor(output["index"])
            if int8:
                scale, zero_point = output["quantization"]
                x = (x.astype(np.float32) - zero_point) * scale  # re-scale
            y.append(x)
        y = [x if isinstance(x, np.ndarray) else x.numpy() for x in y]
        h, w = self.get_input_shape()[1:3]
        # NMS requires non-normalized coordinates.
        y[0][..., :4] *= [w, h, w, h]  # xywh normalized to pixels.
        if isinstance(y, (list, tuple)):
            output_data = self.from_numpy(y[0]) if len(y) == 1 else [
                self.from_numpy(x) for x in y]
        else:
            output_data = self.from_numpy(y)
        infer_ns = clock_now() - start
        self.inference_timings.append(infer_ns * 1e-6)

        """Postprocessing"""
        start = clock_now()
        output = self.non_max_supression(output_data)
        nmsed_boxes, nmsed_classes, nmsed_scores = self.postprocessing(output)
        decoder_ns = clock_now() - start
        self.box_timings.append(decoder_ns * 1e-6)
        return nmsed_boxes, nmsed_classes, nmsed_scores

    def postprocessing(
            self, output: list) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        """
        Retrieves the boxes, scores and labels.

        Parameters
        ----------
            outputs:
                This contains bounding boxes, scores, labels in the format.
                [[xmin, ymin, xmax, ymax, confidence, label], [...], ...].

        Returns
        -------
            nmsed_boxes: np.ndarray
                The prediction bounding boxes.. [[box1], [box2], ...].

            nmsed_classes: np.ndarray
                The prediction labels.. [cl1, cl2, ...].

            nmsed_scores: np.ndarray
                The prediction confidence scores.. [score, score, ...]
                normalized between 0 and 1.
        """
        h, w = self.get_input_shape()[1:3]
        outputs = output[0].numpy()
        outputs[..., :4] /= [w, h, w, h]
        
        nmsed_boxes = outputs[..., :4]
        # Single dimensional arrays gets converted to the element. 
        # Specify the axis into 1 to prevent that.
        nmsed_scores = np.squeeze(outputs[..., 4:5], axis=1)
        nmsed_classes = np.squeeze(outputs[...,5:6], axis=1) + self.parameters.label_offset

        if len(self.labels) > 0:
            string_nms_predicted_classes = list()
            for cls in nmsed_classes:
                try:
                    string_nms_predicted_classes.append(self.labels[int(cls)])
                except IndexError:
                    raise NonMatchingIndexException(cls)
            nmsed_classes = np.array(string_nms_predicted_classes)
        return nmsed_boxes, nmsed_classes, nmsed_scores
    
    def get_input_type(self) -> str:
        """
        This returns the input type of the model.

        Returns
        -------
            type: str
                The input type of the model.
        """
        return self.interpreter.get_input_details()[0]["dtype"].__name__
    
    def get_output_type(self) -> str:
        """
        This returns the output type of the model.

        Returns
        -------
            type: str
                The output type of the model.
        """
        return self.interpreter.get_output_details()[0]["dtype"].__name__

    def get_input_shape(self) -> np.ndarray:
        """
        Grabs the model input shape.

        Returns
        -------
            shape: np.ndarray
                The model input shape.
                (batch size, height, width, channels).
        """
        return self.interpreter.get_input_details()[0]["shape"]
    
    def get_output_shape(self) -> np.ndarray:
        """
        Grabs the model output shape.

        Returns
        --------
            shape: np.ndarray
                The model output shape.
                (batch size, boxes, classes).
        """
        return self.interpreter.get_output_details()[0]["shape"]