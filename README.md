# AI-project-SCAI


Smart Stadium Management System

Overview

A comprehensive system powered by artificial intelligence technologies designed
to enhance the experience of fans and organizers within sports stadiums.
It offers intelligent solutions for crowd management, ticketing, fan engagement,
and surveillance, aiming to elevate safety, efficiency, and interaction.

⸻

Key Features
        •       Smart Crowd Analysis: Utilizes YOLOv8 for real-time person detection and tracking in images and videos.
        •       Ticket Management: Seamless booking and management of tickets.
        •       Virtual Attendance: Interactive experiences that simulate real-life presence from anywhere.
        •       Interactive Stadium Map: Displays seating arrangements, gates, and key areas within the stadium.
        •       Intelligent Assistant (Chatbot): Responds to fan inquiries through an interactive and friendly interface.
        •       Customized Interfaces: Tailored designs for both fans and organizers to match their specific needs.

⸻

Fully Functional Modules:
main.py: The main script that serves as the entry point of the project.

faceRecognition.py: Implements real-time face detection and recognition.

EmptySeats.py: Detects whether a seat is occupied by analyzing person positions within the frame.

MovementDetection.py: Captures and analyzes motion in a given scene.

Bestpath.py: Suggests optimal paths based on movement analysis.

Fight.py: Detects instances of physical fighting or aggressive behavior.

hand.py: Recognizes hand positions or gestures.

people_tracking.py: Tracks individuals in real-time using object tracking.

faintConditions.py: Attempts to detect cases of fainting or falling.

traffic_data.csv: A dataset used for traffic analysis or model training.

train_model.py: Handles training processes for YOLOv8 models.

Modules Under Development or Require Improvements:
fire.py: Currently under development. Aims to implement fire detection using computer vision techniques.

peoplePositions.py: Still needs refinement to reliably determine and visualize the positions of individuals.

parking.py: Functional but still in progress. Requires additional training to improve accuracy in detecting available parking spots.

YOLO Integration:
yolo_media_detector.py and yoloWebCam.py: Core object detection scripts using YOLOv8 for both image/video files and live camera feeds.

yolov8n.pt: Pre-trained YOLOv8 model used across various detection scripts.

Additional Files:
ShortCodeForFire.py: A minimal or experimental version of fire detection logic.

roboflow.zip: Likely contains dataset exports or annotations from RoboFlow.

Captured, ImagesForYolo, runs: Folders used for storing input data, training images, and output results.

Web App Project Structure

/app                  - Next.js application
/(auth)               - Authentication pages
/(dashboard)          - Admin dashboard
/(mobile)             - Mobile-specific interface
/api                  - API endpoints
/components           - UI components
/context              - Context providers
/dashboard            - Dashboard elements
/layout               - Shared layout files
/people-counter       - Crowd counting module
/stadium-assistant    - Intelligent chat assistant
/ui                   - UI elements and shared components
/lib                  - Helper functions and utilities
/public               - Static assets (images, icons, etc.)
/supabase             - Supabase configuration and integration files



⸻

How to Use the Project

1. Extract the files from the ZIP archive:
Unzip the project into a suitable folder on your device.

2. Run the project:

cd path-to-project
npm install
npm run dev



⸻

You can also try the web application directly without downloading
or setting up anything, via the following link:

[Access the Smart Stadium Web App] (https://v0.dev/chat/data-analysis-app-kvpxeZxnc4F )


Note:
This project is still in active development.
While most modules are stable and ready for use,
a few components are undergoing refinement to enhance
their performance and accuracy. Feedback, contributions,
and suggestions are welcome and appreciated.

