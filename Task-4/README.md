#**YOLOv8 Object Detection on Custom and Pre-Labeled Datasets**

This task focuses on preparing and training YOLOv8 models.In this task I have used two different dataset.

Custom Labeled Dataset: I clicked the photos of different objects and performed manual labeling using Label Studio. The labeled dataset was then used to train a YOLOv8 model.

Pre-labeled Dataset: I used a coin dataset that was already labeled in YOLO format and trained a YOLOv8 model on it directly.


##🔹**1. Custom Labeling (custom_labeled_dataset/)**
In this part, I worked on manually labeling a dataset using Label Studio .

The labeled images and annotations were exported in YOLOv8 format.

I trained a YOLOv8 model using this custom dataset in Google Colab.

The outputs include training metrics, loss curves, and sample detection results.


📂 Refer: custom_labeled_dataset//README.md for detailed steps and explanation.

##🔹 **2. Pre-labeled Coin Dataset (coin_dataset/)**
This section uses a pre-labeled coin dataset available in YOLO format.

I used this dataset to train another YOLOv8 model.

The training process, results, and final weights are similar to the custom labeled workflow, except the manual labeling step.

📂 Refer: coin_dataset//README.md for more details.
