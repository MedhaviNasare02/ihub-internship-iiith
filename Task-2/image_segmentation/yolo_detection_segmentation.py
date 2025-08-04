from ultralytics import YOLO
import os

# Load the segmentation model
model = YOLO('yolov8l-seg.pt')

# Path to folder containing images
image_folder = 'imagess'

# Loop over all images and segment
for img_file in os.listdir(image_folder):
    if img_file.lower().endswith(('.jpg', '.jpeg', '.png')):
        img_path = os.path.join(image_folder, img_file)
        print(f"🔍 Segmenting: {img_path}")
        results = model(img_path)  # This returns a list of results
        results[0].save()  # Save the first result (correct way)
