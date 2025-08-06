# 🗂️ Custom Dataset Creation and Annotation for Object Detection
To develop a high-performance object detection model, I chose to build a custom dataset using real-world images captured manually. This approach ensures the dataset closely represents the target deployment environment and objects. The following steps outline the procedure I followed:

## 🔍 Target Objects
I selected five common everyday objects for detection:

Book
Glass
Laptop
Moisturizer
Remote

These objects were chosen to introduce variation in shape, texture, and reflectivity, enabling the model to learn robust object features.

## 📷 Image Collection
To ensure good model generalization, I captured multiple images of each object under varied conditions:

Different angles (top, side, tilted, etc.)

Single object images

Group images (multiple objects in the same frame)

This diversity helps the model learn better object localization and classification.

## 🏷️ Annotation Process
For annotation, I used Label Studio — a free, open-source image labeling tool with an easy-to-use interface. Each object in the image was labeled with its respective class.

Annotation Format: YOLO format

After annotation, the project was exported from Label Studio, resulting in a data.zip file with the following structure:

data.zip/
├── images/         ← All captured images  
├── labels/         ← YOLO annotation `.txt` files for each image  
├── classes.txt     ← List of class names (Book, Glass, Laptop, Moisturizer, Remote)  
└── notes.json      ← Metadata (ignored for training)
This structure aligns with YOLOv8 input format requirements.

## ⚙️ Dataset Preparation on Google Colab
Upload the zipped image dataset to Google Colab and extract it

**Split the dataset** into train and val directories to facilitate model training and validation

**Install dependencies**: (!pip install ultralytics)

**Configure Training** – Create data.yaml file

A YAML configuration file was created to specify:

Paths for train and validation images
Number of classes
Class names

A classes.txt file was also used to assist in generating correct labels and mappings.

## 🚀 Model Training & Testing
The YOLOv8 training process was started using the configuration defined

Training involved 60 epochs and optimized the model weights

After training, I evaluated the model on the validation set

Trained model weights were saved and downloaded for deployment or inference

# 📚 Key Learnings
**Labeling is Crucial:**
Inaccurate or inconsistent annotations can drastically reduce model performance.

I learned the importance of high-quality labeling and having sufficient data.

**Dataset Quantity Matters:**

With a very small dataset, the model failed to generalize well

YOLO models need diverse, high-quality images for better performance

**Experience with the Pipeline:**

Understood the complete workflow of custom object detection from scratch

Gained hands-on experience using Colab, YOLOv8, and Roboflow
