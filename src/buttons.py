from cmu_graphics import *
import random
from virtualtryon import tryOnCamera
import math
#from storeMode import *

#POPUP MENU
def drawPopupMenu(app):
    if app.isInstructing and app.state != 'storeMode':
        drawRect(app.popupX, app.popupY, app.popupWidth, app.popupHeight,
                 fill='white', border='black', align='center')
        drawRect(app.popupX, app.popupY - app.popupHeight/2 + 13, 
                 app.popupWidth, 30,
                 fill='lightpink', align='center', border='black')
        drawCircle(app.popupX - app.popupWidth/2 + 15, app.popupY - 
                   app.popupHeight/2 + 13,
                   10, fill='red')
        drawLabel("X", app.popupX - app.popupWidth/2 + 15, app.popupY - 
                  app.popupHeight/2 + 13,
                  size=15, fill='white')

        #Hand Tracking Mode Instructions
        if app.handTrackingMode:
            drawLabel("Hand Tracking Mode", app.popupX, app.popupY - 100, 
                      size=20, bold=True)
            drawLabel("• Swipe horizontally to change tops", app.popupX, 
                      app.popupY - 60, size=16)
            drawLabel("• Swipe vertically to change bottoms", app.popupX, 
                      app.popupY - 30, size=16)
            drawLabel("• Hold up 5 fingers for a random outfit", 
                      app.popupX, app.popupY, size=16)

        #game mode instructions
        elif app.state == "gameMode":
            drawLabel("Game Mode", app.popupX, app.popupY - 110, size=20, 
                      bold=True)
            drawLabel("• Click on the arrows to browse clothing", app.popupX, 
                      app.popupY - 80, size=16)
            drawLabel("• Mix and match tops and bottoms", app.popupX, 
                      app.popupY - 50, size=16)
            drawLabel("• Click the store to buy clothing with coins", 
                      app.popupX, app.popupY - 20, size=16)
            drawLabel("• Click handtracking to play without a keyboard", 
                      app.popupX, app.popupY + 10, size=16)
            drawLabel("• Click try on to see the outfit on your body", 
                      app.popupX, app.popupY + 40, size=16)
            drawLabel("• Click grade to get feedback on your outfit", 
                      app.popupX, app.popupY + 70, size=16)

        # Try On Mode Instructions
        elif app.state == 'tryOnMode':
            drawLabel("Try-On Mode", app.popupX, app.popupY - 40, 
                      size=20, bold=True)
            drawLabel("• Swipe right to change tops", app.popupX, 
                      app.popupY - 10, size=16)
            drawLabel("• Swipe left to change bottoms", 
                      app.popupX, app.popupY + 20, size=16)


def pressX(app):
    if (app.popupX-app.popupWidth/2+5 <= app.mouseX <= 
        app.popupX-app.popupWidth/2+25 and
        app.popupY-app.popupHeight/2+3 <= app.mouseY <= 
        app.popupY-app.popupHeight/2+23):
        app.isInstructing = False

#CATEGORY BUTTONS
def drawCategoryButtons(app):
    drawRect(app.topButtonX, app.topButtonY, 150, 
             100, fill="lightblue")
    drawLabel("Top", app.topButtonX, app.topButtonY, size=20,)
    drawRect(app.bottomButtonX, app.bottomButtonY, 150, 
             100, fill="lightblue")
    drawLabel("Bottom", app.bottomButtonX, app.bottomButtonY, size=20,)

def pressCategoryButtons(app):
    if (app.topButtonX <= app.mouseX <= app.topButtonX+150 and 
        app.topButtonY <= app.mouseY <= app.topButtonY+100):
        app.category = "top"
    if (app.bottomButtonX <= app.mouseX <= app.bottomButtonX+150 and 
         app.bottomButtonY <= app.mouseY <= app.bottomButtonY+100):
        app.category = "bottom"

#SOUND BUTTON       
def drawSoundButton(app):
    drawRect(app.soundButtonX, app.soundButtonY, 
             app.soundButtonSize, app.soundButtonSize,
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
     if (app.soundButtonX <= app.mouseX <= app.soundButtonX + 
         app.soundButtonSize and
            app.soundButtonY <= app.mouseY <= app.soundButtonY + 
            app.soundButtonSize):
        if app.soundIsPlaying:
            app.sound.pause()
            app.soundIsPlaying = False
        else:
            app.sound.play(restart=False)
            app.soundIsPlaying = True

#WELCOME MODE
def drawStartPlayingButton(app):
     pass

def pressStartPlayingButton(app):
     if (app.buttonX <= app.mouseX <= app.buttonX + app.buttonWidth and
                app.buttonY <= app.mouseY <= app.buttonY + app.buttonHeight):
            app.state = "instructions"
     
#INSTRUCTIONS MODE
def drawStartStylingButton(app):
     pass

def pressStartStylingButton(app):
     if (app.instructionsButtonX <= app.mouseX <= app.instructionsButtonX + 
         app.instructionsButtonWidth and
                app.instructionsButtonY <= app.mouseY <= app.instructionsButtonY 
                + app.instructionsButtonHeight):
            app.state = "browse"
     
#GAMEMODE
def drawModeButtons(app):
    buttonWidth = app.modeButtonWidth
    buttonHeight = app.modeButtonHeight * 1.5
    buttonXDressMe = 2 * (app.width / 3)  
    buttonXBrowse = app.width / 3 - app.modeButtonWidth
    buttonY = app.height // 2 - buttonHeight // 2 

    dressMePoints = []
    for i in range(6):
        angle = math.radians(60 * i)
        x = buttonXDressMe + buttonWidth / 2 + \
        (buttonWidth / 2) * math.cos(angle)
        y = buttonY + buttonHeight / 2 + \
        (buttonHeight / 2) * math.sin(angle)
        dressMePoints.append(x)
        dressMePoints.append(y)

    if (buttonXDressMe <= app.mouseX <= buttonXDressMe + buttonWidth and
        buttonY <= app.mouseY <= buttonY + buttonHeight):
        borderColor = 'black'
        borderWidth = 4
    else:
        borderColor = 'black'
        borderWidth = 1

    drawPolygon(*dressMePoints, fill=app.brown, border=borderColor, 
                borderWidth=borderWidth)
    drawLabel('Dress Me', buttonXDressMe + buttonWidth / 2, 
              buttonY + buttonHeight / 2, size=25, fill='white', bold=True)

    browsePoints = []
    for i in range(6):
        angle = math.radians(60 * i)
        x = buttonXBrowse + buttonWidth / 2 + \
        (buttonWidth / 2) * math.cos(angle)
        y = buttonY + buttonHeight / 2 + (buttonHeight / 2) * math.sin(angle)
        browsePoints.append(x)
        browsePoints.append(y)

    if (buttonXBrowse <= app.mouseX <= buttonXBrowse + buttonWidth and
        buttonY <= app.mouseY <= buttonY + buttonHeight):
        borderColor = 'black'
        borderWidth = 3
    else:
        borderColor = 'black'
        borderWidth = 1

    drawPolygon(*browsePoints, fill=app.brown, border=borderColor, 
                borderWidth=borderWidth)
    drawLabel('Browse', buttonXBrowse + buttonWidth / 2, 
              buttonY + buttonHeight / 2, size=25, fill='white', bold=True)

    centerX = app.width / 2 
    centerY = buttonY - 100  
    radius = 50
    angleStep = 360 / 6  
    points = []

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
    # Updated coordinates based on the new positioning of buttons
    if ((2 * (app.width / 3) <= app.mouseX <= 2 * (app.width / 3) + 
         app.modeButtonWidth) and
        (app.height // 2 - app.modeButtonHeight // 2 <= app.mouseY <= 
         app.height // 2 + app.modeButtonHeight // 2)):
            app.state = "dressMe"
            app.isDressingMode = True
            app.isSelectionMode = False

    if ((app.width / 3 - app.modeButtonWidth <= app.mouseX <= app.width / 3) and
        (app.height // 2 - app.modeButtonHeight // 2 <= app.mouseY <= 
         app.height // 2 + app.modeButtonHeight // 2)):
            app.state = "browse"
            app.isDressingMode = False
            app.isSelectionMode = True
    
    if (410 <= app.mouseX <= 540 and 5 <= app.mouseY <= 5 + 
        app.blackBarHeight - 10):
        app.handTrackingMode = not app.handTrackingMode
        if app.handTrackingMode:
            app.isInstructing = True

#GRADE BUTTONS
def drawGradeButton(app):
    drawRect(app.gradeButtonX, app.gradeButtonY, app.gradeButtonWidth, 
             app.gradeButtonHeight, fill=app.lightPink, border='black')
    drawLabel("Grade", app.gradeButtonX + app.gradeButtonWidth//2, 
              app.gradeButtonY + app.gradeButtonHeight//2,
              size=15, fill=app.darkBrown, bold=True, align='center')

def pressGradeButton(app):
    if (app.gradeButtonX <= app.mouseX <= (app.gradeButtonX + 
                                           app.gradeButtonWidth) and
        app.gradeButtonY <= app.mouseY <= (app.gradeButtonY + app.gradeButtonHeight)):
        
        topKey = app.topKeys[app.currTopIndex % len(app.topKeys)]
        bottomKey = app.bottomKeys[app.currBottomIndex % len(app.bottomKeys)]
        
        # Set the locked-in outfit
        app.visibleTopIndex = app.currTopIndex
        app.visibleBottomIndex = app.currBottomIndex

        message, rating = app.outfitManager.gradeOutfit(topKey, bottomKey)
        app.feedbackText = f"{message}"
        app.outfitRating = rating
        app.isGrading = True
        app.state = "gradeMode"

#STORE BUTTONS        
def drawStoreButton(app):
    drawRect(app.storeButtonX, app.storeButtonY, app.storeButtonWidth, 
             app.storeButtonHeight, fill=app.lightPink, border='black')
    drawLabel("Store", app.storeButtonX + app.storeButtonWidth//2,
              app.storeButtonY + app.storeButtonHeight//2, size=15, 
              bold=True, fill=app.darkBrown)
    
def pressStoreButton(app):
    if (app.storeButtonX <= app.mouseX <= (app.storeButtonX + 
                                            app.storeButtonWidth) and
        app.storeButtonY <= app.mouseY <= (app.storeButtonY +
                                            app.storeButtonHeight)):
        app.state = "pickType"
        
        

#TRY ON BUTTON   
def drawTryOnButton(app):
    drawRect(app.tryOnButtonX, app.tryOnButtonY, app.tryOnButtonWidth, 
             app.tryOnButtonHeight, fill=app.lightPink, border='black')
    drawLabel("Try On", app.tryOnButtonX + app.tryOnButtonWidth//2,
              app.tryOnButtonY + app.tryOnButtonHeight//2, size=15,
              bold=True, fill=app.darkBrown)

def pressTryOnButton(app):
     if (app.tryOnButtonX <= app.mouseX <= (app.tryOnButtonX + 
                                            app.tryOnButtonWidth) and
        app.tryOnButtonY <= app.mouseY <= (app.tryOnButtonY +
                                            app.tryOnButtonHeight)):
        app.state = "tryOnMode"
        tryOnCamera(app)
        app.isInstructing = True


#SELECTION BUTTONS
def drawSelectionButtons(app):
    if not app.handTrackingMode:
        drawRect(app.playButtonX, app.playButtonY, app.playButtonWidth,
                app.playButtonHeight, fill='gray')
        drawRect(app.playButtonX, app.playButtonY + app.whiteBoxHeight / 2,
                app.playButtonWidth, app.playButtonHeight, fill='gray')
        drawRect(app.forwardButtonX, app.backwardButtonY,  
                 #swapped X coordinates for backwardButton
                app.backwardButtonWidth, app.backwardButtonHeight, fill='gray')
        drawRect(app.forwardButtonX, app.backwardButtonY + app.whiteBoxHeight / 2,
                app.backwardButtonWidth, app.backwardButtonHeight, fill='gray')
        drawRect(app.backwardButtonX, app.backwardButtonY,  
                 #swapped X coordinates for forwardButton
                app.backwardButtonWidth, app.backwardButtonHeight, fill='gray')
        drawRect(app.backwardButtonX, app.backwardButtonY + 
                 app.whiteBoxHeight / 2,
                app.backwardButtonWidth, app.backwardButtonHeight, fill='gray')
        #top buttons
        drawPolygon(app.forwardButtonX + 20, app.backwardButtonY + 10,
                    app.forwardButtonX + 20, app.backwardButtonY + 
                    app.backwardButtonHeight - 10,
                    app.forwardButtonX + 35, app.backwardButtonY + 
                    app.backwardButtonHeight / 2,
                    fill='white')
        drawPolygon(app.forwardButtonX + 40, app.backwardButtonY + 10,
                    app.forwardButtonX + 40, app.backwardButtonY + 
                    app.backwardButtonHeight - 10,
                    app.forwardButtonX + 55, app.backwardButtonY + 
                    app.backwardButtonHeight / 2,
                    fill='white')
        drawPolygon(app.playButtonX + 20, app.playButtonY + 10,
                    app.playButtonX + 20, app.playButtonY + 
                    app.playButtonHeight - 10,
                    app.playButtonX + app.playButtonWidth - 20, 
                    app.playButtonY + app.playButtonHeight / 2,
                    fill='white')
        drawPolygon(app.backwardButtonX + app.backwardButtonWidth - 20, 
                    app.backwardButtonY + 10,
                    app.backwardButtonX + app.backwardButtonWidth - 20, 
                    app.backwardButtonY + app.backwardButtonHeight - 10,
                    app.backwardButtonX + app.backwardButtonWidth - 35, 
                    app.backwardButtonY + app.backwardButtonHeight / 2,
                    fill='white')
        drawPolygon(app.backwardButtonX + app.backwardButtonWidth - 40, 
                    app.backwardButtonY + 10,
                    app.backwardButtonX + app.backwardButtonWidth - 40, 
                    app.backwardButtonY + app.backwardButtonHeight - 10,
                    app.backwardButtonX + app.backwardButtonWidth - 55, 
                    app.backwardButtonY + app.backwardButtonHeight / 2,
                    fill='white')
        #bottom buttons
        drawPolygon(app.forwardButtonX + 20, app.backwardButtonY + 
                    app.whiteBoxHeight / 2 + 10,
                    app.forwardButtonX + 20, app.backwardButtonY + 
                    app.whiteBoxHeight / 2 + app.backwardButtonHeight - 10,
                    app.forwardButtonX + 35, app.backwardButtonY + 
                    app.whiteBoxHeight / 2 + app.backwardButtonHeight / 2,
                    fill='white')
        drawPolygon(app.forwardButtonX + 40, app.backwardButtonY + 
                    app.whiteBoxHeight / 2 + 10,
                    app.forwardButtonX + 40, app.backwardButtonY + 
                    app.whiteBoxHeight / 2 + app.backwardButtonHeight - 10,
                    app.forwardButtonX + 55, app.backwardButtonY + 
                    app.whiteBoxHeight / 2 + app.backwardButtonHeight / 2,
                    fill='white')
        drawPolygon(app.playButtonX + 20, app.playButtonY + 
                    app.whiteBoxHeight / 2 + 10,
                    app.playButtonX + 20, app.playButtonY + 
                    app.whiteBoxHeight / 2 + app.playButtonHeight - 10,
                    app.playButtonX + app.playButtonWidth - 20, 
                    app.playButtonY + app.whiteBoxHeight / 2 + 
                    app.playButtonHeight / 2,
                    fill='white')
        drawPolygon(app.backwardButtonX + app.backwardButtonWidth - 20, 
                    app.backwardButtonY + app.whiteBoxHeight / 2 + 10,
                    app.backwardButtonX + app.backwardButtonWidth - 20, 
                    app.backwardButtonY + app.whiteBoxHeight / 2 + 
                    app.backwardButtonHeight - 10,
                    app.backwardButtonX + app.backwardButtonWidth - 35, 
                    app.backwardButtonY + app.whiteBoxHeight / 2 + 
                    app.backwardButtonHeight / 2,
                    fill='white')
        drawPolygon(app.backwardButtonX + app.backwardButtonWidth - 40, 
                    app.backwardButtonY + app.whiteBoxHeight / 2 + 10,
                    app.backwardButtonX + app.backwardButtonWidth - 40, 
                    app.backwardButtonY + app.whiteBoxHeight / 2 + 
                    app.backwardButtonHeight - 10,
                    app.backwardButtonX + app.backwardButtonWidth - 55, 
                    app.backwardButtonY + app.whiteBoxHeight / 2 + 
                    app.backwardButtonHeight / 2,
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
         (app.mouseY <= app.backwardButtonY+app.whiteBoxHeight/2 + 
          app.backwardButtonHeight))):
        app.currBottomIndex+=1
        app.currBottomIndex%=len(app.bottoms)
    #bottoms backward button press
    if (((app.backwardButtonX <= app.mouseX) and 
         (app.mouseX <= app.backwardButtonX + app.backwardButtonWidth)) and
        ((app.backwardButtonY+app.whiteBoxHeight/2 <= app.mouseY) and 
         (app.mouseY <= app.backwardButtonY+app.whiteBoxHeight/2 + 
          app.backwardButtonHeight))):
        app.currBottomIndex-=1
        app.currBottomIndex%=len(app.bottoms)
    #tops play button press
    if (app.playButtonX <= app.mouseX <= app.playButtonX + 
        app.playButtonWidth and
        app.playButtonY <= app.mouseY <= app.playButtonY + 
        app.playButtonHeight):
        app.currTopIndex = random.randint(0, len(app.tops) - 1)
    #bottoms play button press
    if (app.playButtonX <= app.mouseX <= app.playButtonX + 
        app.playButtonWidth and
        app.playButtonY + app.whiteBoxHeight / 2 <= app.mouseY <= 
        app.playButtonY + 
        app.whiteBoxHeight / 2 + app.playButtonHeight):
        app.currBottomIndex = random.randint(0, len(app.bottoms) - 1)


#BACK BUTTONS
def drawBackButton(app):
    drawRect(app.width//2 - 60, app.height - 60, 120, 40, 
             fill=app.lightPink, border='black')
    drawLabel("Back", app.width//2, app.height - 40, size=18, bold=True)

def pressBackButton(app):
     if ((app.backButtonX <= app.mouseX <= 
          app.backButtonX + app.backButtonWidth) and
            (app.backButtonY <= app.mouseY <= 
             app.backButtonY + app.backButtonHeight)):
            app.state = "gameMode"
            app.feedbackText = ""
            app.isGrading = False 

def drawUniversalBackButton(app):
    drawRect(app.universalBackButtonX, app.universalBackButtonY,
             app.universalBackButtonWidth, app.universalBackButtonHeight,
             fill=app.lightPink, border=app.darkBrown, borderWidth=2)
    
    drawLabel("←", app.universalBackButtonX + app.universalBackButtonWidth // 2,
              app.universalBackButtonY + app.universalBackButtonHeight // 2,
              size=20, bold=True, fill=app.darkBrown)
   
def pressUniversalBackButton(app):
    if (app.universalBackButtonX <= app.mouseX <= 
        app.universalBackButtonX + app.universalBackButtonWidth and
        app.universalBackButtonY <= app.mouseY <= 
        app.universalBackButtonY + app.universalBackButtonHeight):
    #go back to previous page
        if app.state == "instructions":
            app.state = "welcome"
        elif app.state == "browse" or app.state == "dressMe":
            app.state = "instructions"
        elif app.state == "gradeMode":
            app.state = "browse"
            app.feedbackText = ""
            app.isGrading = False
        elif app.state == 'pickType':
            app.state = "browse"
        elif app.state == 0 or 1 or 2 or 3:
            app.state = "pickType"
            


 