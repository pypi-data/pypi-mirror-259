# Copyright 2022 by Au-Zone Technologies.  All Rights Reserved.
#
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential.
#
# This source code is provided solely for runtime interpretation by Python.
# Modifying or copying any source code is explicitly forbidden.

from deepview.validator.exceptions import MissingLibraryException
from deepview.validator.metrics.detectionutils import batch_iou
from deepview.validator.datasets.core import Dataset
import numpy as np
import os

class Runner:
    """
    Abstract Class that provides a template for the other runner classes.

    Parameters
    ----------
        model: str, tf.keras.Model
            This is the path to the model file, 
            directory of prediction text files (offline), or a loaded keras
            model.

    Raises
    ------
        FileNotFoundError
            Raised if the path to the model does not exist.
    """
    def __init__(self, model):
        
        self.model = model
        self.input_shape = None

        self.box_timings = list()
        self.inference_timings = list()
        self.loading_input_timings = list()

    @staticmethod
    def validate_model_path(source):
        """
        Validates the existance of the model path.
        
        Parameters
        ----------
            source: str
                This is the path to the model file.

        Returns
        -------
            source: str
                The validated path to the model.

        Raises
        ------
            FileNotFoundError
                Raised if the path to the model does not exist.
        """
        if not os.path.exists(source):
            raise FileNotFoundError(
                "Model file is expected to be at: {}".format(source))
        return source

    def load_model(self):
        """Abstract Method"""
        pass

    def run_single_instance(self, image):
        """Abstract Method"""
        pass

    def postprocessing(self, outputs):
        """Abstract Method"""
        pass

    def get_input_type(self):
        """Abstract Method"""
        pass

    def get_output_type(self):
        """Abstract Method"""
        pass

    def get_input_shape(self):
        """Abstract Method"""
        pass

    @staticmethod
    def apply_normalization(
        image: np.ndarray, normalization: str, input_type: str="float32"):
        """
        Performs images normalizations (signed, unsigned, raw).

        Parameters
        ----------
            image: np.ndarray
                The image to perform normalization.

            normalization: str
                This is the type of normalization to perform [signed, unsigned, raw].

            input_type: str
                This is the numpy datatype to convert. Ex. "uint8"

        Returns
        -------
            image: np.ndarray
                Depending on the normalization, the image will be returned.
        """
        if normalization.lower() == 'signed':
            return np.expand_dims((image / 127.5) - 1.0, 0).astype(np.dtype(input_type))
        elif normalization.lower() == 'unsigned':
            return np.expand_dims(image / 255.0, 0).astype(np.dtype(input_type))
        else:
            return np.expand_dims(image, 0).astype(np.dtype(input_type))
        
    def from_numpy(self, x: np.ndarray):
        """
        Convert numpy array to torch tensor.

        Parameters
        ----------
            x: np.ndarray
                The numpy array to convert to pytorch tensor.

        Returns
        -------
            x: torch.Tensor
                This is the numpy array as a torch.Tensor type.
        """
        try:
            import torch
        except ImportError:
            raise MissingLibraryException("pytorch is needed for Tflite models.")
        return torch.from_numpy(x).to("cpu") if isinstance(x, np.ndarray) else x
    
    def non_max_supression( # NOSONAR
            self, 
            prediction,
            agnostic: bool=False,
            multi_label: bool=True,
            nm: int=0,
            max_wh: int=7680,
            max_nms: int= 30000,
            redundant: bool=True,
            merge: bool=False
        ):
        """
        This is the YoloV5 NMS found here:: \
        https://github.com/ultralytics/yolov5/blob/master/utils/general.py#L955

        Reproducing the same parameters as YoloV5 requires:: \
        1) detection score threshold = 0.001
        2) detection iou threshold = 0.60
        3) max detections = 300

        Parameters
        ----------
            prediction: torch.Tensor
                Raw predictions from the model (inference_out, loss_out).
            agnostic: bool

            multi_label: bool
                If validation has more than 1 labels.

            nm: int

            max_wh: int
                The maximum box width and height (pixels).

            max_nms: int
                The maximum number of boxes into torchvision.ops.nms().

            redundant: bool
                Require redundant detections.

            merge: bool
                Use merge NMS.

        Returns
        -------
            output
        """
        try:
            import torchvision
            import torch
        except ImportError:
            raise MissingLibraryException(
                "pytorch is needed for Tflite models.")

        # YOLOv5 model in validation model.
        if isinstance(prediction, (list, tuple)):  
            # Select only inference output.
            prediction = prediction[0] 

        bs = prediction.shape[0]  # Batch size.
        nc = prediction.shape[2] - nm - 5  # The number of classes.
        xc = prediction[..., 4] > self.parameters.detection_score # Candidates.

        multi_label &= nc > 1  # Multiple labels per box (adds 0.5ms/img).
        mi = 5 + nc  # Mask start index.
        output = [torch.zeros((0, 6 + nm), device="cpu")] * bs

        for xi, x in enumerate(prediction):  # Image index, image inference.
            x = x[xc[xi]]  # Confidence.
            if not x.shape[0]:
                continue
            
            # Compute conf
            x[:, 5:] *= x[:, 4:5]  # conf = obj_conf * cls_conf.
            
            # (center_x, center_y, width, height) to (x1, y1, x2, y2).
            box = Dataset.yolo2xyxy(x[:, :4])  
            mask = x[:, mi:]  # zero columns if no masks

            # Detections matrix nx6 (xyxy, conf, cls).
            if multi_label:
                i, j = (
                    x[:, 5:mi] > self.parameters.detection_score
                ).nonzero(as_tuple=False).T
                x = torch.cat(
                    (box[i], x[i, 5 + j, None], j[:, None].float(), mask[i]), 
                    1)
            else:  # Best class only.
                conf, j = x[:, 5:mi].max(1, keepdim=True)
                x = torch.cat(
                    (box, conf, j.float(), mask), 
                    1)[conf.view(-1) > self.parameters.detection_score]

            # Check shape.
            n = x.shape[0]  # Number of boxes.
            if not n:  # No boxes.
                continue
            # Sort by confidence and remove excess boxes.
            x = x[x[:, 4].argsort(descending=True)[:max_nms]]  

            # Batched NMS.
            c = x[:, 5:6] * (0 if agnostic else max_wh)  # The classes.
            # boxes (offset by class), scores.
            boxes, scores = x[:, :4] + c, x[:, 4]  
            
            # Torchvision NMS.
            i = torchvision.ops.nms(
                boxes, scores, self.parameters.detection_iou)  
            i = i[:self.parameters.max_detections]  # This limits detections.
            # Merge NMS (boxes merged using weighted mean).
            if merge and (1 < n < 3e3):  
                # Update boxes as boxes(i,4) = weights(i,n) * boxes(n,4).
                # IoU matrix.
                iou = batch_iou(boxes[i], boxes) > self.parameters.detection_iou
                weights = iou * scores[None]  # Box weights.
                # Merged boxes.
                x[i, :4] = torch.mm(
                    weights, x[:, :4]).float() / weights.sum(1, keepdim=True) 
                if redundant:
                    i = i[iou.sum(1) > 1]  # Require redundancy.
            output[xi] = x[i]
        return output
    
    def summarize(self):
        """
        Returns a summary of all the timings: 
        (mean, avg, max) of (load, inference, box).

        Returns
        -------
            timings in ms: dict

            .. code-block:: python

                {
                 'min_inference_time': minimum time to produce bounding boxes,
                 'max_inference_time': maximum time to produce bounding boxes,
                 'min_input_time': minimum time to load an image,
                 'max_input_time': maximum time to load an image,
                 'min_decoding_time': minimum time to process model
                                    predictions,
                 'max_decoding_time': maximum time to process model
                                    predictions,
                 'avg_decoding': average time to process model predictions,
                 'avg_input': average time to load an image,
                 'avg_inference': average time to produce bounding boxes,
                }
        """
        try:
            return {
                'min_inference_time': np.min(self.inference_timings),
                'max_inference_time': np.max(self.inference_timings),
                'min_input_time': np.min(self.loading_input_timings),
                'max_input_time': np.max(self.loading_input_timings),
                'min_decoding_time': np.min(self.box_timings),
                'max_decoding_time': np.max(self.box_timings),
                'avg_decoding': np.mean(self.box_timings),
                'avg_input': np.mean(self.loading_input_timings),
                'avg_inference': np.mean(self.inference_timings),
            }
        except ValueError:
            return None