# # Citation: Parishi Jain's code (2024)

import cv2
import mediapipe as mp
from cmu_graphics import *
from PIL import Image as PILImage

# Initialize Mediapipe and OpenCV
mp_hands = mp.solutions.hands
handTracker = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

# OpenCV camera feed
camera = cv2.VideoCapture(0)
currentIndexTipX = None
currentIndexTipY = None

# Camera feed detects the landmarks
def processCameraFeed():
    global currentIndexTipX, currentIndexTipY
    ret, frame = camera.read() # Read frame from camera
    if not ret:
        return None

    # Invert the frame to show user themselves
    frame = cv2.flip(frame, 1)
    frameRgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # Process with MEdiapipe
    result = handTracker.process(frameRgb)

    # Update fingertip coordinates if a hand is detected
    if result.multi_hand_landmarks:
        for handLandmarks in result.multi_hand_landmarks:
            indexTip = handLandmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            currentIndexTipX = indexTip.x
            currentIndexTipY = indexTip.y

    # Convert OpenCV frame to PIL image for CMU Graphics
    frameRgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    pilImage = PILImage.fromarray(frameRgb)
    return CMUImage(pilImage)


def getFingerPosition():
    #Return the position of the finger tip
    if currentIndexTipX is not None and currentIndexTipY is not None:
        return (currentIndexTipX, currentIndexTipY)
    return None