# from cmu_graphics import *
# import random

# def drawWelcomeScreen(app):
#     # Dark background like the movie
#     drawRect(0, 0, app.width, app.height, fill=rgb(30, 30, 30))
    
#     # Draw all hangers
#     for hanger in app.hangerManager.hangers:
#         drawImage("images/hanger.png", 
#                  hanger['x'], hanger['y'],
#                  width=60, height=80,
#                  rotateAngle=hanger['rotation'])
    
#     drawLabel(app.welcomeText, 
#              app.width/2, app.height/2 - 30, 
#              size=36, bold=True, fill='gold')
    
#     drawLabel(app.instructionText,
#              app.width/2, app.height/2 + 30,
#              size=20, fill='white')

# def drawMainGame(app):
#     # Pink background like Clueless
#     drawRect(0, 0, app.width, app.height, fill='pink')
    
#     # Decorative border
#     drawCheetahBorder(app)
    
#     # Main game UI
#     drawLabel("CHER'S WARDROBE", app.width/2, 50, 
#              size=28, font='monospace', bold=True)
#     drawLabel("FALL FASHIONS", app.width/2, 80, 
#              size=20, font='monospace')
    
#     # Placeholder for outfit display
#     drawLabel("OUTFIT SELECTION COMING SOON", 
#              app.width/2, app.height/2, size=20)

# def drawCheetahBorder(app):
#     # Simple cheetah print pattern around edges
#     for x in range(0, app.width, 40):
#         for y in range(0, app.height, 40):
#             if x < 40 or x > app.width-40 or y < 40 or y > app.height-40:
#                 if random.random() > 0.7:
#                     drawCircle(x, y, 15, fill='black')
#                     drawCircle(x+5, y+5, 5, fill='gold')

from cmu_graphics import *

def drawWelcomeScreen(app):
    # Draw background image
    drawImage(app.backgroundImage, 0, 0, width=app.width, height=app.height)
    
    # Draw start button (placeholder)
    drawStartButton(app)

def drawStartButton(app):
    pass
    

def drawMainGame(app):
    # Draw background image
    drawImage(app.backgroundImage, 0, 0, width=app.width, height=app.height)
    
    