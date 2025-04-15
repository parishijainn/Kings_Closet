# Citation: Parishi Jain's code (2024)


'''import cv2
import mediapipe as mp
from cmu_graphics import *
from PIL import Image as PILImage

# Initialize Mediapipe hand detection
mpHands = mp.solutions.hands
handTracker = mpHands.Hands()
mpDrawing = mp.solutions.drawing_utils

# Start the webcam
camera = cv2.VideoCapture(0)
currentIndexTipX = None
currentIndexTipY = None

# Process one frame from the camera and update fingertip position
def processCameraFeed():
    global currentIndexTipX, currentIndexTipY
    ret, frame = camera.read()
    if not ret:
        return None

    frame = cv2.flip(frame, 1)  # Mirror the image
    frameRgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = handTracker.process(frameRgb)

    # If hands detected, update index finger tip position
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            indexTip = handLms.landmark[mpHands.HandLandmark.INDEX_FINGER_TIP]
            currentIndexTipX = indexTip.x
            currentIndexTipY = indexTip.y
            break  # Only track first hand

    # Convert OpenCV BGR image to CMUImage
    pilImage = PILImage.fromarray(frameRgb)
    return CMUImage(pilImage)

# Return the latest finger tip position
def getFingerPosition():
    if currentIndexTipX is not None and currentIndexTipY is not None:
        return (currentIndexTipX, currentIndexTipY)
    return None'''
