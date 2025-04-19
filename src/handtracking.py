# # # Citation: Parishi Jain's code (2024)

# import cv2
# import mediapipe as mp
# from cmu_graphics import *
# from PIL import Image as PILImage

# # Initialize Mediapipe and OpenCV
# mp_hands = mp.solutions.hands
# handTracker = mp_hands.Hands()
# mp_drawing = mp.solutions.drawing_utils

# # OpenCV camera feed
# camera = cv2.VideoCapture(0)
# currentIndexTipX = None
# currentIndexTipY = None

# # Camera feed detects the landmarks
# def processCameraFeed():
#     global currentIndexTipX, currentIndexTipY
#     ret, frame = camera.read() # Read frame from camera
#     if not ret:
#         return None

#     # Invert the frame to show user themselves
#     frame = cv2.flip(frame, 1)
#     frameRgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     # Process with MEdiapipe
#     result = handTracker.process(frameRgb)

#     # Update fingertip coordinates if a hand is detected
#     if result.multi_hand_landmarks:
#         for handLandmarks in result.multi_hand_landmarks:
#             indexTip = handLandmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
#             currentIndexTipX = indexTip.x
#             currentIndexTipY = indexTip.y

#     # Convert OpenCV frame to PIL image for CMU Graphics
#     frameRgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     pilImage = PILImage.fromarray(frameRgb)
#     return CMUImage(pilImage)


# def getFingerPosition():
#     #Return the position of the finger tip
#     if currentIndexTipX is not None and currentIndexTipY is not None:
#         return (currentIndexTipX, currentIndexTipY)
#     return None

import cv2
import mediapipe as mp
from cmu_graphics import *
from PIL import Image as PILImage
import random

# Initialize Mediapipe and OpenCV
mp_hands = mp.solutions.hands
handTracker = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

# OpenCV camera feed
camera = cv2.VideoCapture(0)
currentIndexTipX = None
currentIndexTipY = None

# Count fingers using landmarks
def countFingers(handLandmarks):
    tipIds = [8, 12, 16, 20]  # Index, Middle, Ring, Pinky
    count = 0
    for tipId in tipIds:
        if handLandmarks.landmark[tipId].y < handLandmarks.landmark[tipId - 2].y:
            count += 1
    # Thumb logic (optional): Check if thumb is open
    thumbOpen = handLandmarks.landmark[4].x > handLandmarks.landmark[3].x
    if thumbOpen:
        count += 1
    return count

def processCameraFeed():
    global currentIndexTipX, currentIndexTipY
    ret, frame = camera.read()
    if not ret:
        return None

    frame = cv2.flip(frame, 1)
    frameRgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = handTracker.process(frameRgb)

    if result.multi_hand_landmarks:
        for handLandmarks in result.multi_hand_landmarks:
            indexTip = handLandmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            currentIndexTipX = indexTip.x
            currentIndexTipY = indexTip.y

            # 5-Finger gesture = random outfit (only once per cooldown)
            if app.fingerCooldown == 0 and countFingers(handLandmarks) == 5:
                app.currTopIndex = random.randint(0, len(app.tops) - 1)
                app.currBottomIndex = random.randint(0, len(app.bottoms) - 1)
                app.fingerCooldown = 30

    # Convert OpenCV frame to PIL image for CMU Graphics
    frameRgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    pilImage = PILImage.fromarray(frameRgb)
    return CMUImage(pilImage)

def getFingerPosition():
    if currentIndexTipX is not None and currentIndexTipY is not None:
        return (currentIndexTipX, currentIndexTipY)
    return None

def onStep(app):
    if app.handTrackingMode:
        app.cameraFrame = processCameraFeed(app)
        finger = getFingerPosition()

        if finger is not None:
            fx, fy = finger
            if app.lastFingerX is not None and app.fingerCooldown == 0:
                dx = fx - app.lastFingerX
                dy = fy - app.lastFingerY

                if abs(dx) > 0.07:
                    if dx > 0:
                        app.currTopIndex = (app.currTopIndex + 1) % len(app.tops)
                    else:
                        app.currTopIndex = (app.currTopIndex - 1) % len(app.tops)
                    app.fingerCooldown = 10

                elif abs(dy) > 0.07:
                    if dy > 0:
                        app.currBottomIndex = (app.currBottomIndex + 1) % len(app.bottoms)
                    else:
                        app.currBottomIndex = (app.currBottomIndex - 1) % len(app.bottoms)
                    app.fingerCooldown = 10

            app.lastFingerX, app.lastFingerY = fx, fy

        if app.fingerCooldown > 0:
            app.fingerCooldown -= 1
