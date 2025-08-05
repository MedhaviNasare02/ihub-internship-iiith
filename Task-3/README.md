
# 🐘🦒🦏🦓 **Wildlife Detection using YOLOv8 and learn to interpret results from various graphs and other output.**


In this task, I trained a YOLOv8 model on the **African Wildlife Detection Dataset**, containing four classes: elephant, giraffe, rhino, and zebra. 
The model was trained for 20 epochs, and performance was analyzed through evaluation metrics and curves.

## 📊 Evaluation Highlights

## 1. ✅ Confusion Matrix Analysis:
It provides a clear summary of how well the trained YOLO model has classified each animal class. The matrix displays the number of correct predictions along the diagonal and the misclassifications in the off-diagonal cells. Overall, the model performs well, with high accuracy and minimal confusion between similar classes.

•	Elephant: 80 correctly predicted, but 12 were missed labeled as background. A few were confused with giraffe.
•	Giraffe: 78 correct. Some confusion with zebras (19 cases)
•	Rhino: 78 accurate detections. A few were misclassified, mostly as background.
•	Zebra: 106 correctly detected, with some misclassified as background.
•	Background Row: Indicates some false detections where background was wrongly predicted as animals. 

## 2. 📈 F1-Confidence Curve:  
The F1 score peaks at ~0.91 around 0.575 confidence. Rhino performs best and giraffe slightly lower. Also the bold blue line shows average performance.

## 3. 🎯 Precision-Confidence Curve:
This graph shows how precision varies with confidence scores for each class. Overall, the model maintains high precision across different confidence levels, with rhino and zebra showing the most stable curves.

## 4. 📉 Precision-Recall Curve:
This curve illustrates the trade-off between precision and recall. Zebra and rhino lead with scores of 0.957 and 0.959, followed by elephant (0.953) and giraffe (0.915). All classes perform well, especially with an overall mAP@0.5 of 0.946, indicating strong detection accuracy.

## 5. 🔍 Recall-Confidence Curve:
Here, recall decreases as confidence increases. The model retrieves most true positives at lower confidence thresholds, and maintains good recall consistency across all classes.

## 6. 📊 Training & Validation Metrics:
This summary plot displays loss reduction and metric improvements over 20 epochs. Both training and validation losses steadily decrease, while precision, recall, and mAP metrics consistently improve, confirming effective model learning.

## 📈 Final Evaluation Metrics

| Metric              | Value   |
|---------------------|---------|
| **Precision (P)**   | 0.936   |
| **Recall (R)**      | 0.878   |
| **mAP@0.5**         | 0.946   |
| **mAP@0.5-0.95**    | 0.777   |


