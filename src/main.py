import cv2
import numpy as np
import pickle
from src.utils import process_frame

# Load parking space positions
with open("data/processed/parking_positions.pkl", "rb") as f:
    parking_positions = pickle.load(f)

# Load video
cap = cv2.VideoCapture("data/raw/carPark.mp4")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = process_frame(frame, parking_positions)

    cv2.imshow("Car Parking Detection", frame)
    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
