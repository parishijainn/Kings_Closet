import cv2
import mediapipe as mp
import os
import time

# Constants
topScale = 1.25 #how much to scale the shirt width
bottomScale = 2.5   #how much to scale the bottom width
swipeThreshold = 0.2  #how far your finger must move (fraction of screen width/height)
swipeCooldown = 1.0   #cooldown in seconds between swipes

#load images from the images folder
def loadClothingImages():
    folderPath = 'images'
    topImages = [
        cv2.imread(os.path.join(folderPath, f"shirt{i}.png"), 
                   cv2.IMREAD_UNCHANGED)
        for i in range(1, 7)
    ]
    bottomImages = [
        cv2.imread(os.path.join(folderPath, f"skirt{i}.png"), 
                   cv2.IMREAD_UNCHANGED)
        for i in range(1, 4)
    ]
    return topImages, bottomImages

#overlay an RGBA image onto a BGR frame 
def overlayPng(frame, overlayImage, positionX, positionY):
    overlayHeight, overlayWidth = overlayImage.shape[:2]
    frameHeight, frameWidth = frame.shape[:2]

    if positionX + overlayWidth < 0 or positionX > frameWidth or \
       positionY + overlayHeight < 0 or positionY > frameHeight:
        return frame

    #compute intersection area
    x1 = max(positionX, 0)
    y1 = max(positionY, 0)
    x2 = min(positionX + overlayWidth, frameWidth)
    y2 = min(positionY + overlayHeight, frameHeight)
    offsetX = x1 - positionX
    offsetY = y1 - positionY
    intersectionWidth = x2 - x1
    intersectionHeight = y2 - y1

    #clip overlay region
    foregroundRegion = overlayImage[offsetY:offsetY + intersectionHeight,
                                    offsetX:offsetX + intersectionWidth]
    alphaChannel = foregroundRegion[:, :, 3:] / 255.0
    backgroundRegion = frame[y1:y2, x1:x2]
    
    #blend foreground into background using transparency
    for channel in range(3):
        backgroundRegion[:, :, channel] = (
            (1 - alphaChannel[:, :, 0]) * backgroundRegion[:, :, channel] +
            alphaChannel[:, :, 0] * foregroundRegion[:, :, channel]
        )

    frame[y1:y2, x1:x2] = backgroundRegion
    return frame

#function to handle the virtual try-on camera
def tryOnCamera(app):
    topImages, bottomImages = loadClothingImages()
    currentTopIndex = 0
    currentBottomIndex = 0

    lastTopSwipeTime = 0
    lastBottomSwipeTime = 0

    #mediapipe solutions
    mpPose = mp.solutions.pose
    mpHands = mp.solutions.hands
    poseDetector = mpPose.Pose(min_detection_confidence=0.5, 
                               min_tracking_confidence=0.5)
    handDetector = mpHands.Hands(max_num_hands=1, 
                                 min_detection_confidence=0.5, 
                                 min_tracking_confidence=0.5)

    #initialize video capture
    videoCapture = cv2.VideoCapture(0)
    previousRightX = None
    previousRightY = None

    #initialize clothing images
    while True:
        success, frame = videoCapture.read()
        if not success:
            break

        frame = cv2.flip(frame, 1)
        frameHeight, frameWidth = frame.shape[:2]
        colorFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        #pose detection for overlay placement
        poseResult = poseDetector.process(colorFrame)
        if poseResult.pose_landmarks:
            landmarks = poseResult.pose_landmarks.landmark
            leftShoulder = landmarks[mpPose.PoseLandmark.LEFT_SHOULDER]
            rightShoulder = landmarks[mpPose.PoseLandmark.RIGHT_SHOULDER]
            leftHip = landmarks[mpPose.PoseLandmark.LEFT_HIP]
            rightHip = landmarks[mpPose.PoseLandmark.RIGHT_HIP]

            #compute midpoints
            shoulderX = int((leftShoulder.x + 
                             rightShoulder.x) / 2 * frameWidth)
            shoulderY = int((leftShoulder.y + 
                             rightShoulder.y) / 2 * frameHeight)
            hipX = int((leftHip.x + rightHip.x) / 2 * frameWidth)
            hipY = int((leftHip.y + rightHip.y) / 2 * frameHeight)

            shoulderWidth = abs(rightShoulder.x - 
                                leftShoulder.x) * frameWidth
            hipWidth = abs(rightHip.x - leftHip.x) * frameWidth
            scaledTopWidth = max(50, min(int(shoulderWidth * topScale), 
                                         frameWidth))
            scaledBottomWidth = max(50, min(int(hipWidth * bottomScale), 
                                            frameWidth))

            resizedTop = cv2.resize(topImages[currentTopIndex], 
                                    (scaledTopWidth, scaledTopWidth))
            resizedBottom = cv2.resize(bottomImages[currentBottomIndex], 
                                       (scaledBottomWidth, scaledBottomWidth))

            frame = overlayPng(frame, resizedTop, shoulderX - 
                               scaledTopWidth // 2, shoulderY - 
                               scaledTopWidth // 4)
            frame = overlayPng(frame, resizedBottom, hipX - 
                               scaledBottomWidth // 2, hipY - 
                               scaledBottomWidth // 4)

        #one hand gesture detection (right hand only now)
        handResult = handDetector.process(colorFrame)
        currentTime = time.time()

        if handResult.multi_hand_landmarks and handResult.multi_handedness:
            for handLm, handness in zip(handResult.multi_hand_landmarks, 
                                        handResult.multi_handedness):
                if handness.classification[0].label != 'Right':
                    continue  #only respond to right hand

                indexTip = handLm.landmark[mpHands.HandLandmark.INDEX_FINGER_TIP]
                xPos = indexTip.x
                yPos = indexTip.y

                if previousRightX is not None and previousRightY is not None:
                    deltaX = xPos - previousRightX
                    deltaY = yPos - previousRightY

                    #horizontal swipe for tops
                    if abs(deltaX) > abs(deltaY) \
                    and abs(deltaX) > swipeThreshold:
                        if deltaX > 0 and currentTime - \
                        lastTopSwipeTime > swipeCooldown:
                            currentTopIndex = (currentTopIndex + 1)% \
                            len(topImages)
                            lastTopSwipeTime = currentTime
                        elif deltaX < 0 and currentTime - lastTopSwipeTime > \
                        swipeCooldown:
                            currentTopIndex = (currentTopIndex - 1) % \
                            len(topImages)
                            lastTopSwipeTime = currentTime

                    #vertical swipe for bottoms
                    elif abs(deltaY) > abs(deltaX) and abs(deltaY) > \
                    swipeThreshold:
                        if deltaY > 0 and currentTime - lastBottomSwipeTime > \
                        swipeCooldown:
                            currentBottomIndex = (currentBottomIndex + 1) % \
                            len(bottomImages)
                            lastBottomSwipeTime = currentTime
                        elif deltaY < 0 and currentTime - \
                        lastBottomSwipeTime > swipeCooldown:
                            currentBottomIndex = (currentBottomIndex - 1) % \
                            len(bottomImages)
                            lastBottomSwipeTime = currentTime
                #initialize previous positions
                previousRightX = xPos
                previousRightY = yPos

        #display the frame
        cv2.imshow("Virtual Try-On", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            app.isGrading = False
            app.popupVisible = False
            app.state = "browse"
            app.isInstructing = False
            break

    videoCapture.release()
    cv2.destroyAllWindows()
if __name__ == "__main__":
    tryOnCamera(app)