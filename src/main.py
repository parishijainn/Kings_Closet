from cmu_graphics import *
from objects import HangerManager, OutfitManager
from ui import drawWelcomeScreen, drawMainGame
import os

# def onAppStart(app):
#     # Setup game dimensions
#     app.width = 800
#     app.height = 600
#     app.state = "welcome"
    
#     # Initialize managers
#     app.hangerManager = HangerManager(app)
#     app.outfitManager = OutfitManager(app)
    
#     # Welcome screen properties
#     app.welcomeText = "WELCOME TO CHER'S CLOSET"
#     app.instructionText = "click anywhere to begin"

# def onMousePress(app, mouseX, mouseY):
#     if app.state == "welcome":
#         app.state = "main"

# def onStep(app):
#     if app.state == "welcome":
#         app.hangerManager.update()
#     elif app.state == "main":
#         app.outfitManager.update()

# def redrawAll(app):
#     if app.state == "welcome":
#         drawWelcomeScreen(app)
#     elif app.state == "main":
#         drawMainGame(app)

# runApp(width=800, height=600)

from cmu_graphics import *
from objects import HangerManager, OutfitManager
from ui import drawWelcomeScreen, drawMainGame
import os

def onAppStart(app):
    app.width = 800
    app.height = 600
    app.state = "welcome"
    
    # Initialize managers
    # app.hangerManager = HangerManager(app)
    # app.outfitManager = OutfitManager(app)
    
    app.backgroundImage = "images/kingclosetbackgrounds.png"
    
    

    app.buttonX = app.width // 2 - 100
    app.buttonY = app.height // 2 
    app.buttonWidth = 200
    app.buttonHeight = 50
    app.buttonText = "START"
    app.buttonColor = "lightblue"
    app.buttonHoverColor = "blue"
    app.buttonTextColor = "white"
    app.buttonHoverTextColor = "white"
def onMousePress(app, mouseX, mouseY):
    # something like if app.state == welcome and they clicked within where the button is then app.state = main
    pass

def redrawAll(app):
    if app.state == "welcome":
        drawWelcomeScreen(app)
    elif app.state == "main":
        drawMainGame(app)

runApp(width=800, height=600)