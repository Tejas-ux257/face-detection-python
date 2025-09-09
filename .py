import cv2
import os
import sys
from datetime import datetime

class FaceDetector:
    def __init__(self):
        # Load the pre-trained face detection model
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
        
    def detect_faces_in_image(self, image_path, output_dir="output"):
        """Detect faces in a static image"""
        try:
            # Create output directory if it doesn't exist
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            
            # Read the image
            img = cv2.imread(image_path)
            if img is None:
                print(f"Error: Could not load image from {image_path}")
                return False
            
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            
            # Detect faces
            faces = self.face_cascade.detectMultiScale(gray, 1.1, 4)
            
            print(f"Found {len(faces)} face(s) in the image")
            
            # Draw rectangles around faces
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
                
                # Detect eyes within the face region
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = img[y:y+h, x:x+w]
                eyes = self.eye_cascade.detectMultiScale(roi_gray)
                
                for (ex, ey, ew, eh) in eyes:
                    cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
            
            # Save the result
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_path = os.path.join(output_dir, f"detected_faces_{timestamp}.jpg")
            cv2.imwrite(output_path, img)
            print(f"Result saved to: {output_path}")
            
            # Display the result
            cv2.imshow('Face Detection Result', img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            
            return True
            
        except Exception as e:
            print(f"Error processing image: {str(e)}")
            return False
    
    def detect_faces_webcam(self):
        """Real-time face detection using webcam"""
        try:
            # Initialize webcam
            cap = cv2.VideoCapture(0)
            
            if not cap.isOpened():
                print("Error: Could not open webcam")
                return False
            
            print("Starting webcam face detection. Press 'q' to quit, 's' to save screenshot")
            
            while True:
                ret, frame = cap.read()
                if not ret:
                    print("Error: Could not read frame from webcam")
                    break
                
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                
                # Detect faces
                faces = self.face_cascade.detectMultiScale(gray, 1.1, 4)
                
                # Draw rectangles around faces
                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                    
                    # Detect eyes within face region
                    roi_gray = gray[y:y+h, x:x+w]
                    roi_color = frame[y:y+h, x:x+w]
                    eyes = self.eye_cascade.detectMultiScale(roi_gray)
                    
                    for (ex, ey, ew, eh) in eyes:
                        cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
                
                # Display face count
                cv2.putText(frame, f'Faces: {len(faces)}', (10, 30), 
                           cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
                
                cv2.imshow('Real-time Face Detection', frame)
                
                key = cv2.waitKey(1) & 0xFF
                if key == ord('q'):
                    break
                elif key == ord('s'):
                    # Save screenshot
                    if not os.path.exists("screenshots"):
                        os.makedirs("screenshots")
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    screenshot_path = f"screenshots/webcam_capture_{timestamp}.jpg"
                    cv2.imwrite(screenshot_path, frame)
                    print(f"Screenshot saved: {screenshot_path}")
            
            cap.release()
            cv2.destroyAllWindows()
            return True
            
        except Exception as e:
            print(f"Error with webcam detection: {str(e)}")
            return False

def main():
    detector = FaceDetector()
    
    print("=== Face Detection Project ===")
    print("1. Detect faces in an image file")
    print("2. Real-time face detection using webcam")
    print("3. Exit")
    
    while True:
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == '1':
            image_path = input("Enter the path to your image file: ").strip()
            if os.path.exists(image_path):
                detector.detect_faces_in_image(image_path)
            else:
                print("Error: Image file not found!")
                
        elif choice == '2':
            detector.detect_faces_webcam()
            
        elif choice == '3':
            print("Thank you for using Face Detection Project!")
            break
            
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
