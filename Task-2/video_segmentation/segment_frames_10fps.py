from ultralytics import YOLO
import os

model = YOLO('yolov8n-seg.pt')

input_folder = 'extracted_frames_10fps'
output_folder = 'segmented_frames_10fps'

os.makedirs(output_folder, exist_ok=True)

image_files = sorted([f for f in os.listdir(input_folder) if f.endswith(('.jpg', '.png'))])

for idx, img_file in enumerate(image_files):
    img_path = os.path.join(input_folder, img_file)
    results = model(img_path)
    save_path = os.path.join(output_folder, f"seg_frame_{idx:03}.jpg")
    results[0].save(save_path)
    print(f"Segmented {img_file} ➜ {save_path}")
