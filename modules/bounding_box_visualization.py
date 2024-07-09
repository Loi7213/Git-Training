import cv2
from typing import Tuple
import numpy as np

def bounding_box_visualization(image: np.ndarray, x1: int, y1: int, x2: int, y2: int) -> np.ndarray:
    """
    Visualize bounding box on the image.

    Parameters:
    - image: Input image.
    - x1: X-coordinate of the upper left corner of the bounding box.
    - y1: Y-coordinate of the upper left corner of the bounding box.
    - x2: X-coordinate of the lower right corner of the bounding box.
    - y2: Y-coordinate of the lower right corner of the bounding box.

    Returns:
    - The photo has been drawn with a bounding box.
    """

    # Drawing bounding box 
    cv2.rectangle(image, (x1, y1), (x2, y2), (255, 0, 0), 2)

    return image