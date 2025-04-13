import cv2
import numpy as np
from sklearn.cluster import KMeans
from cmu_graphics import *

class OutfitManager:
    def __init__(self, app):
        self.tops = {
            'shirt1': 'images/shirt1.png',
            'shirt2': 'images/shirt2.png',
            'shirt3': 'images/shirt3.png',
            'shirt4': 'images/shirt4.png',
            'shirt5': 'images/shirt5.png',
            'shirt6': 'images/shirt6.png'
        }
        
        self.bottoms = {
            'bottom1': 'images/bottom1.png',
            'bottom2': 'images/bottom2.png',
            'bottom3': 'images/bottom3.png',
            'skirt1': 'images/skirt1.png',
            'skirt2': 'images/skirt2.png',
            'skirt3': 'images/skirt3.png'
        }
        
        # Fashion rules- determining which colors go together
        # '*' means that any color can be worn with that color
        self.colorRules = {
            'yellow': ['blue', 'black', 'white', 'gray', 'yellow'],
            'black': ['*'],  
            'white': ['*'],
            'blue': ['white', 'yellow', 'gray', 'black'],
            'red': ['black', 'white']
        }
        
        self.currentOutfit = {'top': None, 'bottom': None}
        self.colorCache = {}

    # This function uses KMeans clustering to analyze the colors in the image
    # It determines the main color in the clothing and the secondary colors
    # It also extracts the RGB values of the colors
    # It returns a dictionary with the main color, secondary colors, and whether the outfit is solid
    # The function also caches the results to avoid reprocessing the same image
    def analyzeColors(self, imagePath):
        if imagePath in self.colorCache:
            return self.colorCache[imagePath]
        
        try:
            img = cv2.imread(imagePath)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            pixels = img.reshape(-1, 3)

            # Identify the 3 main color clusters
            kmeans = KMeans(n_clusters=3)
            kmeans.fit(pixels)
            colors = kmeans.cluster_centers_

            colorNames = [self.rgbToColorName(color) for color in colors]

            result = {
                'mainColor': colorNames[0],
                'secondaryColors': colorNames[1:],
                'isSolid': len(set(colorNames)) == 1
            }

            self.colorCache[imagePath] = result
            return result

        except Exception as e:
            print(f"Color analysis error: {e}")
            return {
                'mainColor': 'unknown',
                'secondaryColors': [],
                'isSolid': False
            }

    def rgbToColorName(self, rgb):
        r, g, b = rgb
        colorThresholds = {
            'yellow': ((200, 150, 0), (255, 255, 150)),
            'black': ((0, 0, 0), (50, 50, 50)),
            'white': ((200, 200, 200), (255, 255, 255)),
            'blue': ((0, 0, 150), (100, 100, 255)),
            'red': ((150, 0, 0), (255, 100, 100))
        }

        for name, ((rMin, gMin, bMin), (rMax, gMax, bMax)) in colorThresholds.items():
            if rMin <= r <= rMax and gMin <= g <= gMax and bMin <= b <= bMax:
                return name
        return 'unknown'

    # Grades based on the AI color analysis
    def gradeOutfit(self, topId, bottomId):
        topPath = self.tops.get(topId)
        bottomPath = self.bottoms.get(bottomId)

        if not topPath or not bottomPath:
            return ("Missing items!", "fail", 0)

        topInfo = self.analyzeColors(topPath)
        bottomInfo = self.analyzeColors(bottomPath)
        score = self.calculateMatchScore(topInfo, bottomInfo)

        if score >= 90:
            return ("Perfect match! As if!", "perfect", score)
        elif score >= 70:
            return ("Looking cute!", "good", score)
        elif score >= 50:
            return ("Not terrible...", "okay", score)
        else:
            return ("Fashion disaster!", "fail", score)

    def calculateMatchScore(self, top, bottom):
        score = 0

        if bottom['mainColor'] in self.colorRules.get(top['mainColor'], []):
            score += 60
        elif '*' in self.colorRules.get(top['mainColor'], []):
            score += 50
        elif top['mainColor'] == bottom['mainColor']:
            score += 40

        if top['isSolid'] and bottom['isSolid']:
            score += 20

        commonSecondaries = set(top['secondaryColors']) & set(bottom['secondaryColors'])
        if commonSecondaries:
            score += min(10, len(commonSecondaries) * 5)

        return min(100, score)
