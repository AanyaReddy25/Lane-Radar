
# Lane Radar
## Smart Queue and Checkout Time Estimation

## 1. Project Overview

Lane Radar is a computer vision project designed to estimate the number of people waiting at supermarket checkout lanes. The estimated queue length can help customers identify less crowded checkout lanes and support future checkout-time estimation.

The project evaluates pretrained object detection models to identify people in supermarket checkout images.

## 2. Evaluation Methodology

### 2.1 Objective

The objective of the evaluation is to identify a suitable pretrained object detection model for counting people in supermarket checkout images. A good model should provide accurate person counts, low counting error, reliable performance in crowded scenes, and reasonable inference speed.

### 2.2 Dataset

The evaluation dataset contains 20 images depicting supermarket checkout lanes and queue scenes. Each image has a manually assigned ground-truth count of people.

The dataset includes a variety of scenes, such as:
- Images with relatively few people.
- Moderately crowded checkout lanes.
- Dense queues with overlapping people.
- Images with partially visible people.
- Images with background people and different image qualities.

The dataset is stored in `data/eval_dataset.csv`, which contains image paths and actual person counts.

### 2.3 Models Evaluated

Three pretrained object detection models were evaluated:
1. YOLOv8n
2. YOLO11n
3. Faster R-CNN ResNet50 FPN

All models were evaluated using the same 20 images and the same ground-truth counts. Person detections were used for counting. For YOLO models, the confidence threshold was 0.25. For Faster R-CNN, the confidence threshold was 0.50.

### 2.4 Metrics and Scoring

The following metrics were used:

**Mean Absolute Error (MAE):**
MAE measures the average absolute difference between predicted and actual people counts. It is the primary metric because it directly represents the average counting error in people. Lower MAE is better.

**Root Mean Squared Error (RMSE):**
RMSE penalizes larger counting errors more heavily. It helps identify models that make occasional substantial mistakes. Lower RMSE is better.

**Exact Match Accuracy:**
This measures the percentage of images where the predicted count exactly matches the ground-truth count.

**Within ±1 Accuracy:**
This measures the percentage of images where the predicted count differs from the ground truth by no more than one person.

**Average Inference Time:**
This measures the average time taken to process an image. Lower inference time is desirable for a real-time checkout application.

The primary selection criterion is MAE, followed by RMSE and inference speed. Exact match and within ±1 accuracy are used as additional indicators of counting reliability.

### 2.5 Target Performance

The initial target is to achieve an MAE of 2 people or fewer per image, with a longer-term objective of improving within ±1 accuracy to at least 70%.

These targets are project goals and are not assumed to have been achieved by the current models.

## 3. Model Evaluation Results

| Model | MAE | RMSE | Exact Match (%) | Within ±1 (%) | Avg. Inference Time (s) |
|---|---:|---:|---:|---:|---:|
| YOLOv8n | 2.60 | 3.421 | 20.0 | 45.0 | 0.3191 |
| YOLO11n | 2.40 | 2.966 | 15.0 | 30.0 | 0.1209 |
| Faster R-CNN ResNet50 FPN | 7.45 | 9.521 | 5.0 | 20.0 | 0.1664 |

### 3.1 Model Selection

YOLO11n was selected as the preferred model for the current Lane Radar prototype.

It achieved the lowest MAE of 2.40 people and the lowest RMSE of 2.966 among the evaluated models. It also demonstrated a relatively low average inference time of 0.1209 seconds per image.

Although YOLOv8n achieved better exact match and within ±1 accuracy, YOLO11n had lower overall counting error. Faster R-CNN performed less effectively on this dataset, with a substantially higher MAE of 7.45.

YOLO11n is therefore selected based on its balance of average counting error and processing speed. Its performance remains preliminary because the evaluation dataset contains only 20 images.

### 3.2 Estimated Cost

The evaluated models are pretrained open-weight models run locally in Google Colab. No paid model API was used.

Estimated model API cost per 1,000 images: $0.

This estimate excludes Google Colab, GPU, cloud infrastructure, storage, and other compute-related expenses. Actual deployment costs may vary.

## 4. Iteration Log

| Iteration | Evaluation | Change Made | Result / Learning |
|---|---|---|---|
| 1 | Baseline evaluation of YOLOv8n, YOLO11n, and Faster R-CNN on 20 images | Pretrained models evaluated using the same dataset and counting criteria | YOLO11n achieved the lowest MAE. Crowded and overlapping scenes produced larger errors. |

No model fine-tuning or parameter optimization was performed during this evaluation. Future iterations should investigate confidence thresholds, fine-tuning, and dataset expansion.

## 5. Limitations

The dataset contains only 20 images. Therefore, the results may not generalize to every supermarket environment.

The current implementation estimates the number of visible people. It does not yet estimate shopping basket sizes or actual checkout waiting times.

Possible sources of error include occlusion, overlapping people, image quality, people appearing small in the image, and differences in manual annotation.

The evaluation is based on pretrained models without task-specific fine-tuning.

## 6. Conclusion

YOLO11n provides a promising starting point for Lane Radar. It achieved the lowest MAE and RMSE among the three evaluated models.

Further improvements may include a larger dataset, fine-tuning, consistent annotation rules, and checkout-time estimation based on queue length and basket load.

## 7. Detailed Error Analysis

The three largest YOLO11n counting errors were examined.

### Example 1: Boston Public Library Image
- Actual people: 22
- Predicted people: 16
- Absolute error: 6
- Observation: The model undercounted the people in the image. Possible reasons include overlapping people and occlusion.

### Example 2: IMG_2209.webp
- Actual people: 12
- Predicted people: 6
- Absolute error: 6
- Observation: The model undercounted the visible people. The crowded scene may have made person detection difficult.

### Example 3: 2ADCGEDSPFFCVKR2KZTFNE3P6M.jpg
- Actual people: 2
- Predicted people: 6
- Absolute error: 4
- Observation: The model overcounted the people. One possible reason is that checkout staff and customers may have been counted differently during manual annotation.

### Error Analysis Conclusion

YOLO11n showed both undercounting and overcounting. Occlusion, crowded scenes, and inconsistent counting scope may contribute to the errors. A larger dataset and consistent annotation rules could improve evaluation reliability.
