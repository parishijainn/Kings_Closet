# from cmu_graphics import *
# from objects import HangerManager, OutfitManager
# from ui import drawWelcomeScreen, drawMainGame
# import os

# def onAppStart(app):
#     app.width = 800
#     app.height = 600
#     app.state = "welcome"
    
#     # Initialize managers
#     # app.hangerManager = HangerManager(app)
#     # app.outfitManager = OutfitManager(app)
    
#     app.backgroundImage = "images/kingclosetbackgrounds.png"
    

# def onMousePress(app, mouseX, mouseY):
#     # something like if app.state == welcome and they clicked within where the button is then app.state = main
#     pass

# def redrawAll(app):
#     if app.state == "welcome":
#         drawWelcomeScreen(app)
#     elif app.state == "main":
#         drawMainGame(app)

# runApp(width=800, height=600)

from cmu_graphics import *
from objects import VideoManager, OutfitManager
from ui import drawWelcomeScreen, drawMainGame
import os

def onAppStart(app):
    # Setup game dimensions
    app.width = 800
    app.height = 600
    app.state = "welcome"
    
    # Initialize managers
    app.videoManager = VideoManager(app)
    app.outfitManager = OutfitManager(app)
    
    # Start button properties
    app.startButton = {
        'x': app.width/2,
        'y': app.height - 100,
        'width': 200,
        'height': 60
    }

def onMousePress(app, mouseX, mouseY):
    # Check if start button was clicked
    if (app.state == "welcome" and 
        abs(mouseX - app.startButton['x']) < app.startButton['width']/2 and
        abs(mouseY - app.startButton['y']) < app.startButton['height']/2):
        app.state = "main"
        app.videoManager.stopVideo()  # Stop video when leaving welcome screen

def onStep(app):
    if app.state == "welcome":
        app.videoManager.update()

def redrawAll(app):
    if app.state == "welcome":
        drawWelcomeScreen(app)
    elif app.state == "main":
        drawMainGame(app)

runApp(width=800, height=600)