
import os
import torch
from PIL import Image
from ultralytics import YOLO
from torchvision.models.detection import (
    fasterrcnn_resnet50_fpn,
    FasterRCNN_ResNet50_FPN_Weights
)

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

SUPPORTED_MODELS = ["yolov8n", "yolo11n", "fasterrcnn"]

_models = {}


def load_model(model_name):
    """Load and cache a selected pretrained object detection model."""

    if model_name not in SUPPORTED_MODELS:
        raise ValueError(
            f"Unsupported model: {model_name}. "
            f"Choose from {SUPPORTED_MODELS}"
        )

    if model_name not in _models:

        if model_name == "yolov8n":
            _models[model_name] = YOLO("yolov8n.pt")

        elif model_name == "yolo11n":
            _models[model_name] = YOLO("yolo11n.pt")

        elif model_name == "fasterrcnn":
            weights = FasterRCNN_ResNet50_FPN_Weights.DEFAULT
            model = fasterrcnn_resnet50_fpn(weights=weights)
            model.to(DEVICE)
            model.eval()

            _models[model_name] = model

    return _models[model_name]


def predict_people(image_path, model_name="yolo11n", confidence=0.25):
    """
    Input:
        image_path: path to an image
        model_name: yolov8n, yolo11n, or fasterrcnn
        confidence: detection confidence threshold

    Output:
        Integer representing the predicted number of people.
    """

    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found: {image_path}")

    model = load_model(model_name)

    if model_name in ["yolov8n", "yolo11n"]:

        prediction = model.predict(
            source=image_path,
            classes=[0],
            conf=confidence,
            verbose=False
        )[0]

        return len(prediction.boxes)

    elif model_name == "fasterrcnn":

        image = Image.open(image_path).convert("RGB")

        weights = FasterRCNN_ResNet50_FPN_Weights.DEFAULT
        image_tensor = weights.transforms()(image).to(DEVICE)

        with torch.no_grad():
            prediction = model([image_tensor])[0]

        person_count = (
            (prediction["labels"] == 1) &
            (prediction["scores"] >= confidence)
        ).sum().item()

        return int(person_count)

