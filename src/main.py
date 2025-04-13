from cmu_graphics import *
from objects import HangerManager, OutfitManager
from ui import drawWelcomeScreen, drawMainGame, drawInstructionsScreen 
import os

def onAppStart(app):
    app.width = 800
    app.height = 600
    app.state = "welcome"
    
    # Initialize managers
    # app.hangerManager = HangerManager(app)
    # app.outfitManager = OutfitManager(app)
    
    app.backgroundImage = "images/kingclosetbackgrounds.png"
    app.buttonWidth = 310
    app.buttonHeight = 80
    app.buttonX = app.width // 2 - app.buttonWidth // 2
    app.buttonY = app.height // 2 + 45

    
    app.mouseX = None
    app.mouseY = None

def onMousePress(app, mouseX, mouseY):
    if app.state == "welcome":
        if (app.buttonX <= mouseX <= app.buttonX + app.buttonWidth and
            app.buttonY <= mouseY <= app.buttonY + app.buttonHeight):
            app.state = "instructions"
def onMouseMove(app, mouseX, mouseY):
    app.mouseX = mouseX
    app.mouseY = mouseY

def redrawAll(app):
    if app.state == "welcome":
        drawWelcomeScreen(app)
    elif app.state == "instructions":
        drawInstructionsScreen(app)
    elif app.state == "main":
        drawMainGame(app)

runApp(width=800, height=600)

# from cmu_graphics import *
# from objects import VideoManager, OutfitManager
# from ui import drawWelcomeScreen, drawMainGame
# import os

# def onAppStart(app):
#     # Setup game dimensions
#     app.width = 800
#     app.height = 600
#     app.state = "welcome"
    
#     # Initialize managers
#     app.videoManager = VideoManager(app)
#     app.outfitManager = OutfitManager(app)

# def onMousePress(app, mouseX, mouseY):
#     # Check if start button was clicked
#     if (app.state == "welcome" and 
#         abs(mouseX - app.startButton['x']) < app.startButton['width']/2 and
#         abs(mouseY - app.startButton['y']) < app.startButton['height']/2):
#         app.state = "main"
#         app.videoManager.stopVideo()  # Stop video when leaving welcome screen

# def onStep(app):
#     if app.state == "welcome":
#         app.videoManager.update()

# def redrawAll(app):
#     if app.state == "welcome":
#         drawWelcomeScreen(app)
#     elif app.state == "main":
#         drawMainGame(app)

# runApp(width=800, height=600)