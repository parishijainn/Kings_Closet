from cmu_graphics import *
import cv2
import numpy as np
from sklearn.cluster import KMeans

class OutfitManager:
    def __init__(self, app):
        self.jackets = {
            'jacket1.png': {'main_color': 'brown', 'secondary_color': 'light blue'},
            'jacket2.png': {'main_color': 'blue', 'secondary_color': 'yellow'},
            'jacket3.png': {'main_color': 'gray', 'secondary_color': None},
            'jacket4.png': {'main_color': 'yellow', 'secondary_color': None},
            'jacket5.png': {'main_color': 'pink', 'secondary_color': None},
            'jacket6.png': {'main_color': 'green', 'secondary_colors': ['maroon', 'yellow']},
            'jacket7.png': {'main_color': 'red', 'secondary_color': 'white'},
            'jacket8.png': {'main_color': 'orange', 'secondary_color': 'teal'},
            'jacket9.png': {'main_color': 'bluegreen', 'secondary_color': 'white'}
        }
        
        self.color_rules = {
            'brown': ['light blue', 'white', 'pink'],
            'blue': ['yellow', 'white', 'orange'],
            'gray': ['*'],
            'yellow': ['blue', 'purple', 'black'],
            'pink': ['brown', 'white', 'black'],
            'green': ['maroon', 'yellow', 'white'],
            'red': ['white', 'black', 'blue'],
            'orange': ['teal', 'white', 'black'],
            'bluegreen': ['white', 'orange', 'yellow']
        }
        
        self.current_outfit = {'top': None, 'bottom': None}
    
    def analyze_real_clothing(self, image_path):
        try:
            # Load image
            img = cv2.imread(image_path)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = cv2.resize(img, (200, 200))
            dominant_color = self.get_dominant_color(img)
            color_name = self.rgb_to_color_name(dominant_color)
            return {'main_color': color_name}
        except Exception as e:
            print(f"Error analyzing image: {e}")
            return {'main_color': 'unknown'}

    # Chat-GPT Citation: Lines 47-70
    def get_dominant_color(self, img, k=3):
        """Extract dominant color using K-means clustering"""
        pixels = img.reshape(-1, 3)
        kmeans = KMeans(n_clusters=k)
        kmeans.fit(pixels)
        return kmeans.cluster_centers_[0]

    def rgb_to_color_name(self, rgb):
        """Convert RGB values to color names"""
        r, g, b = rgb
        color_map = {
            (139, 69, 19): 'brown',
            (0, 0, 255): 'blue',
            (128, 128, 128): 'gray',
            (255, 255, 0): 'yellow',
            (255, 192, 203): 'pink',
            (0, 128, 0): 'green',
            (255, 0, 0): 'red',
            (255, 165, 0): 'orange',
            (0, 139, 139): 'teal',
            (0, 206, 209): 'bluegreen',
            (255, 255, 255): 'white'
        }
        
        # Find closest named color
        closest_color = None
        min_distance = float('inf')
        
        for color_rgb, name in color_map.items():
            distance = sum((c1 - c2)**2 for c1, c2 in zip(rgb, color_rgb))
            if distance < min_distance:
                min_distance = distance
                closest_color = name
                
        return closest_color or 'unknown'

    def grade_outfit(self, top, bottom, is_real_photo=False):
        """Grade the outfit combination"""
        if is_real_photo:
            top_info = self.analyze_real_clothing(top)
            bottom_info = self.analyze_real_clothing(bottom)
        else:
            top_info = self.jackets.get(top, {})
            bottom_info = self.jackets.get(bottom, {})
        
        return self._calculate_match(top_info, bottom_info)

    def _calculate_match(self, top, bottom):
        """Core matching logic"""
        if not top or not bottom:
            return ("Missing items!", "fail", 0)
            
        top_color = top.get('main_color', 'unknown')
        bottom_color = bottom.get('main_color', 'unknown')
        
        # Check if colors match
        if (bottom_color in self.color_rules.get(top_color, []) or 
            '*' in self.color_rules.get(top_color, [])):
            return ("Perfect match! As if!", "perfect", 100)
        elif top_color == bottom_color:
            return ("Monochromatic look!", "good", 75)
        else:
            return ("Fashion disaster!", "fail", 30)