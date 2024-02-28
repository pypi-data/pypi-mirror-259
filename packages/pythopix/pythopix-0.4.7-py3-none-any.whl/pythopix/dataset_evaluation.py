import csv
import os
import time
import cv2
import torch
from tqdm import tqdm
import matplotlib.pyplot as plt
from ultralytics import YOLO
from typing import Optional, List, Dict, Tuple
import numpy as np
from PIL import Image

from .data_handling import export_to_csv
from .model_operations import process_image, segregate_images
from .utils import custom_sort_key
from .theme import console, INFO_STYLE, SUCCESS_STYLE
from .labels_operations import (
    Label,
    extract_label_files,
    extract_label_sizes,
    read_yolo_labels,
)


def evaluate_dataset(
    test_images_folder: str,
    model_path: Optional[str] = None,
    num_images: int = 100,
    verbose: bool = False,
    print_results: bool = False,
    copy_images: bool = False,
) -> List[dict]:
    """
    Main function to execute the YOLO model analysis script.

    Args:
    model_path (str): Path to the model weights file.
    test_images_folder (str): Path to the test images folder.
    num_images (int): Number of images to separate for additional augmentation.
    verbose (bool): Enable verbose output for model predictions.
    print_results (bool): Print the sorted image data results.
    copy_images (bool): Copy images to a separate folder for additional augmentation.

    Returns:
    List[dict]: A list of dictionaries containing sorted image data based on the evaluation.
    """

    start_time = time.time()

    images = [
        os.path.join(test_images_folder, file)
        for file in os.listdir(test_images_folder)
        if file.endswith(".jpg") or file.endswith(".png")
    ]

    if model_path is None or not os.path.exists(model_path):
        console.print(
            "Model path not provided or not found. Using default YOLO model.",
            style=INFO_STYLE,
        )
        model = YOLO("yolov8n")
    else:
        model = YOLO(model_path)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = model.to(device)

    image_data_list = []
    predictions_dict = {}

    for image_path in tqdm(images, desc="Processing Images"):
        image_data, predictions = process_image(image_path, model, verbose=verbose)
        image_data_list.append(image_data)
        predictions_dict[image_path] = predictions

    sorted_image_data = sorted(image_data_list, key=custom_sort_key, reverse=True)

    if copy_images:
        segregate_images(image_data_list, predictions_dict, num_images=num_images)

    if print_results:
        export_to_csv(sorted_image_data)

    end_time = time.time()
    duration = end_time - start_time
    console.print(
        f"Script executed successfully in {duration:.2f} seconds.", style=SUCCESS_STYLE
    )

    return sorted_image_data


def calculate_bb_area(label: Label) -> float:
    """
    Calculate the surface area of a bounding box from a Label object.

    The Label object contains class_id, center_x, center_y, width, and height.
    This function calculates the surface area of the bounding box defined by the
    width and height in the Label object.

    Args:
    label (Label): A Label object representing the bounding box and class ID.

    Returns:
    float: The fractional surface area of the bounding box, as a proportion of the total image area.
    """

    area = label.width * label.height

    return area


def plot_bb_distribution(label_paths: List[str], save: bool = False) -> None:
    """
    Plots the distribution of bounding box areas from a list of YOLO label file paths.

    Args:
        label_paths (List[str]): A list of paths to YOLO label files.
        save (bool): If True, saves the plot to a file named 'bbox_distribution.png' in
                     the 'pythonpix_results' directory. Defaults to False.
    """
    areas = []

    for path in label_paths:
        labels = read_yolo_labels(path)
        for label in labels:
            area = calculate_bb_area(label) * 100
            areas.append(area)

    plt.figure(figsize=(10, 6))
    plt.hist(areas, bins=30, color="blue", alpha=0.7)
    plt.title("Distribution of Bounding Box Areas")
    plt.xlabel("Area (% of original image)")
    plt.ylabel("Frequency")

    if save:
        os.makedirs("pythopix_results", exist_ok=True)
        plt.savefig("pythopix_results/bbox_distribution.png")

    plt.show()


def plot_label_size_distribution(
    input_folder: str,
    allowed_classes: List[int] = [0],
    save: bool = False,
    show: bool = True,
) -> None:
    """
    Plots the distribution of label widths and heights in pixels from YOLO label files for specified allowed classes.

    This function reads YOLO label files in the specified input folder, extracts
    the widths and heights of bounding boxes in pixels for the allowed classes, and plots their distributions in
    two subplots. Additionally, it prints the average width and height. If the save flag is set, it saves the plot to a specified path.

    Parameters:
    - input_folder (str): Path to the folder containing images and YOLO label files.
    - allowed_classes (List[int], optional): A list of class IDs for which bounding box sizes should be calculated.
    - save (bool): If True, saves the plot to 'pythopix_results/figs/label_size_distribution.png'. Defaults to False.
    - show (bool): If True, shows the plot. Defaults to True

    Returns:
    - None
    """

    label_files = [
        os.path.join(input_folder, f)
        for f in os.listdir(input_folder)
        if f.endswith(".txt")
    ]

    widths, heights = extract_label_sizes(label_files, allowed_classes=allowed_classes)

    average_width = np.mean(widths) if widths else 0
    average_height = np.mean(heights) if heights else 0
    std_dev_width = np.std(widths) if widths else 0
    std_dev_height = np.std(heights) if heights else 0
    variance_width = np.var(widths) if widths else 0
    variance_height = np.var(heights) if heights else 0
    range_width = np.ptp(widths) if widths else 0  # Peak-to-peak (max-min)
    range_height = np.ptp(heights) if heights else 0

    print(
        f"Average Width: {average_width:.2f} pixels, Standard Deviation: {std_dev_width:.2f}, Variance: {variance_width:.2f}, Range: {range_width}"
    )
    print(
        f"Average Height: {average_height:.2f} pixels, Standard Deviation: {std_dev_height:.2f}, Variance: {variance_height:.2f}, Range: {range_height}"
    )

    fig, axs = plt.subplots(1, 2, figsize=(12, 6))
    axs[0].hist(widths, bins=30, color="blue", alpha=0.7)
    axs[0].set_title("Label Width Distribution in Pixels")
    axs[0].set_xlabel("Width (pixels)")
    axs[0].set_ylabel("Frequency")

    axs[1].hist(heights, bins=30, color="green", alpha=0.7)
    axs[1].set_title("Label Height Distribution in Pixels")
    axs[1].set_xlabel("Height (pixels)")

    plt.tight_layout()

    if save:
        os.makedirs("pythopix_results/figs", exist_ok=True)
        plt.savefig("pythopix_results/figs/label_size_distribution.png")

    if show:
        plt.show()


def plot_label_ratios(
    input_folder: str,
    allowed_classes: List[int] = [0],
    save: bool = False,
    show: bool = True,
) -> None:
    """
    Plots and optionally saves the distribution of label aspect ratios (width/height)
    in a dataset, as extracted from YOLO label files, for specified allowed classes.

    This function reads each label file, finds the corresponding image file to
    obtain actual dimensions, calculates the aspect ratio of the bounding boxes,
    and generates a histogram of these ratios.

    Parameters:
    - input_folder (str): Path to the folder containing images and their corresponding YOLO label files.
    - allowed_classes (List[int], optional): A list of class IDs for which bounding box aspect ratios should be calculated.
    - save (bool, optional): If set to `True`, the plot is saved to 'pythopix_results/figs/label_ratios.png'. Defaults to `False`.
    - show (bool): If True, shows the plot. Defaults to True

    Returns:
    - None: Based on the `save` parameter, the function either displays the plot or saves it to a specified directory.
    """

    label_files = [
        os.path.join(input_folder, f)
        for f in os.listdir(input_folder)
        if f.endswith(".txt")
    ]
    widths, heights = extract_label_sizes(label_files, allowed_classes=allowed_classes)

    ratios = [
        w / h if h != 0 else 0 for w, h in zip(widths, heights)
    ]  # Avoid division by zero

    average_aspect_ratio = sum(ratios) / len(ratios) if ratios else 0
    print(f"Average Aspect Ratio: {average_aspect_ratio:.2f}")

    plt.figure(figsize=(8, 6))
    plt.hist(ratios, bins=30, color="purple", alpha=0.7)
    plt.title("Label Aspect Ratio Distribution")
    plt.xlabel("Aspect Ratio (Width/Height)")
    plt.ylabel("Frequency")
    plt.grid(True)

    if save:
        os.makedirs("pythopix_results/figs", exist_ok=True)
        plt.savefig("pythopix_results/figs/label_ratios.png")

    if show:
        plt.show()


def calculate_segmented_metrics(
    folder_path: str,
    model: YOLO = None,
    model_path: str = None,
    segment_number: int = 4,
) -> Dict[str, Tuple[float, float, float]]:
    """
    Processes a folder of images, dividing bounding boxes into segments based on their sizes,
    and calculates average metrics for each segment.

    Args:
    folder_path (str): Path to the folder containing images and corresponding YOLO label files.
    model (YOLO, optional): An instance of the YOLO model. If None, model is loaded from model_path.
    model_path (str, optional): Path to load the YOLO model, used if model is None.
    segment_number (int, optional): Number of segments to divide the bounding boxes into based on their sizes.

    Returns:
    Dict[str, Tuple[float, float, float]]: A dictionary where the key is the segment range (e.g., '0-0.25'),
    and the value is a tuple containing the average false positives, false negatives, and box loss for that segment.
    """

    if model is None:
        if model_path is not None:
            model = YOLO(model_path)
        else:
            console.print(
                "Model path not provided or not found. Using default YOLO model.",
                style=INFO_STYLE,
            )
            model = YOLO("yolov8n")

    # Extract label files
    label_files = extract_label_files(folder_path, label_type="txt")

    # Calculate Bounding Box Sizes
    all_bb_areas = []
    for label_file in label_files:
        labels = read_yolo_labels(label_file)
        for label in labels:
            area = calculate_bb_area(label)
            all_bb_areas.append(area)

    # Segment Bounding Boxes
    max_area = max(all_bb_areas)
    min_area = min(all_bb_areas)
    segment_size = (max_area - min_area) / segment_number
    segments = [
        (
            round(min_area + i * segment_size, 2),
            round(min_area + (i + 1) * segment_size, 2),
        )
        for i in range(segment_number)
    ]
    # Initialize metrics storage
    metrics_by_segment = {f"{seg[0]:.2f}-{seg[1]:.2f}": [] for seg in segments}

    # Assign Bounding Boxes to Segments and Calculate Metrics
    for label_file in tqdm(label_files, desc="Calculating metrics"):
        image_file = label_file.replace(".txt", ".png")
        labels = read_yolo_labels(label_file)

        for label in labels:
            area = calculate_bb_area(label)
            for seg in segments:
                if seg[0] <= area < seg[1]:
                    segment_key = f"{seg[0]:.2f}-{seg[1]:.2f}"
                    image_data, _ = process_image(image_file, model, verbose=False)
                    metrics_by_segment[segment_key].append(image_data)

    for segment, data in tqdm(
        metrics_by_segment.items(), desc="Calculating average metrics by segment"
    ):
        if data:
            valid_fp = [
                d.false_positives
                for d in data
                if isinstance(d.false_positives, (int, float))
            ]
            valid_fn = [
                d.false_negatives
                for d in data
                if isinstance(d.false_negatives, (int, float))
            ]
            valid_bl = [
                d.box_loss for d in data if isinstance(d.box_loss, (int, float))
            ]

            avg_false_positives = round(np.mean(valid_fp) if valid_fp else 0, 2)
            avg_false_negatives = round(np.mean(valid_fn) if valid_fn else 0, 2)
            avg_box_loss = round(np.mean(valid_bl) if valid_bl else 0, 2)

            metrics_by_segment[segment] = (
                avg_false_positives,
                avg_false_negatives,
                avg_box_loss,
            )
        else:
            metrics_by_segment[segment] = (0, 0, 0)

    return metrics_by_segment


def plot_metrics_by_segment(
    metrics_by_segment: Dict[str, Tuple[float, float, float]], save: bool = False
) -> None:
    """
    Plots and optionally saves three bar charts for the given metrics by segment.
    There will be one chart for false positives, one for false negatives, and one for box loss.

    Args:
    metrics_by_segment (Dict[str, Tuple[float, float, float]]): A dictionary with segment ranges as keys and tuples of metrics as values.
    save (bool, optional): If True, saves the plots to the 'pythopix_results' folder. Defaults to False.
    """
    segments = [
        f"{float(seg.split('-')[0])*100:.2f}-{float(seg.split('-')[1])*100:.2f}%"
        for seg in metrics_by_segment.keys()
    ]
    false_positives = [metrics[0] for metrics in metrics_by_segment.values()]
    false_negatives = [metrics[1] for metrics in metrics_by_segment.values()]
    box_losses = [metrics[2] for metrics in metrics_by_segment.values()]

    # Create the directory for saving results if it doesn't exist
    if save:
        os.makedirs("pythopix_results", exist_ok=True)

    # Plotting False Positives
    plt.figure(figsize=(10, 6))
    plt.bar(segments, false_positives, color="#56baf0")
    plt.xlabel("Segments (% of original image)")
    plt.ylabel("False Positives")
    plt.title("False Positives by Segment")
    plt.xticks(rotation=45)
    plt.tight_layout()
    if save:
        plt.savefig("pythopix_results/false_positives_by_segment.png")
    plt.show()

    # Plotting False Negatives
    plt.figure(figsize=(10, 6))
    plt.bar(segments, false_negatives, color="#a3e38c")
    plt.xlabel("Segments (% of original image)")
    plt.ylabel("False Negatives")
    plt.title("False Negatives by Segment")
    plt.xticks(rotation=45)
    plt.tight_layout()
    if save:
        plt.savefig("pythopix_results/false_negatives_by_segment.png")
    plt.show()

    # Plotting Box Loss
    plt.figure(figsize=(10, 6))
    plt.bar(segments, box_losses, color="#050c26")
    plt.xlabel("Segments (% of original image)")
    plt.ylabel("Box Loss")
    plt.title("Box Loss by Segment")
    plt.xticks(rotation=45)
    plt.tight_layout()
    if save:
        plt.savefig("pythopix_results/box_loss_by_segment.png")
    plt.show()


def save_segmented_metrics_to_csv(
    metrics_by_segment: Dict[str, Tuple[float, float, float]]
) -> None:
    """
    Saves the metrics by segment data to a CSV file.

    Args:
    metrics_by_segment (Dict[str, Tuple[float, float, float]]): Metrics data segmented by bounding box sizes.
    save (bool, optional): If True, saves the data to a CSV file in the 'pythopix_results' folder. Defaults to False.
    """
    os.makedirs("pythopix_results", exist_ok=True)
    file_path = os.path.join("pythopix_results", "metrics_by_segment.csv")

    with open(file_path, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Segments", *metrics_by_segment.keys()])

        false_positives = ["False Positives"] + [
            metrics[0] for metrics in metrics_by_segment.values()
        ]
        false_negatives = ["False Negatives"] + [
            metrics[1] for metrics in metrics_by_segment.values()
        ]
        box_loss = ["Box Loss"] + [
            metrics[2] for metrics in metrics_by_segment.values()
        ]

        # Writing data rows
        writer.writerow(false_positives)
        writer.writerow(false_negatives)
        writer.writerow(box_loss)


def visualize_bounding_boxes(
    image_path: str,
    save_fig: bool = False,
    big_labels: bool = False,
    extra_area_percentage: int = 10,
) -> None:
    """
    Displays an image with its bounding boxes as defined in its corresponding YOLO label file,
    optionally with extra area around each box if big_labels is True.
    Can also save the image if save_fig is True.

    Args:
    - image_path (str): Path to the image file.
    - save_fig (bool, optional): If True, saves the image with bounding boxes to a designated folder
                                 instead of displaying it. Defaults to False.
    - big_labels (bool, optional): If True, adds extra area around the bounding boxes. Defaults to False.
    - extra_area_percentage (int, optional): The percentage of the extra area to add around each bounding box. Defaults to 10.

    Returns:
    - None
    """
    image = cv2.imread(image_path)
    if image is None:
        print(f"Image not found at {image_path}")
        return

    height, width, _ = image.shape
    label_path = image_path.replace(".jpg", ".txt").replace(".png", ".txt")

    if not os.path.exists(label_path):
        print(f"No corresponding label file found for {image_path}")
        return

    with open(label_path, "r") as file:
        for line in file:
            class_id, x_center, y_center, bbox_width, bbox_height = [
                float(x) for x in line.split()
            ]

            # Convert to pixel coordinates
            x = int((x_center - bbox_width / 2) * width)
            y = int((y_center - bbox_height / 2) * height)
            w = int(bbox_width * width)
            h = int(bbox_height * height)

            if big_labels:
                extra_w = int(w * extra_area_percentage / 100)
                extra_h = int(h * extra_area_percentage / 100)
                x = max(0, x - extra_w // 2)
                y = max(0, y - extra_h // 2)
                w = min(width, w + extra_w)
                h = min(height, h + extra_h)

            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    if save_fig:
        output_folder = "pythopix_results/figs"
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        base_filename = os.path.splitext(os.path.basename(image_path))[0]
        output_filename = os.path.join(
            output_folder, f"bbox_on_image_{base_filename}.png"
        )
        cv2.imwrite(output_filename, image)
        print(f"Image saved as {output_filename}")
    else:
        cv2.imshow("Image with Bounding Boxes", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


def analyze_image_dimensions(input_folder: str, plot: bool = False, save: bool = False):
    """
    Analyzes the dimensions of PNG images in a specified folder.

    Parameters:
    - input_folder (str): The path to the folder containing the PNG images.
    - plot (bool): If True, plots the width and height distribution of the images.

    This function goes through all PNG images in the specified folder, optionally
    plots their width and height distribution if `plot` is True, and prints out the
    average width and height of the images.
    """
    widths = []
    heights = []

    for file in os.listdir(input_folder):
        if file.endswith(".png"):
            img_path = os.path.join(input_folder, file)
            with Image.open(img_path) as img:
                width, height = img.size
                widths.append(width)
                heights.append(height)

    plt.figure(figsize=(12, 6))

    ax1 = plt.subplot(1, 2, 1)
    plt.hist(widths, bins=20, color="skyblue")
    plt.title("Width Distribution")
    plt.xlabel("Width")
    plt.ylabel("Frequency")
    ax1.ticklabel_format(useOffset=False, style="plain")

    ax2 = plt.subplot(1, 2, 2)
    plt.hist(heights, bins=20, color="lightgreen")
    plt.title("Height Distribution")
    plt.xlabel("Height")
    ax2.ticklabel_format(useOffset=False, style="plain")

    plt.tight_layout()

    if save:
        save_path = "pythopix_results/figs"
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        plt.savefig(f"{save_path}/image_dimensions.png")
    if plot:
        plt.show()

    avg_width = np.mean(widths) if widths else 0
    avg_height = np.mean(heights) if heights else 0
    print(f"Average Width: {avg_width:.2f}")
    print(f"Average Height: {avg_height:.2f}")
