from cmu_graphics import *
from objects import HangerManager, OutfitManager
from ui import drawWelcomeScreen, drawMainGame
<<<<<<< HEAD
=======
import os
>>>>>>> a000bf385b97a688ebbcda8e68bd40baccc2907c

def onAppStart(app):
    # Setup game dimensions
    app.width = 800
    app.height = 600
    app.state = "welcome"
    
    # Initialize managers
    app.hangerManager = HangerManager(app)
    app.outfitManager = OutfitManager(app)
    
    # Welcome screen properties
    app.welcomeText = "WELCOME TO CHER'S CLOSET"
    app.instructionText = "click anywhere to begin"

def onMousePress(app, mouseX, mouseY):
    if app.state == "welcome":
        app.state = "main"

def onStep(app):
    if app.state == "welcome":
        app.hangerManager.update()
    elif app.state == "main":
        app.outfitManager.update()

def redrawAll(app):
    if app.state == "welcome":
        drawWelcomeScreen(app)
    elif app.state == "main":
        drawMainGame(app)

runApp(width=800, height=600)