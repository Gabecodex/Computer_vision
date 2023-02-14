from ultralytics import YOLO
import cv2 as cv

Model = YOLO("yolov8n.pt")

image = cv.imread("Images/n1.png")
print(image.shape)
