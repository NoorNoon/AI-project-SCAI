import cv2
from ultralytics import YOLO
model = YOLO("../yolo-Weights/yolov8n.pt")
results = model("imagesForYolo/people.jpg",show=True)
cv2.waitKey(0)
