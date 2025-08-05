from ultralytics import YOLO

model = YOLO("yolov8n.pt")
model.train(data="C:/yoloproject/african-wildlife/african-wildlife.yaml", epochs=20, imgsz=640)
