from cmu_graphics import *
from objects import HangerManager, OutfitManager
from ui import drawWelcomeScreen, drawMainGame, drawInstructionsScreen 
from gameMode import drawGameMode
import os

def onAppStart(app):
    app.width = 800
    app.height = 600
    app.state = "welcome"
    #gameMode
    app.isSelectionMode = True
    app.isDressingMode = False
    app.currTopIndex = 0
    app.currBottomIndex = 0
    app.modeButtonWidth, app.modeButtonHeight = 160, 80
    app.blackBarHeight = 80
    
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

    app.instructionsButtonWidth = 250
    app.instructionsButtonHeight = 60
    app.instructionsButtonX = app.width // 2 - app.instructionsButtonWidth // 2
    app.instructionsButtonY = app.height - 120
    app.instructionsButtonText = "Start Styling"    

def onMousePress(app, mouseX, mouseY):
    if app.state == "welcome":
        if (app.buttonX <= mouseX <= app.buttonX + app.buttonWidth and
            app.buttonY <= mouseY <= app.buttonY + app.buttonHeight):
            app.state = "instructions"
            
    if app.state == "instructions":
        if (app.instructionsButtonX <= mouseX <= app.instructionsButtonX + app.instructionsButtonWidth and
            app.instructionsButtonY <= mouseY <= app.instructionsButtonY + app.instructionsButtonHeight):
            app.state = "gameMode"   

    if app.state == 'gameMode':    
        if ((2*(app.width/3) <= mouseX <= 2*(app.width/3) + app.modeButtonWidth) and
            ((app.height-app.blackBarHeight-app.modeButtonHeight <= mouseY <= app.height-app.blackBarHeight))):
            #dressme mode
            app.isDressingMode = True
            app.isSelectionMode = False
        if ((app.width-app.modeButtonWidth <= mouseX <= app.width-app.modeButtonWidth + app.modeButtonWidth) and
            (app.height-app.blackBarHeight-app.modeButtonHeight <= mouseY <= app.height-app.blackBarHeight-app.modeButtonHeight + app.modeButtonHeight)):
            #browse mode
            app.isDressingMode = False
            app.isSelectionMode = True

    
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
    elif app.state == 'gameMode':
        drawGameMode(app)

runApp(width=800, height=600)