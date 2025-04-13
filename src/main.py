from cmu_graphics import *
from ui import * 
from gameMode import drawGameMode
from clothesClasses import *
from outfitgrader import OutfitManager
import os

def onAppStart(app):
    app.width = 800
    app.height = 600
    app.state = "welcome"

    app.isSelectionMode = True
    app.isDressingMode = False

    app.currTopIndex = 0
    app.currBottomIndex = 0
    app.feedbackText = ""

    app.tops = [Tops("images/shirt1.png"), Tops("images/shirt2.png"), Tops("images/shirt3.png"),
                Tops("images/shirt4.png"), Tops("images/shirt5.png"), Tops("images/shirt6.png")]
    app.bottoms = [Bottoms("images/skirt1.png"), Bottoms("images/skirt2.png"), Bottoms("images/skirt3.png"),
                   Bottoms("images/bottom1.png"), Bottoms("images/bottom2.png"), Bottoms("images/bottom3.png")]

    app.modeButtonWidth, app.modeButtonHeight = 160, 80

    app.blackBarHeight = 50
    app.whiteBoxWidth = app.width / 3
    app.whiteBoxHeight = app.height - 2 * app.blackBarHeight
    app.whiteBoxX = app.width / 3
    app.buttonAllowance = 10

    app.forwardButtonWidth = app.whiteBoxWidth * 0.33
    app.forwardButtonHeight = app.blackBarHeight - app.blackBarHeight * 0.2
    app.forwardButtonX = app.width/3 + app.buttonAllowance
    app.forwardButtonY = (app.height / 2 - app.blackBarHeight +
                          (app.blackBarHeight - app.forwardButtonHeight) / 2)
    app.backwardButtonX = app.width - app.whiteBoxWidth - app.forwardButtonWidth - 2 * app.buttonAllowance

    app.playButtonWidth = app.forwardButtonWidth * 0.66
    app.playButtonHeight = app.forwardButtonHeight
    app.playButtonX = app.width / 2 - app.playButtonWidth / 2
    app.playButtonY = app.forwardButtonY

    app.gradeButtonWidth = 140
    app.gradeButtonHeight = 40
    app.gradeButtonX = app.width // 2 - app.gradeButtonWidth // 2
    app.gradeButtonY = app.height - app.blackBarHeight - app.gradeButtonHeight - 10

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
        if ((2 * (app.width / 3) <= mouseX <= 2 * (app.width / 3) + app.modeButtonWidth) and
                (app.height - app.blackBarHeight - app.modeButtonHeight <= mouseY <= app.height - app.blackBarHeight)):
            app.isDressingMode = True
            app.isSelectionMode = False

        if ((app.width - app.modeButtonWidth <= mouseX <= app.width) and
                (app.height - app.blackBarHeight - app.modeButtonHeight <= mouseY <= app.height - app.blackBarHeight)):
            app.isDressingMode = False
            app.isSelectionMode = True

        gradeButtonX = app.width/2 - 60
        gradeButtonY = app.height - app.blackBarHeight - 100
        if app.isSelectionMode and (gradeButtonX <= mouseX <= gradeButtonX + 120 and gradeButtonY <= mouseY <= gradeButtonY + 40):
            topKey = app.topKeys[app.currTopIndex % len(app.topKeys)]
            bottomKey = app.bottomKeys[app.currBottomIndex % len(app.bottomKeys)]
            message, rating, score = app.outfitManager.grade_outfit(topKey, bottomKey)
            app.feedbackText = f"{message} ({score}%)"
            app.state = "gradeMode"

def onKeyPress(app, key):
    if app.state == "instructions":
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
    
    # Inside the gameMode mouse press logic
    if app.isSelectionMode and (gradeButtonX <= mouseX <= gradeButtonX + 120 and gradeButtonY <= mouseY <= gradeButtonY + 40):
        topKey = app.topKeys[app.currTopIndex % len(app.topKeys)]
        bottomKey = app.bottomKeys[app.currBottomIndex % len(app.bottomKeys)]
        message, rating, score = app.outfitManager.grade_outfit(topKey, bottomKey)
        app.feedbackText = f"{message} ({score}%)"
        app.state = "gradeMode"
    
    elif app.state == 'gradeMode':
        if app.width/2 - 60 <= mouseX <= app.width/2 + 60 and app.height - 60 <= mouseY <= app.height - 20:
            app.state = "gameMode"




def onMouseMove(app, mouseX, mouseY):
    app.mouseX = mouseX
    app.mouseY = mouseY

def drawGradeScreen(app):
    drawRect(0, 0, app.width, app.height, fill='lightyellow')
    drawLabel("King's Closet: Outfit Grade", app.width // 2, 30, size=28, bold=True)

    topImg = app.outfitManager.tops[app.topKeys[app.currTopIndex % len(app.topKeys)]]
    bottomImg = app.outfitManager.bottoms[app.bottomKeys[app.currBottomIndex % len(app.bottomKeys)]]

    drawImage(topImg, app.width//2, 140, width=180, height=180, align='center')
    drawImage(bottomImg, app.width//2, 320, width=180, height=180, align='center')

    drawLabel(app.feedbackText, app.width//2, app.height - 100, size=22, fill='darkmagenta')

def redrawAll(app):
    if app.state == "welcome":
        drawWelcomeScreen(app)
    elif app.state == "instructions":
        drawInstructionsScreen(app)
    elif app.state == "gameMode":
        drawGameMode(app)
    elif app.state == "gradeMode":
        drawGradeScreen(app)

runApp()
