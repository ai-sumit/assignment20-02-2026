import cv2
import numpy as np
import os
from datetime import datetime
import time

class SimpleBlinkCamera:
    def __init__(self, blink_threshold=0.25, double_blink_window=0.5, cooldown_period=2.0):
        
        self.face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        )
        self.eye_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + 'haarcascade_eye.xml'
        )
        self.eye_cascade2 = cv2.CascadeClassifier(
            cv2.data.haarcascades + 'haarcascade_eye_tree_eyeglasses.xml'
        )
        
        self.blink_threshold = blink_threshold
        self.double_blink_window = double_blink_window
        self.cooldown_period = cooldown_period
        self.blink_count = 0
        self.last_blink_time = 0
        self.eyes_detected_prev = True
        self.photo_counter = 0
        self.last_photo_time = 0
        self.is_on_cooldown = False
        
        self.photos_dir = "blink_photos"
        if not os.path.exists(self.photos_dir):
            os.makedirs(self.photos_dir)
        
        self.blink_history = []
        self.history_size = 3
        
        print(f"Photos will be saved in: {os.path.abspath(self.photos_dir)}")
    
    def detect_eyes(self, gray_frame, face_region):
        eyes = []
        eyes1 = self.eye_cascade.detectMultiScale(
            face_region, scaleFactor=1.1, minNeighbors=5, minSize=(20, 20)
        )
        eyes2 = self.eye_cascade2.detectMultiScale(
            face_region, scaleFactor=1.1, minNeighbors=5, minSize=(20, 20)
        )
        if len(eyes1) > 0:
            eyes.extend(eyes1)
        if len(eyes2) > 0:
            eyes.extend(eyes2)
        return eyes
    
    def calculate_eye_ratio(self, eye_region):
        if eye_region.size == 0:
            return 0
        _, binary = cv2.threshold(eye_region, 70, 255, cv2.THRESH_BINARY_INV)
        dark_pixels = np.sum(binary == 255)
        total_pixels = binary.size
        if total_pixels == 0:
            return 0
        return dark_pixels / total_pixels
    
    def capture_photo(self, frame):
        current_time = time.time()
        if current_time - self.last_photo_time < self.cooldown_period:
            return False
        
        self.photo_counter += 1
        self.last_photo_time = current_time
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")[:-3]
        filename = f"{self.photos_dir}/blink_photo_{timestamp}.jpg"
        
        try:
            cv2.imwrite(filename, frame)
            cv2.putText(frame, "PHOTO CAPTURED!", (50, 100),
                       cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 3)
            cv2.imshow('Double-Blink Camera (OpenCV)', frame)
            cv2.waitKey(300)
            self.blink_history = []
            return True
        except:
            return False
    
    def add_watermark(self, frame):
        cv2.putText(frame, "Sumit's Project",
                    (frame.shape[1] - 220, frame.shape[0] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6, (255, 255, 255), 2, cv2.LINE_AA)
    
    def run(self, camera_id=0):
        cap = cv2.VideoCapture(camera_id)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        
        print("DOUBLE-BLINK PHOTO CAPTURE")
        
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            
            frame = cv2.flip(frame, 1)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, 1.1, 5, minSize=(100, 100))
            
            current_time = time.time()
            time_since_last_photo = current_time - self.last_photo_time
            self.is_on_cooldown = time_since_last_photo < self.cooldown_period
            
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = frame[y:y+h, x:x+w]
                
                eyes = self.detect_eyes(roi_gray, roi_gray)
                eyes_detected_now = len(eyes) > 0
                
                for (ex, ey, ew, eh) in eyes:
                    cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
                
                if not self.is_on_cooldown:
                    if not eyes_detected_now and self.eyes_detected_prev:
                        self.blink_history.append(current_time)
                        self.blink_history = [t for t in self.blink_history if current_time - t <= 2.0]
                        
                        if len(self.blink_history) >= 2:
                            if (self.blink_history[-1] - self.blink_history[-2]) <= self.double_blink_window:
                                self.capture_photo(frame)
                
                self.eyes_detected_prev = eyes_detected_now
            
            cv2.putText(frame, f"Photos: {self.photo_counter}", (10, 30),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            
            # ADD WATERMARK
            self.add_watermark(frame)
            
            cv2.imshow('Double-Blink Camera (OpenCV)', frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        cap.release()
        cv2.destroyAllWindows()


def ultra_simple_blink_camera():
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
    cap = cv2.VideoCapture(0)
    
    photos_dir = "simple_blink_photos"
    if not os.path.exists(photos_dir):
        os.makedirs(photos_dir)
    
    eyes_was_detected = True
    blink_times = []
    photo_count = 0
    last_capture_time = 0
    cooldown = 2.0
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        frame = cv2.flip(frame, 1)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            roi_gray = gray[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray)
            
            eyes_detected_now = len(eyes) > 0
            
            if not eyes_detected_now and eyes_was_detected:
                current_time = time.time()
                blink_times.append(current_time)
                blink_times = [t for t in blink_times if current_time - t <= 1.0]
                
                if len(blink_times) >= 2 and (current_time - blink_times[-2]) <= 0.5:
                    if current_time - last_capture_time > cooldown:
                        photo_count += 1
                        filename = f"{photos_dir}/photo_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
                        cv2.imwrite(filename, frame)
                        last_capture_time = current_time
                        blink_times = []
            
            eyes_was_detected = eyes_detected_now
        
        cv2.putText(frame, f"Photos: {photo_count}", (10, 30),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        
        # WATERMARK
        cv2.putText(frame, "Sumit's Project",
                    (frame.shape[1] - 220, frame.shape[0] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6, (255, 255, 255), 2, cv2.LINE_AA)
        
        cv2.imshow('Ultra Simple Blink Camera', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    print("Starting Advanced Simple Blink Camera...")
    camera = SimpleBlinkCamera()
    camera.run()
