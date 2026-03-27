"""얼굴 비식별화 모듈 — YOLO로 얼굴 감지 후 즉시 블러 처리"""
import cv2
import numpy as np
from ultralytics import YOLO


class FaceAnonymizer:
    def __init__(self, model_path: str = "yolov11n-face.pt"):
        self.model = YOLO(model_path)

    def blur(self, frame: np.ndarray) -> np.ndarray:
        results = self.model(frame, verbose=False)[0]
        for box in results.boxes.xyxy.cpu().numpy().astype(int):
            x1, y1, x2, y2 = box
            roi = frame[y1:y2, x1:x2]
            if roi.size == 0:
                continue
            frame[y1:y2, x1:x2] = cv2.GaussianBlur(roi, (51, 51), 0)
        return frame
