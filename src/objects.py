from cmu_graphics import *
import random

class HangerManager:
    def __init__(self, app):
        self.app = app
        self.hangers = []
        self.createHangers(15)  # Create 15 hangers
        
    def createHangers(self, count):
        for _ in range(count):
            x = random.randint(0, self.app.width)
            y = random.randint(0, self.app.height)
            speed = random.uniform(0.5, 2.5)
            angle = random.uniform(0, 360)
            rotation = random.uniform(0, 360)
            self.hangers.append({
                'x': x, 'y': y, 
                'speed': speed,
                'angle': angle,
                'rotation': rotation,
                'rotationSpeed': random.uniform(-1, 1)
            })
    
    def update(self):
        for hanger in self.hangers:
            # Update position
            hanger['x'] += hanger['speed'] * cos(hanger['angle'])
            hanger['y'] += hanger['speed'] * sin(hanger['angle'])
            hanger['rotation'] += hanger['rotationSpeed']
            
            # Bounce off edges
            if hanger['x'] <= 0 or hanger['x'] >= self.app.width:
                hanger['angle'] = 180 - hanger['angle']
            if hanger['y'] <= 0 or hanger['y'] >= self.app.height:
                hanger['angle'] = -hanger['angle']

class OutfitManager:
    def __init__(self, app):
        self.app = app
        self.currentTop = 0
        self.currentBottom = 0
        self.loadClothingItems()
        
    def loadClothingItems(self):
        # Placeholder for clothing items
        self.tops = []
        self.bottoms = []
    
    def update(self):
        # Will be used for outfit matching logic
        pass