from cmu_graphics import *

def drawWelcomeScreen(app):
    drawImage(app.backgroundImage, 0, 0, width=app.width, height=app.height)
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
<<<<<<< Updated upstream
    #draw background image
    drawImage(app.instructionsBackgroundImage, 0, 0, width=app.width, height=app.height)

def drawInstructionsScreen(app):
    drawImage(app.instructionsBackgroundImage, 0, 0, width = app.width, 
             height = app.height)
#placeholder for background
    drawLabel("How to Play", app.width // 2, 100, size=36, bold=True, fill='darkmagenta')
    drawLabel("🧥 Drag clothes from the closet onto the mannequin.", app.width // 2, 180, size=20)
    drawLabel("🎨 Mix and match to style your best look!", app.width // 2, 220, size=20)
    drawLabel("💾 Press keys to save or shuffle outfits.", app.width // 2, 260, size=20)
    drawLabel("Click anywhere to begin!", app.width // 2, 350, size=18, italic=True, fill='gray')

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
=======
def drawUploadDialog(app):
    if app.show_upload_dialog:
        drawRect(100, 100, 600, 400, fill='white', border='black')
        drawLabel("UPLOAD YOUR CLOTHING", app.width/2, 130, size=24)
        drawRect(app.width/2 - 100, 200, 200, 200, fill='lightGray')
        drawLabel("Click to select photo", app.width/2, 300, size=18)
        drawRect(app.width/2 - 50, 450, 100, 40, fill='pink')
        drawLabel("UPLOAD", app.width/2, 470, size=18)
>>>>>>> Stashed changes
