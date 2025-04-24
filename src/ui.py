from cmu_graphics import *
from buttons import *

def drawWelcomeScreen(app):
    #draw background image
    drawImage(app.backgroundImage, 0, 0, width=app.width, height=app.height)
    drawRect(app.usernameBoxX, app.usernameBoxY,app.usernameBoxWidth, 
             app.usernameBoxHeight, fill=app.lightPink, border=app.redBrown, 
             borderWidth=5)
    drawLabel(app.username or 'Enter your name', 
              app.usernameBoxX + app.usernameBoxWidth // 2,
              app.usernameBoxY + app.usernameBoxHeight // 2, size=20, 
              fill=app.redBrown, bold=True)
    
    if app.enteredUsername:
        drawStartButton(app)

def drawStartButton(app):
    isHovering = (app.mouseX is not None and app.mouseY is not None and
                  app.buttonX <= app.mouseX <= app.buttonX + app.buttonWidth and
                  app.buttonY <= app.mouseY <= app.buttonY + app.buttonHeight)

    fillColor = 'lavenderBlush' if not isHovering else 'pink'
    borderColor = 'maroon'
    textColor = 'maroon' if not isHovering else 'white'
    #button background
    drawRect(app.buttonX, app.buttonY, app.buttonWidth, app.buttonHeight,
             fill=fillColor, border=borderColor, borderWidth=5, 
             align='top-left')

    #button text
    drawLabel("start playing!", 
              app.buttonX + app.buttonWidth // 2, 
              app.buttonY + app.buttonHeight // 2, 
              size=35, bold=True, fill=textColor, font='monospace')

def drawMainGame(app):
    #draw background image
    drawImage(app.instructionsBackgroundImage, 0, 0, width=app.width, 
              height=app.height)

def drawInstructionsScreen(app):
    drawImage(app.instructionsBackgroundImage, 0, 0, width = app.width, 
             height = app.height)
    #draw instructions box to fit the png box
    boxWidth = 587
    boxHeight = 310
    boxX = (app.width - boxWidth) // 2
    boxY = 148
    
    drawRect(boxX, boxY, boxWidth, boxHeight, border='black', 
             borderWidth=3, opacity = 0)
    contentY = boxY + 20 + app.scrollY

    visibleTop = boxY + 5
    visibleBottom = boxY + boxHeight - 5
    
    currentY = boxY + 20 + app.scrollY
    
    if visibleTop <= currentY <= visibleBottom - 24:  
        drawLabel("Welcome to King's Closet!", 
                 app.width // 2, currentY, 
                 size=24, fill='rosyBrown', bold=True)
    currentY += 60
    
    #instruction 1
    if visibleTop <= currentY <= visibleBottom - 20:
        drawLabel(("1. Use the up and down arrows to navigate through the "
        "instructions."), 
                 app.width // 2, currentY, 
                 size=20, fill='rosyBrown')
    currentY += 40
    
    #instruction 2
    if visibleTop <= currentY <= visibleBottom - 20:
        drawLabel("2. Click on the arrows to try articles of clothing on.", 
                 app.width // 2, currentY, 
                 size=20, fill='rosyBrown')
    currentY += 40
    
    #instruction 3
    if visibleTop <= currentY <= visibleBottom - 20:
        drawLabel("3. Mix and match tops and bottoms.", 
                 app.width // 2, currentY, 
                 size=20, fill='rosyBrown')
    currentY += 40

    #instruction 4
    if visibleTop <= currentY <= visibleBottom - 20:
        drawLabel("4. Get feedback if your outfit matches or not",
                 app.width // 2, currentY, 
                 size=20, fill='rosyBrown')
    currentY += 40

   #instruction 5
    if visibleTop <= currentY <= visibleBottom - 20:
        drawLabel("5. Press the button on the top right to play music",
                 app.width // 2, currentY, 
                 size=20, fill='rosyBrown')
    currentY += 40
    #instruction 6
    if visibleTop <= currentY <= visibleBottom - 20:
        drawLabel("6. Generate a random outfit by pressing the shuffle button",
                 app.width // 2, currentY, 
                 size=20, fill='rosyBrown')
    currentY += 40
    #instruction 7
    if visibleTop <= currentY <= visibleBottom - 20:
        drawLabel("7. See how the outfit looks on you!", 
                 app.width // 2, currentY, 
                 size=20, fill='rosyBrown')
    currentY += 40

    if visibleTop <= currentY <= visibleBottom - 20:
        drawLabel("Finalize your outfit and admire your creation!", 
                 app.width // 2, currentY, 
                 size=20, fill='rosyBrown')
    currentY += 40
    #final message
    if visibleTop <= currentY <= visibleBottom - 20:
        drawLabel("Have fun styling!", 
                 app.width // 2, currentY, 
                 size=20, fill='rosyBrown', italic=True)
    

    #hover 
    hovered = (app.instructionsButtonX <= app.mouseX <= 
               app.instructionsButtonX + app.instructionsButtonWidth
               and app.instructionsButtonY <= app.mouseY <= 
               app.instructionsButtonY + app.instructionsButtonHeight)

    #choose colors
    color = 'lightPink' if hovered else 'pink'
    btnBorder = 'black' if hovered else 'white'

    # draw the button
    drawRect(app.instructionsButtonX, app.instructionsButtonY, 
             app.instructionsButtonWidth, app.instructionsButtonHeight,
             fill=color,
             border=btnBorder,
             borderWidth=3)

    
    drawLabel(app.instructionsButtonText,
              app.instructionsButtonX + app.instructionsButtonWidth // 2,
              app.instructionsButtonY + app.instructionsButtonHeight // 2,
              size=24, bold=True, fill='maroon')

def drawGameScreen(app):
    drawImage(app.gameScreenBackgroundImage, 0, 0, width=app.width, 
              height=app.height)
    drawLabel("Outfit Match Results", app.width // 2, 40, size=30, bold=True)

    topIndex = app.visibleTopIndex % len(app.tops)
    bottomIndex = app.visibleBottomIndex % len(app.bottoms)

    topImgPath = app.tops[topIndex].image
    bottomImgPath = app.bottoms[bottomIndex].image

    drawImage(topImgPath, app.width // 2, 150, width=180, height=180, 
              align='center')
    drawImage(bottomImgPath, app.width // 2, 340, width=180, height=180,
               align='center')

    drawLabel("Match Result:", app.width // 2, app.height - 140, size=22, 
              fill='black')
    drawLabel(app.feedbackText, app.width // 2, app.height - 110, size=26, 
              fill='darkmagenta', bold=True)

    drawPopupMenu(app)
