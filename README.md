Face Detection Project 🎯

A Python-based face detection application using OpenCV that can detect faces in images and provide real-time face detection through webcam.
Features ✨

Image Face Detection: Upload any image and detect faces with bounding boxes
Real-time Detection: Use your webcam for live face detection
Eye Detection: Also detects eyes within detected faces
Screenshot Capture: Save screenshots during real-time detection
Multiple Output Formats: Save processed images with timestamps

Requirements 📋

Python 3.7 or higher
OpenCV (cv2)
NumPy
A working webcam (for real-time detection)

Installation 🚀

Clone the repository
bashgit clone https://github.com/yourusername/face-detection-project.git
cd face-detection-project

Create a virtual environment (recommended)
bashpython -m venv face_detection_env


Usage 💻

Run the application
bashpython main.py

Choose from the menu

Option 1: Detect faces in an image file

Enter the path to your image
View the result with detected faces highlighted


Option 2: Real-time face detection

Your webcam will start
Press 'q' to quit
Press 's' to save a screenshot
Project Structure 📁
face-detection-project/
│
├── main.py              # Main application file
├── requirements.txt     # Python dependencies
├── README.md           # Project documentation
├── output/             # Processed images (created automatically)
├── screenshots/        # Webcam screenshots (created automatically)
└── sample_images/      # Sample images for testing (optional)
How It Works 🔍
The project uses OpenCV's Haar Cascade classifiers for face detection:

Haar Cascades: Pre-trained classifiers that detect objects (faces/eyes)
Image Processing: Converts images to grayscale for better detection
Detection Algorithm: Scans the image at multiple scales
Bounding Boxes: Draws rectangles around detected faces
Real-time Processing: Processes video frames continuously

Key Functions 🛠️

detect_faces_in_image(): Process static images
detect_faces_webcam(): Real-time webcam detection
Automatic creation of output directories
Timestamp-based file naming
Error handling for various scenarios

