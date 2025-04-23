from cmu_graphics import *
from ui import * 
from buttons import *
from gameMode import drawGameMode
from clothesClasses import *
from outfitgrader import OutfitManager
import os
import random
from tkinter import filedialog, Tk
from virtualtryon import tryOnCamera
from handtracking import processCameraFeed, getFingerPosition
from storeMode import *

def onAppStart(app):
    app.width = 800
    app.height = 600
    app.state = "welcome"

    app.closetTops = []
    app.closetBottoms = []
    app.storePage = "pickType"
    app.money = 500
    app.closetTopPrices = [20, 20, 20, 20, 20, 20]
    app.closetBottomPrices = [20, 20, 20, 20, 20, 20]
    app.closetTopTypes = ["Tees", "Tees", "Tees", "Tees", "Tees", "Tees"]
    app.closetBottomTypes = ['Jeans', 'Jeans', 'Jeans', 'Jeans', 'Jeans', 
                             'Jeans']

    #INSTRUCTIONS POPUPS
    app.popupX = app.width//2
    app.popupY = app.height//2
    app.popupWidth = 600
    app.popupHeight = 300
    app.isInstructing = True

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
    app.tops = [Tops("images/shirt1.png"), Tops("images/shirt2.png"), 
                Tops("images/shirt3.png"), Tops("images/shirt4.png"), 
                Tops("images/shirt5.png"), Tops("images/shirt6.png")]
    app.bottoms = [Bottoms("images/skirt1.png"), Bottoms("images/skirt2.png"), 
                   Bottoms("images/skirt3.png"), Bottoms("images/bottom1.png"), 
                   Bottoms("images/bottom2.png"), Bottoms("images/bottom3.png")]
    app.visibleTopIndex = app.currTopIndex
    app.visibleBottomIndex = app.currBottomIndex

    
    #BACKGROUND
    app.gameScreenBackgroundImage = "images/cheetahBackGround.png"
    app.blackBarHeight = 50
    app.whiteBoxWidth = app.width/3
    app.whiteBoxHeight = app.height - 2*app.blackBarHeight
    app.whiteBoxX = app.width/3

    #MODE BUTTONS
    app.modeButtonWidth = 160
    app.modeButtonHeight = 80

    #CLOTHES SELECTION BUTTONS
    app.backwardButtonWidth = app.whiteBoxWidth*0.33
    app.backwardButtonHeight = app.blackBarHeight - app.blackBarHeight*0.2
    app.backwardButtonX = app.whiteBoxWidth+10
    app.backwardButtonY = ((app.height/2) - app.blackBarHeight +
                      (app.blackBarHeight-app.backwardButtonHeight)/2)
    
    app.forwardButtonX = app.width - app.whiteBoxWidth - app.backwardButtonWidth - 10
    
    #SOUND BUTTON
    app.playButtonWidth = app.backwardButtonWidth*0.66
    app.playButtonHeight = app.backwardButtonHeight
    app.playButtonX = app.width/2 - app.playButtonWidth/2
    app.playButtonY = app.backwardButtonY
    app.sound = Sound('kidsInAmerica.mp3')
    app.soundIsPlaying = False
    app.soundButtonX = app.width - 40
    app.soundButtonY = 10
    app.soundButtonSize = 30

    #GRADE BUTTON
    app.gradeButtonX = app.width - 150 
    app.gradeButtonY = 5
    app.gradeButtonWidth = 100
    app.gradeButtonHeight = app.blackBarHeight - 10

    #TRY ON BUTTON
    app.tryOnButtonX = 545
    app.tryOnButtonY = 5
    app.tryOnButtonWidth = 100
    app.tryOnButtonHeight = app.blackBarHeight - 10

    #STORE BUTTON
    app.storeButtonX = 305
    app.storeButtonY = 5
    app.storeButtonWidth = 100
    app.storeButtonHeight = app.blackBarHeight - 10

    #MONEY BUTTON
    app.moneyButtonX = app.width - 45
    app.moneyButtonY = app.blackBarHeight + 20
    app.moneyButtonR = 20

    #BACK BUTTON
    app.backButtonX = app.width/2 - 60
    app.backButtonY = app.height - 60
    app.backButtonWidth = 120
    app.backButtonHeight = 40
    app.universalBackButtonWidth = 100
    app.universalBackButtonHeight = 40
    app.universalBackButtonX = 20
    app.universalBackButtonY = app.height - app.universalBackButtonHeight - 5

    app.outfitManager = OutfitManager(app)
    app.topKeys = list(app.outfitManager.tops.keys())
    app.bottomKeys = list(app.outfitManager.bottoms.keys())
    
    app.mouseX = None
    app.mouseY = None
    app.isGrading = False

    app.feedbackText = ""

    #HANDTRACKING VARIABLES    
    app.handTrackingMode = False
    app.cameraFrame = None
    app.lastFingerX = None
    app.lastFingerY = None
    app.fingerCooldown = 0

    #USERNAME VARIABLES 
    app.username = ""
    app.typing = False
    app.enteredUsername = False
    app.usernameBoxWidth = 300
    app.usernameBoxHeight = 40
    app.usernameBoxX = app.width // 2 - app.usernameBoxWidth // 2
    app.usernameBoxY = app.height // 2
    
    #CUSTOM COLORS
    app.lightPink = rgb(255, 233, 233)
    app.lightBrown = rgb(186, 170, 170)
    app.darkBrown = rgb(137, 118, 118)
    app.brown = rgb(89, 72, 72)
    app.redBrown = rgb(111, 61, 61)

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
        pressTryOnButton(app)
        pressStoreButton(app)
        pressX(app)
        sellClothes(app)
        
    elif app.state == "gradeMode":
        pressBackButton(app)
        pressX(app)

    if app.state == 'storeMode':
        pressBackButton(app)
        if app.storePage == "pickType":
            pressPickType(app, mouseX, mouseY)
        else:
            addToCloset(app, mouseX, mouseY)

    if app.state != "welcome":
        pressUniversalBackButton(app)
        pressX(app)

def onMouseMove(app, mouseX, mouseY):
    app.mouseX = mouseX
    app.mouseY = mouseY

        # Evaluate outfit
    if app.isSelectionMode:
        playButtonX = app.width / 2 - 50
        playButtonY = app.height - app.blackBarHeight - 60
        if playButtonX <= mouseX <= playButtonX + 100 and playButtonY <= mouseY <= playButtonY + 40:
            # topKey = app.topKeys[app.currTopIndex % len(app.topKeys)]
            # bottomKey = app.bottomKeys[app.currBottomIndex % len(app.bottomKeys)]
            topKey = app.topKeys[app.currTopIndex % len(app.topKeys)]
            bottomKey = app.bottomKeys[app.currBottomIndex % len(app.bottomKeys)]
            message, score = app.outfitManager.grade_outfit(topKey, bottomKey)
            app.feedbackText = f"{message} ({score}%)"

def onKeyPress(app, key):
    if app.state == "welcome":
        if key == "backspace":
            app.username = app.username[:-1]
        elif key == "enter" and app.username.strip() != "":
            app.hasEnteredUsername = True
        elif len(key) == 1 and len(app.username) < 20:
            app.username += key
    elif app.state == "instructions":
        if key == "up" and app.scrollY < app.maxScrollUp:
            app.scrollY += 20
        elif key == "down" and app.scrollY > -app.maxScrollDown:
            app.scrollY -= 20
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

def onStep(app):
    if app.handTrackingMode:
        # Update camera frame
        app.cameraFrame = processCameraFeed()
        finger = getFingerPosition()

        if finger is not None:
            fx, fy = finger
            # If previous finger position exists and cooldown has passed
            if app.lastFingerX is not None and app.fingerCooldown == 0:
                dx = fx - app.lastFingerX
                dy = fy - app.lastFingerY

                # Swipe horizontally → change top
                if abs(dx) > 0.07:
                    if dx > 0:
                        app.currTopIndex = (app.currTopIndex + 1) % len(app.tops)
                    else:
                        app.currTopIndex = (app.currTopIndex - 1) % len(app.tops)
                    app.fingerCooldown = 10

                # Swipe vertically → change bottom
                elif abs(dy) > 0.07:
                    if dy > 0:
                        app.currBottomIndex = (app.currBottomIndex + 1) % len(app.bottoms)
                    else:
                        app.currBottomIndex = (app.currBottomIndex - 1) % len(app.bottoms)
                    app.fingerCooldown = 10

            # Store current position
            app.lastFingerX, app.lastFingerY = fx, fy

        if app.fingerCooldown > 0:
            app.fingerCooldown -= 1

def redrawAll(app):
    if app.state == "welcome":
        drawWelcomeScreen(app)
    if app.storePage == 'sellTop' and app.isInstructing:
        drawGameMode(app)
        drawPopupMenu(app)
        drawSellTop(app)
    elif app.storePage == 'sellBottom' and app.isInstructing:
        drawGameMode(app)
        drawPopupMenu(app)
        drawSellBottom(app)
    elif app.state == "instructions":
        drawInstructionsScreen(app)
    elif app.state == "gameMode":
        drawGameMode(app)
    elif app.state == "storeMode":
        drawStoreMode(app)
    elif app.state == "gradeMode":
        drawGameScreen(app)
    elif app.state == 'storeMode':
        drawStoreMode(app)
    drawSoundButton(app)
   
    if app.state != "welcome" and app.state != "gradeMode":
        drawUniversalBackButton(app)
    
runApp(width=800, height=600)