# import cv2
# import numpy as np
# from sklearn.cluster import KMeans
# from cmu_graphics import *

# class OutfitManager:
#     def __init__(self, app):
#         self.app = app
#         self.tops = {
#             'shirt1': 'images/shirt1.png',
#             'shirt2': 'images/shirt2.png',
#             'shirt3': 'images/shirt3.png',
#             'shirt4': 'images/shirt4.png',
#             'shirt5': 'images/shirt5.png',
#             'shirt6': 'images/shirt6.png'
#         }

#         self.bottoms = {
#             'skirt1': 'images/skirt1.png',
#             'skirt2': 'images/skirt2.png',
#             'skirt3': 'images/skirt3.png'
#         }

#         self.colorRules = {
#             'yellow': ['yellow', 'blue', 'white', 'gray', 'black', 'brown', 'orange'],
#             'black': ['*'],
#             'white': ['*'],
#             'blue': ['blue', 'white', 'yellow', 'gray', 'black'],
#             'red': ['red', 'black', 'white'],
#             'green': ['green', 'white', 'black', 'brown'],
#             'brown': ['brown', 'cream', 'white', 'green'],
#             'pink': ['pink', 'white', 'blue', 'gray'],
#             'purple': ['purple', 'white', 'black', 'gray'],
#             'orange': ['orange', 'yellow', 'white', 'black', 'blue'],
#             'gray': ['*'],
#             'beige': ['white', 'brown', 'black'],
#             'cream': ['*']
#         }

#         self.colorCache = {}
#         self.currentOutfit = {'top': None, 'bottom': None}

#     def analyzeColors(self, imagePath):
#         if imagePath in self.colorCache:
#             return self.colorCache[imagePath]

#         img = cv2.imread(imagePath)
#         img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#         pixels = img.reshape(-1, 3)

#         kmeans = KMeans(n_clusters=3)
#         labels = kmeans.fit_predict(pixels)
#         colors = kmeans.cluster_centers_

#         counts = np.bincount(labels)
#         total = len(labels)

#         sortedIndices = np.argsort(-counts)
#         colorNames = []
#         for i in sortedIndices:
#             color = colors[i]
#             proportion = counts[i] / total
#             name = self.rgbToColorName(color)
#             if name not in colorNames:
#                 if proportion >= 0.10 or len(colorNames) == 0:
#                     colorNames.append(name)

#         result = {
#             'mainColor': colorNames[0],
#             'secondaryColors': colorNames[1:],
#             'isSolid': len(set(colorNames)) == 1
#         }

#         self.colorCache[imagePath] = result
#         return result

#     def rgbToColorName(self, rgb):
#         r, g, b = rgb
#         colorThresholds = {
#             'yellow': ((200, 170, 0), (255, 255, 150)),
#             'black': ((0, 0, 0), (40, 40, 40)),
#             'white': ((220, 220, 220), (255, 255, 255)),
#             'blue': ((0, 0, 100), (80, 150, 255)),
#             'red': ((130, 0, 0), (255, 100, 100)),
#             'green': ((0, 80, 0), (120, 255, 120)),
#             'brown': ((100, 50, 0), (160, 120, 90)),
#             'pink': ((200, 100, 120), (255, 180, 200)),
#             'purple': ((80, 0, 80), (180, 100, 200)),
#             'orange': ((200, 80, 0), (255, 180, 100)),
#             'gray': ((100, 100, 100), (180, 180, 180)),
#             'beige': ((180, 150, 100), (230, 210, 170)),
#             'cream': ((240, 220, 190), (255, 250, 230))
#         }

#         for name, ((rMin, gMin, bMin), (rMax, gMax, bMax)) in colorThresholds.items():
#             if rMin <= r <= rMax and gMin <= g <= gMax and bMin <= b <= bMax:
#                 return name

#         minDist = float('inf')
#         bestMatch = 'unknown'
#         for name, ((rMin, gMin, bMin), (rMax, gMax, bMax)) in colorThresholds.items():
#             avgColor = ((rMin + rMax) / 2, (gMin + gMax) / 2, (bMin + bMax) / 2)
#             dist = np.linalg.norm(np.array([r, g, b]) - np.array(avgColor))
#             if dist < minDist:
#                 minDist = dist
#                 bestMatch = name

#         return bestMatch

#     def gradeOutfit(self, topId, bottomId):
#         topPath = self.tops.get(topId)
#         bottomPath = self.bottoms.get(bottomId)

#         if not topPath or not bottomPath:
#             return ("Missing items!", "fail")

#         topInfo = self.analyzeColors(topPath)
#         bottomInfo = self.analyzeColors(bottomPath)
#         score = self.calculateMatchScore(topInfo, bottomInfo)

#         if score > 50:
#             self.app.money += 20
#             return ("Perfect match!", "perfect")
#         else:
#             return ("Mismatch! Try again!", "fail")


#     def calculateMatchScore(self, topInfo, bottomInfo):
#         score = 0
#         topColor = topInfo['mainColor']
#         bottomColor = bottomInfo['mainColor']

#         if topColor == bottomColor:
#             score += 90
#         elif '*' in self.colorRules.get(topColor, []):
#             score += 90
#         elif bottomColor in self.colorRules.get(topColor, []):
#             score += 50

#         if topInfo['isSolid'] and bottomInfo['isSolid']:
#             score += 20

#         sharedSecondaries = set(topInfo['secondaryColors']) & set(bottomInfo['secondaryColors'])
#         if sharedSecondaries:
#             score += min(10, len(sharedSecondaries) * 5)

#         return min(100, score)

import cv2
import numpy as np
from sklearn.cluster import KMeans
from cmu_graphics import *
class OutfitManager:
    def __init__(self, app):
        self.app = app
        self.tops = app.tops
        self.bottoms = app.bottoms

        self.colorRules = {
            'yellow': ['yellow', 'blue', 'white', 'gray', 'black', 'brown', 'orange'],
            'black': ['*'],
            'white': ['*'],
            'blue': ['blue', 'white', 'yellow', 'gray', 'black'],
            'red': ['red', 'black', 'white'],
            'green': ['green', 'white', 'black', 'brown'],
            'brown': ['brown', 'cream', 'white', 'green'],
            'pink': ['pink', 'white', 'blue', 'gray'],
            'purple': ['purple', 'white', 'black', 'gray'],
            'orange': ['orange', 'yellow', 'white', 'black', 'blue'],
            'gray': ['*'],
            'beige': ['white', 'brown', 'black'],
            'cream': ['*']
        }

        self.colorCache = {}

    def analyzeColors(self, imagePath):
        if imagePath in self.colorCache:
            return self.colorCache[imagePath]

        img = cv2.imread(imagePath)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        pixels = img.reshape(-1, 3)

        kmeans = KMeans(n_clusters=3)
        labels = kmeans.fit_predict(pixels)
        colors = kmeans.cluster_centers_

        counts = np.bincount(labels)
        total = len(labels)

        sortedIndices = np.argsort(-counts)
        colorNames = []
        for i in sortedIndices:
            color = colors[i]
            proportion = counts[i] / total
            name = self.rgbToColorName(color)
            if name not in colorNames:
                if proportion >= 0.10 or len(colorNames) == 0:
                    colorNames.append(name)

        result = {
            'mainColor': colorNames[0],
            'secondaryColors': colorNames[1:],
            'isSolid': len(set(colorNames)) == 1
        }

        self.colorCache[imagePath] = result
        return result

    def rgbToColorName(self, rgb):
        r, g, b = rgb
        colorThresholds = {
            'yellow': ((200, 170, 0), (255, 255, 150)),
            'black': ((0, 0, 0), (40, 40, 40)),
            'white': ((220, 220, 220), (255, 255, 255)),
            'blue': ((0, 0, 100), (80, 150, 255)),
            'red': ((130, 0, 0), (255, 100, 100)),
            'green': ((0, 80, 0), (120, 255, 120)),
            'brown': ((100, 50, 0), (160, 120, 90)),
            'pink': ((200, 100, 120), (255, 180, 200)),
            'purple': ((80, 0, 80), (180, 100, 200)),
            'orange': ((200, 80, 0), (255, 180, 100)),
            'gray': ((100, 100, 100), (180, 180, 180)),
            'beige': ((180, 150, 100), (230, 210, 170)),
            'cream': ((240, 220, 190), (255, 250, 230))
        }

        for name, ((rMin, gMin, bMin), (rMax, gMax, bMax)) in colorThresholds.items():
            if rMin <= r <= rMax and gMin <= g <= gMax and bMin <= b <= bMax:
                return name

        minDist = float('inf')
        bestMatch = 'unknown'
        for name, ((rMin, gMin, bMin), (rMax, gMax, bMax)) in colorThresholds.items():
            avgColor = ((rMin + rMax) / 2, (gMin + gMax) / 2, (bMin + bMax) / 2)
            dist = np.linalg.norm(np.array([r, g, b]) - np.array(avgColor))
            if dist < minDist:
                minDist = dist
                bestMatch = name

        return bestMatch

    def gradeOutfit(self, topIndex, bottomIndex):
        if topIndex >= len(self.tops) or bottomIndex >= len(self.bottoms):
            return ("Invalid outfit selection!", "fail")

        topPath = self.tops[topIndex].image
        bottomPath = self.bottoms[bottomIndex].image

        topInfo = self.analyzeColors(topPath)
        bottomInfo = self.analyzeColors(bottomPath)
        score = self.calculateMatchScore(topInfo, bottomInfo)

        if score > 50:
            self.app.money += 20
            return ("Perfect match!", "perfect")
        else:
            return ("Mismatch! Try again!", "fail")

    def calculateMatchScore(self, topInfo, bottomInfo):
        score = 0
        topColor = topInfo['mainColor']
        bottomColor = bottomInfo['mainColor']

        if topColor == bottomColor:
            score += 90
        elif '*' in self.colorRules.get(topColor, []):
            score += 90
        elif bottomColor in self.colorRules.get(topColor, []):
            score += 50

        if topInfo['isSolid'] and bottomInfo['isSolid']:
            score += 20

        sharedSecondaries = set(topInfo['secondaryColors']) & set(bottomInfo['secondaryColors'])
        if sharedSecondaries:
            score += min(10, len(sharedSecondaries) * 5)

        return min(100, score)
