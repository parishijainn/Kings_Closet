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
        
        # color matching
        self.color_rules = {
            'yellow': ['blue', 'black', 'white', 'gray'],
            'black': ['*'],  
            'white': ['*'],
            'blue': ['white', 'yellow', 'gray'],
            'red': ['black', 'white', 'blue'],
            'plaid': ['solid', 'denim']  
        }
        
        self.current_outfit = {'top': None, 'bottom': None}
        self.color_cache = {}  

    def analyze_colors(self, image_path):
        """AI-powered color analysis using K-means clustering"""
        if image_path in self.color_cache:
            return self.color_cache[image_path]
            
        try:
            img = cv2.imread(image_path)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            pixels = img.reshape(-1, 3)
            
            # Use K-means to find dominant colors
            kmeans = KMeans(n_clusters=3)
            kmeans.fit(pixels)
            colors = kmeans.cluster_centers_
            
            # Convert to color names
            color_names = [self.rgb_to_color_name(color) for color in colors]
            
            # Determine if plaid pattern exists
            is_plaid = self.detect_plaid_pattern(img)
            
            result = {
                'main_color': color_names[0],
                'secondary_colors': color_names[1:],
                'is_plaid': is_plaid,
                'is_solid': len(set(color_names)) == 1
            }
            
            self.color_cache[image_path] = result
            return result
            
        except Exception as e:
            print(f"Color analysis error: {e}")
            return {
                'main_color': 'unknown',
                'secondary_colors': [],
                'is_plaid': False,
                'is_solid': False
           }


    def rgb_to_color_name(self, rgb):
        """Convert RGB to color names with your specific palette"""
        r, g, b = rgb
        color_thresholds = {
            'yellow': ((200, 150, 0), (255, 255, 150)),
            'black': ((0, 0, 0), (50, 50, 50)),
            'white': ((200, 200, 200), (255, 255, 255)),
            'blue': ((0, 0, 150), (100, 100, 255)),
            'red': ((150, 0, 0), (255, 100, 100))
        }
        
        for name, ((r_min, g_min, b_min), (r_max, g_max, b_max)) in color_thresholds.items():
            if (r_min <= r <= r_max and g_min <= g <= g_max and b_min <= b <= b_max):
                return name
        return 'unknown'

    def grade_outfit(self, top_id, bottom_id):
        """Grade the outfit combination with AI analysis"""
        top_path = self.tops.get(top_id)
        bottom_path = self.bottoms.get(bottom_id)
        
        if not top_path or not bottom_path:
            return ("Missing items!", "fail", 0)
        
        # Analyze both pieces
        top_info = self.analyze_colors(top_path)
        bottom_info = self.analyze_colors(bottom_path)
        score = self.calculate_match_score(top_info, bottom_info)
        
        # feedback
        if score >= 90:
            return ("Perfect match! As if!", "perfect", score)
        elif score >= 70:
            return ("Looking cute!", "good", score)
        elif score >= 50:
            return ("Not terrible...", "okay", score)
        else:
            return ("Fashion disaster!", "fail", score)

    def calculate_match_score(self, top, bottom):
        """Advanced scoring considering colors and patterns"""
        score = 0
        
        if bottom['main_color'] in self.color_rules.get(top['main_color'], []):
            score += 60
        elif '*' in self.color_rules.get(top['main_color'], []):
            score += 50
        elif top['main_color'] == bottom['main_color']:
            score += 40
            
        if top['is_plaid'] and bottom['is_solid']:
            score += 30  
        elif not top['is_plaid'] and not bottom['is_plaid']:
            score += 20  
            
        common_secondaries = set(top['secondary_colors']) & set(bottom['secondary_colors'])
        if common_secondaries:
            score += min(10, len(common_secondaries) * 5)
            
        return min(100, score) 