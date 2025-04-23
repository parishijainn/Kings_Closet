import cv2
import mediapipe as mp
import os

#constants
topScale = 1.25      #how much to scale the shirt width
bottomScale = 2.5    #how much to scale the bottom width
swipeThreshold = 0.2 #how far the finger must move for swipe


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

    #clip overlay region
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


def tryOnCamera(app):
    topImages, bottomImages = loadClothingImages()
    currentTopIndex = 0
    currentBottomIndex = 0

    #mediapipe solutions
    poseSolution = mp.solutions.pose
    handSolution = mp.solutions.hands
    poseDetector = poseSolution.Pose(
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5
    )
    handDetector = handSolution.Hands(
        max_num_hands=2,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5
    )

    videoCapture = cv2.VideoCapture(0)
    previousRightX = None
    previousLeftY = None

    while True:
        success, frame = videoCapture.read()
        if not success:
            break

        frame = cv2.flip(frame, 1)
        frameHeight, frameWidth = frame.shape[:2]
        colorFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        #pose detection for clothing placement
        poseResult = poseDetector.process(colorFrame)
        if poseResult.pose_landmarks:
            landmarks = poseResult.pose_landmarks.landmark
            leftShoulder = landmarks[poseSolution.PoseLandmark.LEFT_SHOULDER]
            rightShoulder = landmarks[poseSolution.PoseLandmark.RIGHT_SHOULDER]
            leftHip = landmarks[poseSolution.PoseLandmark.LEFT_HIP]
            rightHip = landmarks[poseSolution.PoseLandmark.RIGHT_HIP]

            #compute midpoints
            shoulderX = int((leftShoulder.x + rightShoulder.x) / 2 * frameWidth)
            shoulderY = int((leftShoulder.y + rightShoulder.y) / 2 * frameHeight)
            hipX = int((leftHip.x + rightHip.x) / 2 * frameWidth)
            hipY = int((leftHip.y + rightHip.y) / 2 * frameHeight)

            #compute widths and scale
            rawShoulderWidth = abs(rightShoulder.x - leftShoulder.x) * frameWidth
            rawHipWidth = abs(rightHip.x - leftHip.x) * frameWidth
            scaledShoulderWidth = max(50, min(int(rawShoulderWidth * topScale),
                                              frameWidth))
            scaledHipWidth = max(50, min(int(rawHipWidth * bottomScale), 
                                         frameWidth))

            #overlay top
            resizedTop = cv2.resize(
                topImages[currentTopIndex],
                (scaledShoulderWidth, scaledShoulderWidth)
            )
            frame = overlayPng(
                frame,
                resizedTop,
                shoulderX - scaledShoulderWidth // 2,
                shoulderY - scaledShoulderWidth // 4
            )

            #overlay bottom
            resizedBottom = cv2.resize(
                bottomImages[currentBottomIndex],
                (scaledHipWidth, scaledHipWidth)
            )
            frame = overlayPng(
                frame,
                resizedBottom,
                hipX - scaledHipWidth // 2,
                hipY - scaledHipWidth // 4
            )

        #hand tracking for swipe gestures
        handResult = handDetector.process(colorFrame)
        if handResult.multi_hand_landmarks and handResult.multi_handedness:
            for handLm, handedness in zip(
                    handResult.multi_hand_landmarks,
                    handResult.multi_handedness
                ):
                handLabel = handedness.classification[0].label  # 'Left' or 'Right'
                indexTip = handLm.landmark[handSolution.HandLandmark.INDEX_FINGER_TIP]
                xPos, yPos = indexTip.x, indexTip.y

                if handLabel == 'Right' and previousRightX is not None:
                    deltaX = xPos - previousRightX
                    if deltaX > swipeThreshold:
                        currentTopIndex = (currentTopIndex + 1) % len(topImages)
                    elif deltaX < -swipeThreshold:
                        currentTopIndex = (currentTopIndex - 1) % len(topImages)
                    previousRightX = xPos

                elif handLabel == 'Left' and previousLeftY is not None:
                    deltaY = yPos - previousLeftY
                    if deltaY > swipeThreshold:
                        currentBottomIndex = (currentBottomIndex + 1) % len(bottomImages)
                    elif deltaY < -swipeThreshold:
                        currentBottomIndex = (currentBottomIndex - 1) % len(bottomImages)
                    previousLeftY = yPos

                #initialize previous positions
                if handLabel == 'Right' and previousRightX is None:
                    previousRightX = xPos
                if handLabel == 'Left' and previousLeftY is None:
                    previousLeftY = yPos

        cv2.imshow("Virtual Try-On", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            app.state = "gameMode"
            break

    videoCapture.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    tryOnCamera(app)
