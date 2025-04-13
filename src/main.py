from cmu_graphics import *
from ui import * 
from gameMode import drawGameMode
from clothesClasses import *
from outfitgrader import OutfitManager
import os
import random

def onAppStart(app):
    app.width = 800
    app.height = 600
    app.state = "welcome"

    app.isSelectionMode = True
    app.isDressingMode = False

    app.currTopIndex = 0
    app.currBottomIndex = 0
    app.tops = [Tops("images/shirt1.png"), Tops("images/shirt2.png"), Tops("images/shirt3.png"), Tops("images/shirt4.png"), Tops("images/shirt5.png"), Tops("images/shirt6.png")]
    app.bottoms = [Bottoms("images/skirt1.png"), Bottoms("images/skirt2.png"), Bottoms("images/skirt3.png"), Bottoms("images/bottom1.png"), Bottoms("images/bottom2.png"), Bottoms("images/bottom3.png")]
    
    app.modeButtonWidth, app.modeButtonHeight = 160, 80

    app.blackBarHeight = 50

    app.whiteBoxWidth = app.width/3
    app.whiteBoxHeight = app.height - 2*app.blackBarHeight
    app.whiteBoxX = app.width/3

    app.backwardButtonX = app.width - app.whiteBoxWidth - app.forwardButtonWidth - 2*app.buttonAllowance - 35
    app.buttonAllowance = 10

    app.forwardButtonWidth = app.whiteBoxWidth*0.33
    app.forwardButtonHeight = app.blackBarHeight - app.blackBarHeight*0.2
    app.forwardButtonX = app.whiteBoxWidth+app.buttonAllowance
    app.forwardButtonY = ((app.height/2) - app.blackBarHeight +
                      (app.blackBarHeight-app.forwardButtonHeight)/2)

    app.playButtonWidth = app.forwardButtonWidth*0.66
    app.playButtonHeight = app.forwardButtonHeight
    app.playButtonX = app.width/2 - app.playButtonWidth/2
    app.playButtonY = app.forwardButtonY
    # Initialize managers
    # app.hangerManager = HangerManager(app)
    # app.outfitManager = OutfitManager(app)

    app.gradeButtonX = app.width/2 - 50
    app.gradeButtonY = app.height - app.blackBarHeight - 60
    app.gradeButtonWidth = 100
    app.gradeButtonHeight = 40
    app.backButtonX = app.width/2 - 60
    app.backButtonY = app.height - 60
    app.backButtonWidth = 120
    app.backButtonHeight = 40
    
    
    app.backgroundImage = "images/kingclosetbackgrounds.png"
    app.buttonWidth = 310
    app.buttonHeight = 80
    app.buttonX = app.width // 2 - app.buttonWidth // 2
    app.buttonY = app.height // 2 + 45

    app.scrollY = 0
    app.maxScrollUp = 0
    app.maxScrollDown = 200

    app.instructionsBackgroundImage = "images/instructions.png"
    app.instructionsButtonWidth = 250
    app.instructionsButtonHeight = 60
    app.instructionsButtonX = app.width // 2 - app.instructionsButtonWidth // 2
    app.instructionsButtonY = app.height - 120
    app.instructionsButtonText = "Start Styling"    
    
    app.sound = Sound('kidsInAmerica.mp3')
    app.soundIsPlaying = False
    app.soundButtonX = app.width - 40
    app.soundButtonY = 10
    app.soundButtonSize = 30
    
    app.instructionsButtonText = "Start Styling"

    app.outfitManager = OutfitManager(app)
    app.topKeys = list(app.outfitManager.tops.keys())
    app.bottomKeys = list(app.outfitManager.bottoms.keys())

    app.mouseX = None
    app.mouseY = None

def onMousePress(app, mouseX, mouseY):
    if app.state == "welcome":
        if (app.buttonX <= mouseX <= app.buttonX + app.buttonWidth and
                app.buttonY <= mouseY <= app.buttonY + app.buttonHeight):
            app.state = "instructions"

    elif app.state == "instructions":
        if (app.instructionsButtonX <= mouseX <= app.instructionsButtonX + app.instructionsButtonWidth and
                app.instructionsButtonY <= mouseY <= app.instructionsButtonY + app.instructionsButtonHeight):
            app.state = "gameMode"

    elif app.state == 'gameMode':
        # Mode selection buttons
        if ((2 * (app.width / 3) <= mouseX <= 2 * (app.width / 3) + app.modeButtonWidth) and
                (app.height - app.blackBarHeight - app.modeButtonHeight <= mouseY <= app.height - app.blackBarHeight)):
            app.isDressingMode = True
            app.isSelectionMode = False

        if ((app.whiteBoxWidth - app.modeButtonWidth <= mouseX <= app.whiteBoxWidth) and
                (app.height - app.blackBarHeight - app.modeButtonHeight <= mouseY <= app.height - app.blackBarHeight)):
            app.isDressingMode = False
            app.isSelectionMode = True
        
        #tops forward button press
        if (((app.backwardButtonX <= app.mouseX) and 
             (app.mouseX <= (app.backwardButtonX+
                         app.forwardButtonWidth))) and
            ((app.forwardButtonY <= app.mouseY) and 
             (app.mouseY <= app.forwardButtonY + app.forwardButtonHeight))):
        
            app.currTopIndex+=1
            app.currTopIndex %= len(app.tops)

        #tops backward button press
        if (((app.forwardButtonX <= app.mouseX) and 
            (app.mouseX <= app.forwardButtonX + app.forwardButtonWidth)) and
            ((app.forwardButtonY <= app.mouseY) and 
            (app.mouseY <= app.forwardButtonY + app.forwardButtonHeight))):

            app.currTopIndex-=1
            app.currTopIndex %= len(app.tops)

        #tops play button press
        if (((app.playButtonX <= app.mouseX) and 
            (app.mouseX <= app.playButtonX + app.playButtonWidth)) and
            ((app.playButtonY <= app.mouseY) and 
            (app.mouseY <= app.playButtonY + app.playButtonHeight))):

            pass

        #bottoms forward button press
        if (((app.backwardButtonX <= app.mouseX) and 
            (app.mouseX <= (app.backwardButtonX +
                         app.forwardButtonWidth))) and
            ((app.forwardButtonY+app.whiteBoxHeight/2<= app.mouseY) and 
            (app.mouseY <= app.forwardButtonY+app.whiteBoxHeight/2 + app.forwardButtonHeight))):

            app.currBottomIndex+=1
            app.currBottomIndex%=len(app.bottoms)

        #bottoms backward button press
        if (((app.forwardButtonX <= app.mouseX) and 
            (app.mouseX <= app.forwardButtonX + app.forwardButtonWidth)) and
            ((app.forwardButtonY+app.whiteBoxHeight/2 <= app.mouseY) and 
            (app.mouseY <= app.forwardButtonY+app.whiteBoxHeight/2 + app.forwardButtonHeight))):

            app.currBottomIndex-=1
            app.currBottomIndex%=len(app.bottoms)

        #bottoms play button press
        if (((app.playButtonX <= app.mouseX) and 
            (app.mouseX <= app.playButtonX + app.playButtonWidth)) and
            ((app.playButtonY+app.whiteBoxHeight/2 <= app.mouseY) and 
            (app.mouseY <= app.playButtonY+app.playButtonHeight+app.whiteBoxHeight/2))):

            pass

        if ((app.gradeButtonX <= mouseX <= app.gradeButtonX + app.gradeButtonWidth) and
            (app.gradeButtonY <= mouseY <= app.gradeButtonY + app.gradeButtonHeight)):

            topKey = app.topKeys[app.currTopIndex % len(app.topKeys)]
            bottomKey = app.bottomKeys[app.currBottomIndex % len(app.bottomKeys)]
            
            message, rating, score = app.outfitManager.gradeOutfit(topKey, bottomKey)
            
            app.feedbackText = f"{message} ({score}%)"
            app.outfitRating = rating
            app.outfitScore = score

            app.state = "gradeMode"
    
    if app.state == "gradeMode":
        if ((app.backButtonX <= mouseX <= app.backButtonX + app.backButtonWidth) and
            (app.backButtonY <= mouseY <= app.backButtonY + app.backButtonHeight)):
            app.state = "gameMode"


    if (app.soundButtonX <= mouseX <= app.soundButtonX + app.soundButtonSize and
            app.soundButtonY <= mouseY <= app.soundButtonY + app.soundButtonSize):
        if app.soundIsPlaying:
            app.sound.pause()
            app.soundIsPlaying = False
        else:
            app.sound.play(restart=False)
            app.soundIsPlaying = True

    if (app.playButtonX <= mouseX <= app.playButtonX + app.playButtonWidth and
        app.playButtonY <= mouseY <= app.playButtonY + app.playButtonHeight):
        app.currTopIndex = random.randint(0, len(app.tops) - 1)

    elif (app.playButtonX <= mouseX <= app.playButtonX + app.playButtonWidth and
          app.playButtonY + 
          app.whiteBoxHeight / 2 <= mouseY <= app.playButtonY + 
          app.whiteBoxHeight / 2 + app.playButtonHeight):
        app.currBottomIndex = random.randint(0, len(app.bottoms) - 1)
    
    
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
    drawRect(app.width/2 - 50, app.height - app.blackBarHeight - 60, 100, 40, fill='plum', border='black')
    drawLabel("Grade", app.width/2, app.height - app.blackBarHeight - 40, size=18, bold=True)


runApp()