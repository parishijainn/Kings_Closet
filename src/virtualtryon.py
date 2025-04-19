
import cv2
import mediapipe as mp
import os

def loadClothingImages():
    folder = 'images'
    tops = [cv2.imread(os.path.join(folder, f"shirt{i}.png"), cv2.IMREAD_UNCHANGED) for i in range(1, 7)]
    bottoms = [cv2.imread(os.path.join(folder, f"skirt{i}.png"), cv2.IMREAD_UNCHANGED) for i in range(1, 4)]
    bottoms += [cv2.imread(os.path.join(folder, f"bottom{i}.png"), cv2.IMREAD_UNCHANGED) for i in range(1, 4)]
    return tops, bottoms

def overlayPNG(frame, image, x, y):
    height, width = image.shape[:2]

    if image.shape[2] != 4:
        return frame
    
    #skip if  image would go outside the boundaries
    if y + height > frame.shape[0] or x + width > frame.shape[1]:
        return frame

    #breaks the image into its color and transparency parts
    imageRGB = image[:, :, :3]
    transparencyMask = image[:, :, 3] / 255.0

    #get the part of the frame where the image will go
    background = frame[y:y+height, x:x+width]

    #blend the image with the background based on transparency
    for c in range(3):
        background[:, :, c] = (1 - transparencyMask) * background[:, :, c] + transparencyMask * imageRGB[:, :, c]
    #replace that part of the frame with the blended result
    frame[y:y+height, x:x+width] = background
    return frame


def tryOnCamera():
    tops, bottoms = loadClothingImages()
    currTop = 0
    currBottom = 0

    mpPose = mp.solutions.pose
    pose = mpPose.Pose()
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("⚠️ Could not read frame.")
            break
        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(rgb)

        #checks if the pose is detected and then extracts the landmarks on your body
        if results.pose_landmarks:
            landmarks = results.pose_landmarks.landmark
            left_shoulder = landmarks[mpPose.PoseLandmark.LEFT_SHOULDER]
            right_shoulder = landmarks[mpPose.PoseLandmark.RIGHT_SHOULDER]
            left_hip = landmarks[mpPose.PoseLandmark.LEFT_HIP]
            right_hip = landmarks[mpPose.PoseLandmark.RIGHT_HIP]

            #estimate position and size
            shoulder_x = int((left_shoulder.x + right_shoulder.x) / 2 * frame.shape[1])
            shoulder_y = int((left_shoulder.y + right_shoulder.y) / 2 * frame.shape[0])
            shoulder_width = int(abs(right_shoulder.x - left_shoulder.x) * frame.shape[1])

            hip_x = int((left_hip.x + right_hip.x) / 2 * frame.shape[1])
            hip_y = int((left_hip.y + right_hip.y) / 2 * frame.shape[0])
            hip_width = int(abs(right_hip.x - left_hip.x) * frame.shape[1])

            top_resized = cv2.resize(tops[currTop], (shoulder_width, shoulder_width))
            bottom_resized = cv2.resize(bottoms[currBottom], (hip_width, hip_width))

            frame = overlayPNG(frame, top_resized, shoulder_x - shoulder_width//2, shoulder_y - shoulder_width//2)
            frame = overlayPNG(frame, bottom_resized, hip_x - hip_width//2, hip_y - hip_width//4)

        cv2.imshow("Virtual Try-On", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('w'):
            currTop = (currTop + 1) % len(tops)
        elif key == ord('s'):
            currTop = (currTop - 1) % len(tops)
        elif key == ord('d'):
            currBottom = (currBottom + 1) % len(bottoms)
        elif key == ord('a'):
            currBottom = (currBottom - 1) % len(bottoms)

    cap.release()
    cv2.destroyAllWindows()
