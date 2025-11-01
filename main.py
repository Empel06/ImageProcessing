import os
from scripts.Preprocessing import rgb_to_hsv, save_image
import cv2

# Input en output mappen
input_dirs = ['images/real/', 'images/fake/']
output_base_dir = 'output/preprocessed/'

# Verwerk alle .png beelden
for input_dir in input_dirs:
    label = os.path.basename(os.path.normpath(input_dir))  # 'real' of 'fake'
    output_dir = os.path.join(output_base_dir, label)
    os.makedirs(output_dir, exist_ok=True)
    
    for filename in os.listdir(input_dir):
        if filename.lower().endswith('.png'):
            input_path = os.path.join(input_dir, filename)
            image = cv2.imread(input_path)
            if image is None:
                print(f"Fout bij laden van {input_path}")
                continue
            
            # Converteer naar HSV
            hsv_image = rgb_to_hsv(image)
            
            # Opslaan in output/preprocessed/real of fake
            output_filename = filename.replace('.png', '_hsv.png')
            save_image(hsv_image, output_dir, output_filename)
            
            print(f"{input_path} → {os.path.join(output_dir, output_filename)}")
