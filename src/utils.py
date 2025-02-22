import cv2
import numpy as np

def check_occupancy(img, parking_positions):
    occupied_spaces = []
    for pos in parking_positions:
        x, y, w, h = pos
        roi = img[y:y+h, x:x+w]
        gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 1)
        threshold = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY_INV)[1]

        count = cv2.countNonZero(threshold)
        occupied = count > 1000  # Threshold for occupied space
        occupied_spaces.append(occupied)

    return occupied_spaces

def process_frame(frame, parking_positions):
    occupied_spaces = check_occupancy(frame, parking_positions)

    for idx, pos in enumerate(parking_positions):
        x, y, w, h = pos
        color = (0, 255, 0) if not occupied_spaces[idx] else (0, 0, 255)
        cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)

    return frame
