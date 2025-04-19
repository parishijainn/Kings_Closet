from cmu_graphics import *
import random
from virtualtryon import tryOnCamera

def drawSoundButton(app):
    drawRect(app.soundButtonX, app.soundButtonY, app.soundButtonSize, app.soundButtonSize,
             fill='white', border='gray', borderWidth=1)

    centerX = app.soundButtonX + app.soundButtonSize // 2
    centerY = app.soundButtonY + app.soundButtonSize // 2

    if app.soundIsPlaying:
        barWidth = 5
        barHeight = 15
        spacing = 5
        drawRect(centerX - spacing - barWidth, centerY - barHeight // 2,
                 barWidth, barHeight, fill='pink')
        drawRect(centerX + spacing, centerY - barHeight // 2,
                 barWidth, barHeight, fill='pink')
    else:
        drawPolygon(centerX - 5, centerY - 10,
                    centerX - 5, centerY + 10,
                    centerX + 10, centerY,
                    fill='pink')      
def pressSoundButton(app):
     if (app.soundButtonX <= app.mouseX <= app.soundButtonX + app.soundButtonSize and
            app.soundButtonY <= app.mouseY <= app.soundButtonY + app.soundButtonSize):
        if app.soundIsPlaying:
            app.sound.pause()
            app.soundIsPlaying = False
        else:
            app.sound.play(restart=False)
            app.soundIsPlaying = True

#WELCOMEMODE
def drawStartPlayingButton(app):
     pass
def pressStartPlayingButton(app):
     if (app.buttonX <= app.mouseX <= app.buttonX + app.buttonWidth and
                app.buttonY <= app.mouseY <= app.buttonY + app.buttonHeight):
            app.state = "instructions"
     
#INSTRUCTIONSMODE
def drawStartStylingButton(app):
     pass
def pressStartStylingButton(app):
     if (app.instructionsButtonX <= app.mouseX <= app.instructionsButtonX + app.instructionsButtonWidth and
                app.instructionsButtonY <= app.mouseY <= app.instructionsButtonY + app.instructionsButtonHeight):
            app.state = "gameMode"
     
#GAMEMODE
def drawModeButtons(app):
    drawRect(2*(app.width/3), 
             app.height-app.blackBarHeight-app.modeButtonHeight, 
             app.modeButtonWidth, app.modeButtonHeight, fill='gray')
    drawLabel('Dress Me', 2 * (app.width / 3) + app.modeButtonWidth / 2, 
          app.height - app.blackBarHeight - app.modeButtonHeight / 2, 
          size=30, fill='white', bold=True, font = 'monospace')
    drawRect((app.width/3)-app.modeButtonWidth, 
             app.height-app.blackBarHeight-app.modeButtonHeight, 
             app.modeButtonWidth, app.modeButtonHeight, fill='gray')
    drawLabel('Browse', (app.width / 3) - app.modeButtonWidth / 2, 
          app.height - app.blackBarHeight - app.modeButtonHeight / 2, 
          size=30, fill='white', bold=True, font = 'monospace')
def pressModeButtons(app):
    if ((2*(app.width/3) <= app.mouseX <= 2*(app.width/3) + app.modeButtonWidth) and
        (app.height-app.blackBarHeight-app.modeButtonHeight <= app.mouseY <= app.height-app.blackBarHeight)):
            app.isDressingMode = True
            app.isSelectionMode = False

    if ((app.whiteBoxWidth-app.modeButtonWidth <= app.mouseX <= app.whiteBoxWidth) and
        (app.height-app.blackBarHeight-app.modeButtonHeight <= app.mouseY <= app.height-app.blackBarHeight)):
            app.isDressingMode = False
            app.isSelectionMode = True

def drawGradeButton(app):
    drawRect(app.gradeButtonX, app.gradeButtonY, app.gradeButtonWidth, app.gradeButtonHeight, fill='plum', border='black')
    drawLabel("Grade", app.gradeButtonX + 25, app.gradeButtonY +20,
              size=18, bold=True, align='left')
def pressGradeButton(app):
    if (app.gradeButtonX <= app.mouseX <= (app.gradeButtonX + 
                                            app.gradeButtonWidth) and
        app.gradeButtonY <= app.mouseY <= (app.gradeButtonY +
                                            app.gradeButtonHeight)):
        topKey = app.topKeys[app.currTopIndex % len(app.topKeys)]
        bottomKey = app.bottomKeys[app.currBottomIndex % len(app.bottomKeys)]
        message, rating, score = app.outfitManager.gradeOutfit(topKey, bottomKey)
        app.feedbackText = f"{message} ({score}%)"
        app.outfitRating = rating
        app.outfitScore = score
        app.isGrading = True
                
        app.state = "gradeMode"
        
def drawImportButton(app):
    drawRect(app.importButtonX, app.importButtonY, app.importButtonWidth, 
             app.importButtonHeight, fill='lavenderBlush', border='maroon')
    drawLabel("Import Clothes", app.importButtonX + app.importButtonWidth//2,
              app.importButtonY + app.importButtonHeight//2, size=15, bold=True)
def pressImportButton(app):
    if (app.importButtonX <= app.mouseX <= (app.importButtonX + 
                                            app.importButtonWidth) and
        app.importButtonY <= app.mouseY <= (app.importButtonY +
                                            app.importButtonHeight)):
        #app.state = "importMode"
        pass
    
def drawTryOnButton(app):
    drawRect(app.tryOnButtonX, app.tryOnButtonY, app.tryOnButtonWidth, 
             app.tryOnButtonHeight, fill='lavenderBlush', border='maroon')
    drawLabel("Try On", app.tryOnButtonX + app.tryOnButtonWidth//2,
              app.tryOnButtonY + app.tryOnButtonHeight//2, size=15, bold=True)

def pressTryOnButton(app):
     if (app.tryOnButtonX <= app.mouseX <= (app.tryOnButtonX + 
                                            app.tryOnButtonWidth) and
        app.tryOnButtonY <= app.mouseY <= (app.tryOnButtonY +
                                            app.tryOnButtonHeight)):
        tryOnCamera()

def drawSelectionButtons(app):
        drawRect(app.playButtonX, app.playButtonY, app.playButtonWidth,
                app.playButtonHeight, fill='gray')
        drawRect(app.playButtonX, app.playButtonY + app.whiteBoxHeight / 2,
                app.playButtonWidth, app.playButtonHeight, fill='gray')
        drawRect(app.forwardButtonX, app.backwardButtonY,  # Swapped X coordinates for backwardButton
                app.backwardButtonWidth, app.backwardButtonHeight, fill='gray')
        drawRect(app.forwardButtonX, app.backwardButtonY + app.whiteBoxHeight / 2,
                app.backwardButtonWidth, app.backwardButtonHeight, fill='gray')
        drawRect(app.backwardButtonX, app.backwardButtonY,  # Swapped X coordinates for forwardButton
                app.backwardButtonWidth, app.backwardButtonHeight, fill='gray')
        drawRect(app.backwardButtonX, app.backwardButtonY + app.whiteBoxHeight / 2,
                app.backwardButtonWidth, app.backwardButtonHeight, fill='gray')
        #top buttons
        drawPolygon(app.forwardButtonX + 20, app.backwardButtonY + 10,
                    app.forwardButtonX + 20, app.backwardButtonY + app.backwardButtonHeight - 10,
                    app.forwardButtonX + 35, app.backwardButtonY + app.backwardButtonHeight / 2,
                    fill='white')
        drawPolygon(app.forwardButtonX + 40, app.backwardButtonY + 10,
                    app.forwardButtonX + 40, app.backwardButtonY + app.backwardButtonHeight - 10,
                    app.forwardButtonX + 55, app.backwardButtonY + app.backwardButtonHeight / 2,
                    fill='white')
        drawPolygon(app.playButtonX + 20, app.playButtonY + 10,
                    app.playButtonX + 20, app.playButtonY + app.playButtonHeight - 10,
                    app.playButtonX + app.playButtonWidth - 20, app.playButtonY + app.playButtonHeight / 2,
                    fill='white')
        drawPolygon(app.backwardButtonX + app.backwardButtonWidth - 20, app.backwardButtonY + 10,
                    app.backwardButtonX + app.backwardButtonWidth - 20, app.backwardButtonY + app.backwardButtonHeight - 10,
                    app.backwardButtonX + app.backwardButtonWidth - 35, app.backwardButtonY + app.backwardButtonHeight / 2,
                    fill='white')
        drawPolygon(app.backwardButtonX + app.backwardButtonWidth - 40, app.backwardButtonY + 10,
                    app.backwardButtonX + app.backwardButtonWidth - 40, app.backwardButtonY + app.backwardButtonHeight - 10,
                    app.backwardButtonX + app.backwardButtonWidth - 55, app.backwardButtonY + app.backwardButtonHeight / 2,
                    fill='white')
        #bottom buttons
        drawPolygon(app.forwardButtonX + 20, app.backwardButtonY + app.whiteBoxHeight / 2 + 10,
                    app.forwardButtonX + 20, app.backwardButtonY + app.whiteBoxHeight / 2 + app.backwardButtonHeight - 10,
                    app.forwardButtonX + 35, app.backwardButtonY + app.whiteBoxHeight / 2 + app.backwardButtonHeight / 2,
                    fill='white')
        drawPolygon(app.forwardButtonX + 40, app.backwardButtonY + app.whiteBoxHeight / 2 + 10,
                    app.forwardButtonX + 40, app.backwardButtonY + app.whiteBoxHeight / 2 + app.backwardButtonHeight - 10,
                    app.forwardButtonX + 55, app.backwardButtonY + app.whiteBoxHeight / 2 + app.backwardButtonHeight / 2,
                    fill='white')
        drawPolygon(app.playButtonX + 20, app.playButtonY + app.whiteBoxHeight / 2 + 10,
                    app.playButtonX + 20, app.playButtonY + app.whiteBoxHeight / 2 + app.playButtonHeight - 10,
                    app.playButtonX + app.playButtonWidth - 20, app.playButtonY + app.whiteBoxHeight / 2 + app.playButtonHeight / 2,
                    fill='white')
        drawPolygon(app.backwardButtonX + app.backwardButtonWidth - 20, app.backwardButtonY + app.whiteBoxHeight / 2 + 10,
                    app.backwardButtonX + app.backwardButtonWidth - 20, app.backwardButtonY + app.whiteBoxHeight / 2 + app.backwardButtonHeight - 10,
                    app.backwardButtonX + app.backwardButtonWidth - 35, app.backwardButtonY + app.whiteBoxHeight / 2 + app.backwardButtonHeight / 2,
                    fill='white')
        drawPolygon(app.backwardButtonX + app.backwardButtonWidth - 40, app.backwardButtonY + app.whiteBoxHeight / 2 + 10,
                    app.backwardButtonX + app.backwardButtonWidth - 40, app.backwardButtonY + app.whiteBoxHeight / 2 + app.backwardButtonHeight - 10,
                    app.backwardButtonX + app.backwardButtonWidth - 55, app.backwardButtonY + app.whiteBoxHeight / 2 + app.backwardButtonHeight / 2,
                    fill='white')
def pressSelectionButtons(app):
    #tops forward button press
    if (((app.forwardButtonX <= app.mouseX) and 
         (app.mouseX <= (app.forwardButtonX+
                         app.backwardButtonWidth))) and
        ((app.backwardButtonY <= app.mouseY) and 
         (app.mouseY <= app.backwardButtonY + app.backwardButtonHeight))):
        app.currTopIndex+=1
        app.currTopIndex %= len(app.tops)
    #tops backward button press
    if (((app.backwardButtonX <= app.mouseX) and 
         (app.mouseX <= app.backwardButtonX + app.backwardButtonWidth)) and
        ((app.backwardButtonY <= app.mouseY) and 
         (app.mouseY <= app.backwardButtonY + app.backwardButtonHeight))):
        app.currTopIndex-=1
        app.currTopIndex %= len(app.tops)
    #bottoms forward button press
    if (((app.forwardButtonX <= app.mouseX) and 
         (app.mouseX <= (app.forwardButtonX +
                         app.backwardButtonWidth))) and
        ((app.backwardButtonY+app.whiteBoxHeight/2<= app.mouseY) and 
         (app.mouseY <= app.backwardButtonY+app.whiteBoxHeight/2 + app.backwardButtonHeight))):
        app.currBottomIndex+=1
        app.currBottomIndex%=len(app.bottoms)
    #bottoms backward button press
    if (((app.backwardButtonX <= app.mouseX) and 
         (app.mouseX <= app.backwardButtonX + app.backwardButtonWidth)) and
        ((app.backwardButtonY+app.whiteBoxHeight/2 <= app.mouseY) and 
         (app.mouseY <= app.backwardButtonY+app.whiteBoxHeight/2 + app.backwardButtonHeight))):
        app.currBottomIndex-=1
        app.currBottomIndex%=len(app.bottoms)
    #tops play button press
    if (app.playButtonX <= app.mouseX <= app.playButtonX + app.playButtonWidth and
        app.playButtonY <= app.mouseY <= app.playButtonY + app.playButtonHeight):
        app.currTopIndex = random.randint(0, len(app.tops) - 1)
    #bottoms play button press
    if (app.playButtonX <= app.mouseX <= app.playButtonX + app.playButtonWidth and
        app.playButtonY + app.whiteBoxHeight / 2 <= app.mouseY <= app.playButtonY + 
        app.whiteBoxHeight / 2 + app.playButtonHeight):
        app.currBottomIndex = random.randint(0, len(app.bottoms) - 1)

#GRADEMODE
def drawBackButton(app):
    drawRect(app.width//2 - 60, app.height - 60, 120, 40, fill='plum', border='black')
    drawLabel("Back", app.width//2, app.height - 40, size=18, bold=True)
def pressBackButton(app):
     if ((app.backButtonX <= app.mouseX <= app.backButtonX + app.backButtonWidth) and
            (app.backButtonY <= app.mouseY <= app.backButtonY + app.backButtonHeight)):
            app.state = "gameMode"
            app.feedbackText = ""
            app.isGrading = False 
#backbutton for each page
def drawUniversalBackButton(app):
    drawRect(app.universalBackButtonX, app.universalBackButtonY,
             app.universalBackButtonWidth, app.universalBackButtonHeight,
             fill='lavenderBlush', border='maroon', borderWidth=2)
    
    drawLabel("←", app.universalBackButtonX + app.universalBackButtonWidth // 2,
              app.universalBackButtonY + app.universalBackButtonHeight // 2,
              size=20, bold=True, fill='maroon')

    
def pressUniversalBackButton(app):
    if (app.universalBackButtonX <= app.mouseX <= app.universalBackButtonX + app.universalBackButtonWidth and
        app.universalBackButtonY <= app.mouseY <= app.universalBackButtonY + app.universalBackButtonHeight):
    #go back to previous page
        if app.state == "instructions":
            app.state = "welcome"
        elif app.state == "gameMode":
            app.state = "instructions"
        elif app.state == "gradeMode":
            app.state = "gameMode"
            app.feedbackText = ""
            app.isGrading = False