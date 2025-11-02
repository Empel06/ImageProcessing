import cv2
import numpy as np
import os

def rgb_to_hsv(image):
    """
    Converteer een BGR beeld naar HSV.
    Parameters:
        image (numpy.ndarray): Inputbeeld in BGR.
    Returns:
        hsv_image (numpy.ndarray): Beeld in HSV.
    """
    return cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

def apply_clahe_on_value(hsv_image, clip_limit=2.0, tile_grid_size=(8, 8)):
    """
    Pas CLAHE (Contrast Limited Adaptive Histogram Equalization) toe op het Value-kanaal van een HSV-beeld.
    Parameters:
        hsv_image (numpy.ndarray): Inputbeeld in HSV.
        clip_limit (float): Contrastbeperking (hogere waarde = meer contrast).
        tile_grid_size (tuple): Grootte van lokale gebieden voor adaptieve equalization.
    Returns:
        hsv_equalized (numpy.ndarray): HSV-beeld met verbeterd contrast in Value-kanaal.
    """
    h, s, v = cv2.split(hsv_image)
    clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=tile_grid_size)
    v_equalized = clahe.apply(v)
    hsv_equalized = cv2.merge((h, s, v_equalized))
    return hsv_equalized

def hsv_to_bgr(hsv_image):
    """
    Converteer een HSV beeld terug naar BGR.
    """
    return cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)

def preprocess_image(image):
    """
    Complete pre-processing pipeline:
    1. RGB → HSV
    2. Histogram equalization (CLAHE) op Value
    3. HSV → BGR
    """
    hsv = rgb_to_hsv(image)
    hsv_eq = apply_clahe_on_value(hsv)
    bgr_eq = hsv_to_bgr(hsv_eq)
    return bgr_eq

def save_image(image, output_path, filename):
    """
    Sla een beeld op naar de opgegeven map.
    """
    os.makedirs(output_path, exist_ok=True)
    cv2.imwrite(os.path.join(output_path, filename), image)
