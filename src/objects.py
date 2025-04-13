from cmu_graphics import *
import random
# import numpy as np
# import cv2

class HangerManager:
    # def __init__(self, app):
    #     self.app = app
    #     self.hangers = []
    #     self.createHangers(15) 

    # def createHangers(self, count):
    #     for _ in range(count):
    #         x = random.randint(0, self.app.width)
    #         y = random.randint(0, self.app.height)
    #         speed = random.uniform(0.5, 2.5)
    #         angle = random.uniform(0, 360)
    #         rotation = random.uniform(0, 360)
    #         self.hangers.append({
    #             'x': x, 'y': y, 
    #             'speed': speed,
    #             'angle': angle,
    #             'rotation': rotation,
    #             'rotationSpeed': random.uniform(-1, 1)
    #         })
    pass

class OutfitManager:
    # def __init__(self, app):
    #     self.app = app
    #     self.currentTop = 0
    #     self.currentBottom = 0
    #     self.loadClothingItems()
        
    # def loadClothingItems(self):
    #     # Placeholder for clothing items
    #     self.tops = []
    #     self.bottoms = []
    
    # def update(self):
    #     # Will be used for outfit matching logic
    pass

# class VideoManager:
#     def __init__(self, app):
#         self.app = app
#         self.videoPath = "images/welcome_video.mp4"
#         self.cap = cv2.VideoCapture(self.videoPath)
#         self.currentFrame = None
#         self.videoPlaying = True
        
#         # Get video properties
#         self.width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#         self.height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#         self.fps = self.cap.get(cv2.CAP_PROP_FPS)
        
#     def update(self):
#         if self.videoPlaying:
#             ret, frame = self.cap.read()
#             if not ret:
#                 # Loop the video
#                 self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
#                 ret, frame = self.cap.read()
            
#             # Convert BGR to RGB
#             frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#             # Resize to fit app window
#             frame = cv2.resize(frame, (self.app.width, self.app.height))
#             self.currentFrame = frame
    
#     def stopVideo(self):
#         self.videoPlaying = False
#         self.cap.release()
    
#     def getCurrentFrame(self):
#         return self.currentFrame

# class OutfitManager:
#     def __init__(self, app):
#         pass