from cmu_graphics import *
import random
from virtualtryon import tryOnCamera
import math
#POPUP MENU
def drawPopupMenu(app):
    if app.isInstructing:
        drawRect(app.popupX, app.popupY, app.popupWidth, app.popupHeight,
                fill='white', border='black',align='center')
        drawRect(app.popupX, app.popupY-app.popupHeight/2 + 13, app.popupWidth, 30, fill='lightpink', align='center', border='black')
        drawCircle(app.popupX-app.popupWidth/2+15, app.popupY-app.popupHeight/2+13, 10, fill='red')
        drawLabel("X", app.popupX-app.popupWidth/2+15, app.popupY-app.popupHeight/2+13, size=15, fill='white')
        if app.handTrackingMode:
            drawLabel("handTrackingMode instructions", app.popupX, app.popupY+60, size=20)
        elif app.state == "gameMode":
            drawLabel("gameMode instructions", app.popupX, app.popupY, size=20)
        elif app.state == 'storeMode':
            drawLabel("storeMode instructions", app.popupX, app.popupY, size=20)
        elif app.state == 'tryOnMode':
            drawLabel("tryOnMode instructions", app.popupX, app.popupY, size=20)     
def pressX(app):
    if (app.popupX-app.popupWidth/2+5 <= app.mouseX <= app.popupX-app.popupWidth/2+25 and
        app.popupY-app.popupHeight/2+3 <= app.mouseY <= app.popupY-app.popupHeight/2+23):
        app.isInstructing = False

def drawCategoryButtons(app):
    drawRect(app.topButtonX, app.topButtonY, 150, 100, fill="lightblue")
    drawLabel("Top", app.topButtonX, app.topButtonY, size=20,)
    drawRect(app.bottomButtonX, app.bottomButtonY, 150, 100, fill="lightblue")
    drawLabel("Bottom", app.bottomButtonX, app.bottomButtonY, size=20,)

def pressCategoryButtons(app):
    if (app.topButtonX <= app.mouseX <= app.topButtonX+150 and 
        app.topButtonY <= app.mouseY <= app.topButtonY+100):
        app.category = "top"
    if (app.bottomButtonX <= app.mouseX <= app.bottomButtonX+150 and 
         app.bottomButtonY <= app.mouseY <= app.bottomButtonY+100):
        app.category = "bottom"
        
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
# def drawModeButtons(app):
#     # Dress Me Button
#     drawRect(2*(app.width/3), 
#              app.height-app.blackBarHeight-app.modeButtonHeight, 
#              app.modeButtonWidth, app.modeButtonHeight, fill='gray')
#     drawLabel('Dress Me', 2 * (app.width / 3) + app.modeButtonWidth / 2, 
#           app.height - app.blackBarHeight - app.modeButtonHeight / 2, 
#           size=30, fill='white', bold=True, font = 'monospace')
    
#     # Browse Button
#     drawRect((app.width/3)-app.modeButtonWidth, 
#              app.height-app.blackBarHeight-app.modeButtonHeight, 
#              app.modeButtonWidth, app.modeButtonHeight, fill='gray')
#     drawLabel('Browse', (app.width / 3) - app.modeButtonWidth / 2, 
#           app.height - app.blackBarHeight - app.modeButtonHeight / 2, 
#           size=30, fill='white', bold=True, font = 'monospace')
    
    
#     handtrackX = 410
#     handtrackY = 5
#     handtrackW = 130
#     handtrackH = app.blackBarHeight - 10
#     drawRect(handtrackX, handtrackY, handtrackW, handtrackH,
#              fill=app.lightPink, border='black')
#     drawLabel(f"HandTrack: {'ON' if app.handTrackingMode else 'OFF'}", 
#               handtrackX + handtrackW/2, handtrackY + handtrackH/2,
#               size=15, bold=True, fill=app.darkBrown, align='center')

import math

def drawModeButtons(app):
    # Coordinates for the buttons
    buttonWidth = app.modeButtonWidth
    buttonHeight = app.modeButtonHeight * 1.5  
    buttonXDressMe = 2 * (app.width / 3)  
    buttonXBrowse = (app.width / 3) - app.modeButtonWidth * 1.5  
    buttonY = app.height / 2 - app.modeButtonHeight / 2 + 50  

    dressMePoints = []
    for i in range(6):
        angle = math.radians(60 * i)
        x = buttonXDressMe + buttonWidth / 2 + (buttonWidth / 2) * math.cos(angle)
        y = buttonY + buttonHeight / 2 + (buttonHeight / 2) * math.sin(angle)
        dressMePoints.append(x)
        dressMePoints.append(y)

    # Check if hovering over Dress Me button
    if (buttonXDressMe <= app.mouseX <= buttonXDressMe + buttonWidth and
        buttonY <= app.mouseY <= buttonY + buttonHeight):
        borderColor = 'blue'
        borderWidth = 3
    else:
        borderColor = 'black'
        borderWidth = 1

    drawPolygon(*dressMePoints, fill=app.brown, border=borderColor, borderWidth=borderWidth)
    drawLabel('Dress Me', buttonXDressMe + buttonWidth / 2, 
              buttonY + buttonHeight / 2, size=30, fill='white', bold=True)

    # Define points for the Browse button (hexagon shape)
    browsePoints = []
    for i in range(6):
        angle = math.radians(60 * i)
        x = buttonXBrowse + buttonWidth / 2 + (buttonWidth / 2) * math.cos(angle)
        y = buttonY + buttonHeight / 2 + (buttonHeight / 2) * math.sin(angle)
        browsePoints.append(x)
        browsePoints.append(y)

    # Check if hovering over Browse button
    if (buttonXBrowse <= app.mouseX <= buttonXBrowse + buttonWidth and
        buttonY <= app.mouseY <= buttonY + buttonHeight):
        borderColor = 'blue'
        borderWidth = 3
    else:
        borderColor = 'black'
        borderWidth = 1

    drawPolygon(*browsePoints, fill=app.brown, border=borderColor, borderWidth=borderWidth)
    drawLabel('Browse', buttonXBrowse + buttonWidth / 2, 
              buttonY + buttonHeight / 2, size=30, fill='white', bold=True)

    centerX = app.width / 2  
    centerY = buttonY - 100 

    radius = 50
    angleStep = 360 / 6  # 360 degrees divided by 6 sides
    points = []

    # Generate the points for the hexagon
    for i in range(6):
        angle = angleStep * i
        x = centerX + radius * math.cos(math.radians(angle))
        y = centerY + radius * math.sin(math.radians(angle))
        points.append(x)
        points.append(y)

    # Handtracking display
    handtrackX = 410
    handtrackY = 5
    handtrackW = 130
    handtrackH = app.blackBarHeight - 10
    drawRect(handtrackX, handtrackY, handtrackW, handtrackH,
             fill=app.lightPink, border='black')
    drawLabel(f"HandTrack: {'ON' if app.handTrackingMode else 'OFF'}", 
              handtrackX + handtrackW/2, handtrackY + handtrackH/2,
              size=15, bold=True, fill=app.darkBrown, align='center')

def pressModeButtons(app):
    if ((2*(app.width/3) <= app.mouseX <= 2*(app.width/3) + app.modeButtonWidth) and
        (app.height-app.blackBarHeight-app.modeButtonHeight <= app.mouseY <= app.height-app.blackBarHeight)):
            app.isDressingMode = True
            app.isSelectionMode = False

    if ((app.whiteBoxWidth-app.modeButtonWidth <= app.mouseX <= app.whiteBoxWidth) and
        (app.height-app.blackBarHeight-app.modeButtonHeight <= app.mouseY <= app.height-app.blackBarHeight)):
            app.isDressingMode = False
            app.isSelectionMode = True
    
    if (410 <= app.mouseX <= 540 and 5 <= app.mouseY <= 5 + app.blackBarHeight - 10):
        app.handTrackingMode = not app.handTrackingMode
        if app.handTrackingMode:
            app.isInstructing = True

def drawGradeButton(app):
    drawRect(app.gradeButtonX, app.gradeButtonY, app.gradeButtonWidth, app.gradeButtonHeight, fill=app.lightPink, border='black')
    drawLabel("Grade", app.gradeButtonX + 25, app.gradeButtonY +20,
              size=15, fill=app.darkBrown, bold=True, align='left')

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
             app.importButtonHeight, fill=app.lightPink, border='black')
    drawLabel("Import Clothes", app.importButtonX + app.importButtonWidth//2,
              app.importButtonY + app.importButtonHeight//2, size=15, bold=True, fill=app.darkBrown)
    
def pressImportButton(app):
    if (app.importButtonX <= app.mouseX <= (app.importButtonX + 
                                            app.importButtonWidth) and
        app.importButtonY <= app.mouseY <= (app.importButtonY +
                                            app.importButtonHeight)):
        app.state = "importMode"
        app.isInstructing = True
        
   
def drawTryOnButton(app):
    drawRect(app.tryOnButtonX, app.tryOnButtonY, app.tryOnButtonWidth, 
             app.tryOnButtonHeight, fill=app.lightPink, border='black')
    drawLabel("Try On", app.tryOnButtonX + app.tryOnButtonWidth//2,
              app.tryOnButtonY + app.tryOnButtonHeight//2, size=15, bold=True, fill=app.darkBrown)

def pressTryOnButton(app):
     if (app.tryOnButtonX <= app.mouseX <= (app.tryOnButtonX + 
                                            app.tryOnButtonWidth) and
        app.tryOnButtonY <= app.mouseY <= (app.tryOnButtonY +
                                            app.tryOnButtonHeight)):
        tryOnCamera()
        app.state = "tryOnMode"
        app.isInstructing = True

def drawSelectionButtons(app):
    if not app.handTrackingMode:
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
    drawRect(app.width//2 - 60, app.height - 60, 120, 40, fill=app.lightPink, border='black')
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
             fill=app.lightPink, border=app.darkBrown, borderWidth=2)
    
    drawLabel("←", app.universalBackButtonX + app.universalBackButtonWidth // 2,
              app.universalBackButtonY + app.universalBackButtonHeight // 2,
              size=20, bold=True, fill=app.darkBrown)

    
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


 