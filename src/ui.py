from cmu_graphics import *

def drawWelcomeScreen(app):
    # Draw background image
    drawImage(app.backgroundImage, 0, 0, width=app.width, height=app.height)
    
    # Draw start button (placeholder)
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
    drawImage(app.instructionsBackgroundImage, 0, 0, width=app.width, height=app.height)

def drawInstructionsScreen(app):
    drawImage(app.instructionsBackgroundImage, 0, 0, width = app.width, 
             height = app.height)
    # drawLabel("How to Play", app.width // 2, 100, size=36, bold=True, fill='darkmagenta')
    # drawLabel("🧥 Drag clothes from the closet onto the mannequin.", app.width // 2, 180, size=20)
    # drawLabel("🎨 Mix and match to style your best look!", app.width // 2, 220, size=20)
    # drawLabel("💾 Press keys to save or shuffle outfits.", app.width // 2, 260, size=20)
    # drawLabel("Click anywhere to begin!", app.width // 2, 350, size=18, italic=True, fill='gray')

    # centerX = app.width // 2
    # drawLabel("Welcome to King’s Closet!", centerX, 60 + app.scrollY, size=24, fill='rosyBrown', bold=True)
    # drawLabel("1. Use the arrow keys to scroll through items.", centerX, 120 + app.scrollY, size=20, fill='rosyBrown')
    # drawLabel("2. Click on clothing pieces to try them on.", centerX, 180 + app.scrollY, size=20, fill='rosyBrown')
    # drawLabel("3. Mix and match tops and bottoms.", centerX, 240 + app.scrollY, size=20, fill='rosyBrown')
    # drawLabel("4. Press the mode switch buttons to toggle views.", centerX, 300 + app.scrollY, size=20, fill='rosyBrown')
    # drawLabel("5. Finalize your outfit and admire your creation!", centerX, 360 + app.scrollY, size=20, fill='rosyBrown')
    # drawLabel("Have fun styling!", centerX, 420 + app.scrollY, size=20, fill='rosyBrown', italic=True)
    boxWidth = 587
    boxHeight = 310
    boxX = (app.width - boxWidth) // 2
    boxY = 148
    
    drawRect(boxX, boxY, boxWidth, boxHeight, border='black', borderWidth=3, opacity = 0)
    contentY = boxY + 20 + app.scrollY

    visibleTop = boxY + 5
    visibleBottom = boxY + boxHeight - 5
    
    currentY = boxY + 20 + app.scrollY
    
    if visibleTop <= currentY <= visibleBottom - 24:  
        drawLabel("Welcome to King's Closet!", 
                 app.width // 2, currentY, 
                 size=24, fill='rosyBrown', bold=True)
    currentY += 60
    
    # Instruction 1
    if visibleTop <= currentY <= visibleBottom - 20:
        drawLabel("1. Use the up and down arrows to navigate through the instructions.", 
                 app.width // 2, currentY, 
                 size=20, fill='rosyBrown')
    currentY += 40
    
    # Instruction 2
    if visibleTop <= currentY <= visibleBottom - 20:
        drawLabel("2. Click on the arrows to try articles of clothing on.", 
                 app.width // 2, currentY, 
                 size=20, fill='rosyBrown')
    currentY += 40
    
    # Instruction 3
    if visibleTop <= currentY <= visibleBottom - 20:
        drawLabel("3. Mix and match tops and bottoms.", 
                 app.width // 2, currentY, 
                 size=20, fill='rosyBrown')
    currentY += 40

    #Instruction 4
    if visibleTop <= currentY <= visibleBottom - 20:
        drawLabel("4. Get feedback if your outfit matches or not",
                 app.width // 2, currentY, 
                 size=20, fill='rosyBrown')
    currentY += 40

   #Instruction 5
    if visibleTop <= currentY <= visibleBottom - 20:
        drawLabel("5. Press the button on the top right to play music",
                 app.width // 2, currentY, 
                 size=20, fill='rosyBrown')
    currentY += 40
    #Instruction 6
    if visibleTop <= currentY <= visibleBottom - 20:
        drawLabel("6. Generate a random outfit by pressing the shuffle button",
                 app.width // 2, currentY, 
                 size=20, fill='rosyBrown')
    currentY += 40
    # Instruction 7
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
    # Final message
    if visibleTop <= currentY <= visibleBottom - 20:
        drawLabel("Have fun styling!", 
                 app.width // 2, currentY, 
                 size=20, fill='rosyBrown', italic=True)
    
        
    drawRect(app.instructionsButtonX, app.instructionsButtonY,
             app.instructionsButtonWidth, app.instructionsButtonHeight,
             fill='pink', border='maroon', borderWidth=3)
    
    drawLabel(app.instructionsButtonText,
              app.instructionsButtonX + app.instructionsButtonWidth // 2,
              app.instructionsButtonY + app.instructionsButtonHeight // 2,
              size=24, bold=True, fill='maroon')
# from cmu_graphics import *
# import numpy as np

# def drawWelcomeScreen(app):
#     # Draw video frame if available
#     if app.videoManager.currentFrame is not None:
#         frame = app.videoManager.currentFrame
#         # Convert numpy array to CMU Graphics image
#         drawImage(frame, 0, 0, width=app.width, height=app.height)
    
#     # Dark overlay for better button visibility
#     drawRect(0, 0, app.width, app.height, fill='black', opacity=30)
    
#     # Draw start button
#     drawStartButton(app)

# def drawStartButton(app):
#     # Button background
#     drawRect(app.startButton['x'] - app.startButton['width']/2,
#              app.startButton['y'] - app.startButton['height']/2,
#              app.startButton['width'],
#              app.startButton['height'],
#              fill='gold', border='black', borderWidth=2)
    
#     # Button text
#     drawLabel("START GAME", 
#              app.startButton['x'], 
#              app.startButton['y'],
#              size=20, bold=True, fill='black')

# def drawMainGame(app):
#     # Placeholder for main game
#     drawRect(0, 0, app.width, app.height, fill='pink')
#     drawLabel("MAIN GAME SCREEN", 
#              app.width/2, app.height/2,
#              size=24, bold=True)

