from cmu_graphics import *
from ui import * 
from buttons import *
from gameMode import drawGameMode
from clothesClasses import *
from outfitgrader import OutfitManager
import os
import random


def onAppStart(app):
    app.width = 800
    app.height = 600
    app.state = "welcome"

    #WELCOMEMODE
    app.backgroundImage = "images/kingclosetbackgrounds.png"
    app.buttonWidth = 310
    app.buttonHeight = 80
    app.buttonX = app.width // 2 - app.buttonWidth // 2
    app.buttonY = app.height // 2 + 45

    #INSTRUCTIONSMODE
    app.scrollY = 0
    app.maxScrollUp = 0
    app.maxScrollDown = 200

    app.instructionsBackgroundImage = "images/instructions.png"
    app.instructionsButtonWidth = 250
    app.instructionsButtonHeight = 60
    app.instructionsButtonX = app.width // 2 - app.instructionsButtonWidth // 2
    app.instructionsButtonY = app.height - 120
    app.instructionsButtonText = "Start Styling"
    
    #GAMEMODE
    app.isSelectionMode = True
    app.isDressingMode = False

    app.currTopIndex = 0
    app.currBottomIndex = 0
    app.tops = [Tops("images/shirt1.png"), Tops("images/shirt2.png"), Tops("images/shirt3.png"), Tops("images/shirt4.png"), Tops("images/shirt5.png"), Tops("images/shirt6.png")]
    app.bottoms = [Bottoms("images/skirt1.png"), Bottoms("images/skirt2.png"), Bottoms("images/skirt3.png"), Bottoms("images/bottom1.png"), Bottoms("images/bottom2.png"), Bottoms("images/bottom3.png")]
    
    #Background
    app.gameScreenBackgroundImage = "images/cheetahBackGround.png"
    app.blackBarHeight = 50
    app.whiteBoxWidth = app.width/3
    app.whiteBoxHeight = app.height - 2*app.blackBarHeight
    app.whiteBoxX = app.width/3

    #Mode Switch Buttons
    app.modeButtonWidth = 160
    app.modeButtonHeight = 80

    #Clothes Selection Buttons
    app.backwardButtonWidth = app.whiteBoxWidth*0.33
    app.backwardButtonHeight = app.blackBarHeight - app.blackBarHeight*0.2
    app.backwardButtonX = app.whiteBoxWidth+10
    app.backwardButtonY = ((app.height/2) - app.blackBarHeight +
                      (app.blackBarHeight-app.backwardButtonHeight)/2)
    
    app.forwardButtonX = app.width - app.whiteBoxWidth - app.backwardButtonWidth - 10
    
    app.playButtonWidth = app.backwardButtonWidth*0.66
    app.playButtonHeight = app.backwardButtonHeight
    app.playButtonX = app.width/2 - app.playButtonWidth/2
    app.playButtonY = app.backwardButtonY

    #Grade Button
    app.gradeButtonX = app.width - 150
    app.gradeButtonY = 5
    app.gradeButtonWidth = 100
    app.gradeButtonHeight = app.blackBarHeight - 10

    #Try On Button
    app.tryOnButtonX = 120
    app.tryOnButtonY = 5
    app.tryOnButtonWidth = 100
    app.tryOnButtonHeight = app.blackBarHeight - 10

    #Import Clothes Button
    app.importButtonX = 10
    app.importButtonY = 5
    app.importButtonWidth = 100
    app.importButtonHeight = app.blackBarHeight - 10

    #GRADEMODE
    #Back Button
    app.backButtonX = app.width/2 - 60
    app.backButtonY = app.height - 60
    app.backButtonWidth = 120
    app.backButtonHeight = 40
    
    
    # Initialize managers
    # app.hangerManager = HangerManager(app)
    # app.outfitManager = OutfitManager(app)

    app.sound = Sound('kidsInAmerica.mp3')
    app.soundIsPlaying = False
    app.soundButtonX = app.width - 40
    app.soundButtonY = 10
    app.soundButtonSize = 30
    
    app.outfitManager = OutfitManager(app)
    app.topKeys = list(app.outfitManager.tops.keys())
    app.bottomKeys = list(app.outfitManager.bottoms.keys())

    app.mouseX = None
    app.mouseY = None
    app.isGrading = False

    app.feedbackText = ""

def onMousePress(app, mouseX, mouseY):
    pressSoundButton(app)
    if app.state == "welcome":
        pressStartPlayingButton(app)
    
    elif app.state == "instructions":
        pressStartStylingButton(app)

    elif app.state == 'gameMode':
        pressGradeButton(app)
        pressModeButtons(app)
        pressSelectionButtons(app)
        
    elif app.state == "gradeMode":
        pressBackButton(app)

def onMouseMove(app, mouseX, mouseY):
    app.mouseX = mouseX
    app.mouseY = mouseY

        # Evaluate outfit
    if app.isSelectionMode:
        playButtonX = app.width / 2 - 50
        playButtonY = app.height - app.blackBarHeight - 60
        if playButtonX <= mouseX <= playButtonX + 100 and playButtonY <= mouseY <= playButtonY + 40:
            topKey = app.topKeys[app.currTopIndex % len(app.topKeys)]
            bottomKey = app.bottomKeys[app.currBottomIndex % len(app.bottomKeys)]
            message, rating, score = app.outfitManager.grade_outfit(topKey, bottomKey)
            app.feedbackText = f"{message} ({score}%)"

def onKeyPress(app, key):
    if app.state == "instructions":
        if key == "up" and app.scrollY < app.maxScrollUp:
            app.scrollY += 20
        elif key == "down" and app.scrollY > -app.maxScrollDown:
            app.scrollY -= 20
    if key == 'p':
        app.sound.play(restart=True)

    elif app.state == "gameMode":
        if key == "left":
            app.currTopIndex = (app.currTopIndex - 1) % len(app.topKeys)
        elif key == "right":
            app.currTopIndex = (app.currTopIndex + 1) % len(app.topKeys)
        elif key == "up":
            app.currBottomIndex = (app.currBottomIndex - 1) % len(app.bottomKeys)
        elif key == "down":
            app.currBottomIndex = (app.currBottomIndex + 1) % len(app.bottomKeys)

def onMouseMove(app, mouseX, mouseY):
    app.mouseX = mouseX
    app.mouseY = mouseY

def redrawAll(app):
    if app.state == "welcome":
        drawWelcomeScreen(app)
    elif app.state == "instructions":
        drawInstructionsScreen(app)
    elif app.state == "gameMode":
        drawGameMode(app)
    elif app.state == "gradeMode":
        drawGameScreen(app)

    drawSoundButton(app)

runApp(width=800, height=600)

def drawGameScreen(app):
    drawRect(0, 0, app.width, app.height, fill='pink')
    drawLabel("King's Closet: Outfit Grader", app.width // 2, 30, size=28, bold=True)

    topImg = app.outfitManager.tops[app.topKeys[app.currTopIndex % len(app.topKeys)]]
    bottomImg = app.outfitManager.bottoms[app.bottomKeys[app.currBottomIndex % len(app.bottomKeys)]]

    drawImage(topImg, app.width//2, 140, width=180, height=180, align='center')
    drawImage(bottomImg, app.width//2, 320, width=180, height=180, align='center')

    drawLabel(app.feedbackText, app.width//2, app.height - 100, size=22, fill='darkmagenta')
    drawRect(app.gradeButtonX, app.gradeButtonY, app.gradeButtonWidth, app.gradeButtonY, fill='plum', border='black')
    drawLabel("Grade", app.width/2, app.height - app.blackBarHeight - 40, size=18, bold=True)

runApp()