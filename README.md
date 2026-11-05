
# Lane Radar
## Smart Queue and Checkout Time Estimation

Lane Radar is a computer vision project that estimates the number of people waiting at supermarket checkout lanes using pretrained object detection models.

The project compares YOLOv8n, YOLO11n, and Faster R-CNN ResNet50 FPN to identify a suitable model for checkout queue estimation.

## Project Objectives

- Detect people in supermarket checkout images.
- Estimate the number of people in checkout queues.
- Evaluate and compare pretrained object detection models.
- Identify a suitable model for future checkout-time estimation.

## Models Evaluated

- YOLOv8n
- YOLO11n
- Faster R-CNN ResNet50 FPN

## Evaluation Results

| Model | MAE | RMSE | Exact Match (%) | Within ±1 (%) |
|---|---:|---:|---:|---:|
| YOLOv8n | 2.60 | 3.421 | 20.0 | 45.0 |
| YOLO11n | 2.40 | 2.966 | 15.0 | 30.0 |
| Faster R-CNN ResNet50 FPN | 7.45 | 9.521 | 5.0 | 20.0 |

YOLO11n achieved the lowest MAE and RMSE in the evaluation.

## Dataset

The evaluation dataset contains 20 supermarket checkout images with manually assigned ground-truth people counts.

Dataset files:
- `data/eval_dataset.csv`
- `data/eval_images/`
- `data/compressed_images/`

## Technologies Used

- Python
- Google Colab
- PyTorch
- Ultralytics YOLO
- Torchvision
- OpenCV
- Pandas
- NumPy

## Repository Structure

```text

Lane-Radar/
├── data/
│   ├── eval_dataset.csv
│   ├── eval_images/
│   └── compressed_images/
├── results/
│   ├── model_evaluation.csv
│   ├── model_comparison.csv
│   └── YOLO11n_evaluation.csv
├── src/
│   ├── core.py
│   └── evaluate.py
├── lane_radar.ipynb
├── README.md
├── REPORT.md
└── LICENSE

```

## Installation

Install the required libraries:

```bash
pip install ultralytics torch torchvision pandas numpy pillow
```

## Running the Project

1. Open the project notebook in Google Colab.
2. Upload or extract the Lane Radar project files.
3. Install the required dependencies.
4. Run the notebook cells in order.
5. Evaluate the models on the 20-image dataset.
6. View the evaluation metrics and comparison CSV files in the `results/` directory.

## Evaluation Metrics

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- Exact Match Accuracy
- Within ±1 Accuracy
- Average Inference Time

## Limitations

The current evaluation uses only 20 images and pretrained models. The system estimates people counts but does not yet predict actual checkout waiting time.

## Future Work

- Expand the evaluation dataset.
- Fine-tune the object detection models.
- Improve counting in crowded scenes.
- Estimate checkout waiting time.
- Develop a real-time checkout lane monitoring interface.

## Report

Detailed methodology, results, model selection, limitations, and error analysis are available in `REPORT.md`.


## Running the Evaluation Script

The evaluation script supports three pretrained models.

### Run YOLO11n (default)

```bash
python src/evaluate.py --model yolo11n
```

### Run YOLOv8n

```bash
python src/evaluate.py --model yolov8n
```

### Run Faster R-CNN

```bash
python src/evaluate.py --model fasterrcnn
```

The script evaluates the model on the evaluation dataset and calculates:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- Exact Match Accuracy
- Within ±1 Accuracy
- Average Inference Time

Evaluation results are saved in the `results/` directory.

The model can be changed using the `--model` argument without modifying the source code.






