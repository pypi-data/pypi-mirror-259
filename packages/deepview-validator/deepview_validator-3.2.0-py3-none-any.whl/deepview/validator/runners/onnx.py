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

class ONNXRunner(Runner):
    """
    Runs ONNX models.
    
    Parameters
    ----------
        model: str
            The path to the model or the loaded ONNX model.

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
        super(ONNXRunner, self).__init__(model)

        try:
            import onnxruntime
        except ImportError:
            raise MissingLibraryException(
                "onnxruntime or onnxruntime-gpu~=1.17.1 is needed to run ONNX models.")
        try:
            import torch
        except ImportError:
            raise MissingLibraryException(
                "torchvision is needed to check for cuda.")
        
        if isinstance(model, str):
            model = self.validate_model_path(model)
            cuda = torch.cuda.is_available() and parameters.engine != "cpu"  # use CUDA
            providers = ["CUDAExecutionProvider", "CPUExecutionProvider"] if cuda else ["CPUExecutionProvider"]
            self.session = onnxruntime.InferenceSession(model, providers=providers)
            self.output_names = [x.name for x in self.session.get_outputs()]
        else:
            self.session = model
            self.model = "Training Model"

        self.parameters = parameters
        self.labels = []
        if labels is not None:
            self.labels = labels

    def run_single_instance(
        self, 
        image: Union[str, np.ndarray]
    ) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        """
        Produce ONNX inference on one image and records the timings. 
        This method does not pad the images to match the input shape of the 
        model. This is different to yolov5 implementation where images are 
        padded: https://github.com/ultralytics/yolov5/blob/master/val.py#L197

        ONNX runner functionality was taken from:: \
        https://github.com/ultralytics/yolov5/blob/master/models/common.py#L487

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
        image = resize(image, self.get_input_shape()[2:4]) 
        input_type = "float32" if "float" in self.get_input_type() else "uint32"
        image = self.apply_normalization(
            image, self.parameters.normalization, input_type)
        image = np.transpose(image, axes=[0,3,1,2])
        load_ns = clock_now() - start
        self.loading_input_timings.append(load_ns * 1e-6)

        """Inference"""
        start = clock_now()
        y = self.session.run(self.output_names, {self.session.get_inputs()[0].name: image})
        if isinstance(y, (list, tuple)):
            output = self.from_numpy(y[0]) if len(y) == 1 else [
                self.from_numpy(x) for x in y]
        else:
            output = self.from_numpy(y)
        infer_ns = clock_now() - start
        self.inference_timings.append(infer_ns * 1e-6)

        """Postprocessing"""
        start = clock_now()
        # An output with 7 columns refers to batch_id, xmin, ymin, xmax, ymax, cls, score.
        # Otherwise it is batch_size, number of boxes, number of classes which needs external NMS.
        if output.shape[1] != 7:
            output = self.non_max_supression(output)
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
        h, w = self.get_input_shape()[2:4]

        if isinstance(output, list):
            outputs = output[0].numpy()
            outputs[..., :4] /= [w, h, w, h]

            nmsed_boxes = outputs[..., :4]
            # Single dimensional arrays gets converted to the element. 
            # Specify the axis into 1 to prevent that.
            nmsed_scores = np.squeeze(outputs[..., 4:5], axis=1)
        else:
            outputs = output.numpy()
            outputs[..., 1:5] /= [w, h, w, h]
            nmsed_boxes = outputs[..., 1:5]
            # Single dimensional arrays gets converted to the element. 
            # Specify the axis into 1 to prevent that.
            nmsed_scores = np.squeeze(outputs[..., 6:7], axis=1)
        
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
        return self.session.get_inputs()[0].type
    
    def get_output_type(self) -> str:
        """
        This returns the output type of the model.

        Returns
        -------
            type: str
                The output type of the model.
        """
        return self.session.get_outputs()[0].type

    def get_input_shape(self) -> np.ndarray:
        """
        Grabs the model input shape.

        Returns
        -------
            shape: np.ndarray
                The model input shape.
                (batch size, channels, height, width).
        """
        return self.session.get_inputs()[0].shape
    
    def get_output_shape(self) -> np.ndarray:
        """
        Grabs the model output shape.

        Returns
        --------
            shape: np.ndarray
                The model output shape.
                (batch size, boxes, classes).
        """
        return self.session.get_outputs()[0].shape
    
    def get_metadata(self) -> dict:
        """
        This returns the model metadata containing stride and label names
        mapping.

        Returns
        -------
            meta: dict
                Contains the model stride and the label mappings.
        """
        return self.session.get_modelmeta().custom_metadata_map  # metadata