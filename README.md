# Real-Time Hand Tracking Rock Paper Scissors with MediaPipe and OpenCV

This repository contains a Python project for real-time hand detection and tracking using MediaPipe and OpenCV. The code detects hands in video streams, draws landmarks and connections, and provides landmark coordinates for potential applications such as gesture recognition and interactive interfaces.

Easy to use and customize, this project serves as a solid foundation for computer vision enthusiasts and developers exploring hand gesture-based controls and analytics.

---
How It Works
The core of the project is the handDetector class which:

Initializes MediaPipe Hands with configurable parameters

Processes each video frame to detect hand landmarks

Draws landmarks and connections on the frame

Extracts landmark coordinates as pixel positions

This can be extended for gesture recognition or other hand-based interactions.

## Features

- Detects multiple hands in real-time video
- Draws hand landmarks and connections on the video feed
- Returns coordinates of hand landmarks for further processing
- Calculates and displays FPS for performance monitoring

---

## Requirements

- Python 3.6+
- OpenCV (`opencv-python`)
- MediaPipe (`mediapipe`)

You can install the dependencies with:

```bash
pip install opencv-python mediapipe
