# Lane Radar 

### Smart Queue and Checkout Time Estimation Using Computer Vision

Lane Radar is a computer vision project designed to estimate supermarket checkout queue sizes by detecting people in images. The project evaluates different pretrained object detection models to identify their performance in people counting.

##  Project Objectives

- Detect people in supermarket checkout and queue images.
- Estimate the number of people in each queue.
- Compare multiple pretrained object detection models.
- Evaluate model accuracy and inference speed.
- Identify a suitable model for future checkout time estimation.

##  Technologies Used

- Python
- Google Colab
- PyTorch
- Torchvision
- Ultralytics YOLO
- YOLOv8n
- YOLO11n
- Faster R-CNN ResNet50 FPN
- Pandas
- NumPy
- Matplotlib
- OpenCV

##  Model Evaluation

The project evaluates three pretrained object detection models using a dataset of 20 supermarket checkout and queue images.

The evaluation metrics include:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- Exact Match Accuracy
- Accuracy Within ±1 Person
- Average Inference Time

### Models Evaluated

| Model | Description |
|---|---|
| YOLOv8n | Lightweight object detection model |
| YOLO11n | Updated YOLO object detection model |
| Faster R-CNN ResNet50 FPN | Region-based object detection model |

##  Project Contents

The complete project, including the evaluation dataset, model comparison results, evaluation outputs, and project documentation, is available in the ZIP file uploaded to this repository.

##  Future Enhancements

- Improve people detection in crowded checkout queues.
- Incorporate shopping basket and cart load estimation.
- Estimate checkout waiting times.
- Develop a real-time checkout lane monitoring dashboard.
- Display queue information on digital overhead boards.

##  Project Information

**Project Name:** Lane Radar  
**Domain:** Computer Vision and Artificial Intelligence  
**Project Type:** Model Evaluation and Smart Queue Estimation  
**Repository:** Lane-Radar


