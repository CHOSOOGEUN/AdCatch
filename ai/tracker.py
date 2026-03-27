"""ByteTrack 기반 다중 객체 추적 모듈"""
import numpy as np
import supervision as sv


class PersonTracker:
    def __init__(self):
        self.tracker = sv.ByteTracker()
        self.annotator = sv.BoxAnnotator()

    def update(self, detections: sv.Detections) -> sv.Detections:
        """YOLO 감지 결과를 받아 tracker_id가 부여된 Detections 반환"""
        return self.tracker.update_with_detections(detections)

    def annotate(self, frame: np.ndarray, detections: sv.Detections) -> np.ndarray:
        labels = [f"ID:{tid}" for tid in (detections.tracker_id or [])]
        return self.annotator.annotate(frame.copy(), detections=detections, labels=labels)
