import cv2
import os

def rgb_to_hsv(image):
    """
    Converteer een BGR beeld naar HSV.
    
    Parameters:
        image (numpy.ndarray): Input BGR-beeld.
    
    Returns:
        hsv_image (numpy.ndarray): Beeld in HSV.
    """
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    return hsv_image

def save_image(image, output_path, filename):
    """
    Sla een beeld op naar de opgegeven map.
    """
    os.makedirs(output_path, exist_ok=True)
    cv2.imwrite(os.path.join(output_path, filename), image)
