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
    
    
# from cmu_graphics import *
# import numpy as np

# def drawWelcomeScreen(app):
#     # Draw video frame if available
#     if app.videoManager.currentFrame is not None:
#         frame = app.videoManager.currentFrame
#         # Convert numpy array to CMU Graphics image
#         drawImage(frame, 0, 0, width=app.width, height=app.height)
    
#     # Dark overlay for better button visibility
#     drawRect(0, 0, app.width, app.height, fill='black', opacity=30)
    
#     # Draw start button
#     drawStartButton(app)

# def drawStartButton(app):
#     # Button background
#     drawRect(app.startButton['x'] - app.startButton['width']/2,
#              app.startButton['y'] - app.startButton['height']/2,
#              app.startButton['width'],
#              app.startButton['height'],
#              fill='gold', border='black', borderWidth=2)
    
#     # Button text
#     drawLabel("START GAME", 
#              app.startButton['x'], 
#              app.startButton['y'],
#              size=20, bold=True, fill='black')

# def drawMainGame(app):
#     # Placeholder for main game
#     drawRect(0, 0, app.width, app.height, fill='pink')
#     drawLabel("MAIN GAME SCREEN", 
#              app.width/2, app.height/2,
#              size=24, bold=True)
