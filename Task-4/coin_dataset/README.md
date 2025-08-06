# 🪙 Coin Detection using YOLOv8
This project demonstrates the process of training a YOLOv8 object detection model on a pre-labeled US coin dataset. The goal is to detect and classify US coins (Pennies, Dimes, Nickels, and Quarters) from images using deep learning.

## 📁 Dataset
Source: YOLO Coin Dataset by Evan Juras
Images: 750 pre-labeled images
Classes: Pennies, Dimes, Nickels, Quarters

💡 Ensure you're using a GPU-enabled runtime in Colab:
Runtime > Change runtime type > GPU

## Download and Extract Dataset:
!wget -O /content/data.zip https://s3.us-west-1.amazonaws.com/evanjuras.com/resources/YOLO_coin_data_12DEC30.zip
!unzip -q /content/data.zip -d /content/custom_data
## **🧠 Data Preprocessing**
Images were automatically split into training (90%) and validation (10%) sets.

This ensured a balanced and effective distribution for YOLOv8 model training.

## ⚙️ Configuration
A custom data.yaml file was generated automatically. This configuration file specifies the number of classes, class names, and paths to the training and validation data.

## 🚀 Model Training
The YOLOv8 model was trained for 40 epochs with an image size of 640x640. The training utilized GPU acceleration provided by Colab

## 🧪 Model Testing
After training, the model was tested on the validation dataset.

Accuracy and detection performance were visually verified.

## 📊 Result Visualization
The model’s predictions were visualized on sample outputs. Coins were successfully detected and correctly classified.

## 💾 Model Saving & Export
The best-performing model weights and logs were saved. They were then zipped and downloaded for future use using following script:
from google.colab import files
files.download('/content/my_model.zip')
