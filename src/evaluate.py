
import argparse
import time
from pathlib import Path

import numpy as np
import pandas as pd

from core import predict_people


def main():
    parser = argparse.ArgumentParser(
        description="Evaluate a Lane Radar people-counting model."
    )

    parser.add_argument(
        "--model",
        choices=["yolov8n", "yolo11n", "fasterrcnn"],
        default="yolo11n",
        help="Model to evaluate"
    )

    parser.add_argument(
        "--dataset",
        default="data/eval_dataset.csv",
        help="Path to evaluation CSV"
    )

    parser.add_argument(
        "--image-dir",
        default="data/eval_images",
        help="Directory containing evaluation images"
    )

    args = parser.parse_args()

    dataset_path = Path(args.dataset)
    image_dir = Path(args.image_dir)

    if not dataset_path.exists():
        raise FileNotFoundError(
            f"Dataset not found: {dataset_path}"
        )

    df = pd.read_csv(dataset_path)

    required_columns = ["image_path", "actual_people"]

    for column in required_columns:
        if column not in df.columns:
            raise ValueError(
                f"Dataset must contain column: {column}"
            )

    df = df.dropna(subset=["actual_people"]).copy()

    if df.empty:
        raise ValueError(
            "No ground-truth people counts found in the dataset."
        )

    predictions = []
    inference_times = []
    actual_counts = []

    for _, row in df.iterrows():

        original_path = Path(str(row["image_path"]))
        image_path = image_dir / original_path.name

        if not image_path.exists():
            raise FileNotFoundError(
                f"Image not found: {image_path}"
            )

        actual_count = int(row["actual_people"])

        start_time = time.perf_counter()

        predicted_count = predict_people(
            str(image_path),
            model_name=args.model
        )

        elapsed = time.perf_counter() - start_time

        actual_counts.append(actual_count)
        predictions.append(predicted_count)
        inference_times.append(elapsed)

        print(
            f"{image_path.name}: "
            f"Actual={actual_count}, "
            f"Predicted={predicted_count}, "
            f"Time={elapsed:.4f}s"
        )

    actual = np.array(actual_counts)
    predicted = np.array(predictions)

    errors = predicted - actual

    mae = np.mean(np.abs(errors))
    rmse = np.sqrt(np.mean(errors ** 2))
    exact_match = np.mean(errors == 0) * 100
    within_one = np.mean(np.abs(errors) <= 1) * 100
    average_time = np.mean(inference_times)

    results = pd.DataFrame({
        "image_path": df["image_path"].values,
        "actual_people": actual,
        "predicted_people": predicted,
        "absolute_error": np.abs(errors),
        "inference_time_seconds": inference_times
    })

    results_dir = Path("results")
    results_dir.mkdir(exist_ok=True)

    output_file = results_dir / f"{args.model}_evaluation.csv"
    results.to_csv(output_file, index=False)

    print("\n--- Evaluation Summary ---")
    print(f"Model: {args.model}")
    print(f"Images evaluated: {len(actual)}")
    print(f"MAE: {mae:.3f}")
    print(f"RMSE: {rmse:.3f}")
    print(f"Exact Match: {exact_match:.2f}%")
    print(f"Within ±1: {within_one:.2f}%")
    print(f"Average Inference Time: {average_time:.4f} seconds")
    print(f"Results saved to: {output_file}")


if __name__ == "__main__":
    main()
