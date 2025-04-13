# from cmu_graphics import *
# from objects import HangerManager, OutfitManager
# from ui import drawWelcomeScreen, drawMainGame, drawInstructionsScreen 
# import os

# def onAppStart(app):
#     app.width = 800
#     app.height = 600
#     app.state = "welcome"
    
#     # Initialize managers
#     # app.hangerManager = HangerManager(app)
#     # app.outfitManager = OutfitManager(app)
    
#     app.backgroundImage = "images/kingclosetbackgrounds.png"
#     app.buttonWidth = 310
#     app.buttonHeight = 80
#     app.buttonX = app.width // 2 - app.buttonWidth // 2
#     app.buttonY = app.height // 2 + 45

    
#     app.mouseX = None
#     app.mouseY = None

# def onMousePress(app, mouseX, mouseY):
#     if app.state == "welcome":
#         if (app.buttonX <= mouseX <= app.buttonX + app.buttonWidth and
#             app.buttonY <= mouseY <= app.buttonY + app.buttonHeight):
#             app.state = "instructions"
# def onMouseMove(app, mouseX, mouseY):
#     app.mouseX = mouseX
#     app.mouseY = mouseY

# def redrawAll(app):
#     if app.state == "welcome":
#         drawWelcomeScreen(app)
#     elif app.state == "instructions":
#         drawInstructionsScreen(app)
#     elif app.state == "main":
#         drawMainGame(app)

# runApp(width=800, height=600)

from cmu_graphics import *
<<<<<<< Updated upstream
from objects import HangerManager, OutfitManager
from ui import drawWelcomeScreen, drawMainGame, drawInstructionsScreen 
from gameMode import drawGameMode
=======
from objects import OutfitManager
from ui import *
>>>>>>> Stashed changes
import os

def onAppStart(app):
    app.width = 800
    app.height = 600
    app.state = "welcome"
<<<<<<< Updated upstream
    #gameMode
    app.isSelectionMode = True
    app.isDressingMode = False
    app.currTopIndex = 0
    app.currBottomIndex = 0
    app.modeButtonWidth, app.modeButtonHeight = 160, 80
    app.blackBarHeight = 80
=======
    app.backgroundImage = "images/kingclosetbackgrounds.png"
>>>>>>> Stashed changes
    
    # Initialize managers
    app.outfitManager = OutfitManager()
    
    # UI elements
    app.buttonWidth = 310
    app.buttonHeight = 80
    app.buttonX = app.width // 2 - app.buttonWidth // 2
    app.buttonY = app.height // 2 + 45
<<<<<<< Updated upstream
    app.mouseX = None
    app.mouseY = None
=======
    
    # Upload state
    app.show_upload_dialog = False
    app.uploaded_image = None
    app.mouseX= None
    app.mouseY= None
>>>>>>> Stashed changes

    app.instructionsBackgroundImage = "images/instructions.png"
    app.instructionsButtonWidth = 250
    app.instructionsButtonHeight = 60
    app.instructionsButtonX = app.width // 2 - app.instructionsButtonWidth // 2
    app.instructionsButtonY = app.height - 120
    app.instructionsButtonText = "Start Styling"    
    
def onMousePress(app, mouseX, mouseY):
    if app.state == "welcome":
        if (app.buttonX <= mouseX <= app.buttonX + app.buttonWidth and
            app.buttonY <= mouseY <= app.buttonY + app.buttonHeight):
<<<<<<< Updated upstream
            app.state = "instructions"

    if app.state == "instructions":
        if (app.instructionsButtonX <= mouseX <= app.instructionsButtonX + app.instructionsButtonWidth and
            app.instructionsButtonY <= mouseY <= app.instructionsButtonY + app.instructionsButtonHeight):
            app.state = "gameMode"   

    if app.state == 'gameMode':    
        if ((2*(app.width/3) <= mouseX <= 2*(app.width/3) + app.modeButtonWidth) and
            ((app.height-app.blackBarHeight-app.modeButtonHeight <= mouseY <= app.height-app.blackBarHeight))):
            #dressme mode
            app.isDressingMode = True
            app.isSelectionMode = False
        if ((app.width-app.modeButtonWidth <= mouseX <= app.width-app.modeButtonWidth + app.modeButtonWidth) and
            (app.height-app.blackBarHeight-app.modeButtonHeight <= mouseY <= app.height-app.blackBarHeight-app.modeButtonHeight + app.modeButtonHeight)):
            #browse mode
            app.isDressingMode = False
            app.isSelectionMode = True

    
def onMouseMove(app, mouseX, mouseY):
    app.mouseX = mouseX
    app.mouseY = mouseY
=======
            app.state = "main"
    
    elif app.state == "main":
        # Check jacket selection
        for i, jacket in enumerate(app.outfitManager.jackets.keys()):
            x = 100 + (i * 90)
            if x <= mouseX <= x + 80 and 160 <= mouseY <= 160 + 80:
                app.outfitManager.current_outfit['top'] = f"images/jackets/{jacket}"
                grade_outfit(app)
        
        # Check upload button
        if (app.width/2 - 150 <= mouseX <= app.width/2 + 150 and
            300 <= mouseY <= 350):
            app.show_upload_dialog = True
        
        # Handle upload dialog
        if app.show_upload_dialog:
            if (app.width/2 - 100 <= mouseX <= app.width/2 + 100 and
                200 <= mouseY <= 400):
                # In a real app, this would open a file dialog
                app.uploaded_image = "user_uploads/photo.jpg"  # Placeholder
                app.outfitManager.current_outfit['top'] = app.uploaded_image
                grade_outfit(app, is_real_photo=True)
                app.show_upload_dialog = False

def grade_outfit(app, is_real_photo=False):
    """Grade the current outfit"""
    if app.outfitManager.current_outfit['top']:
        feedback, status, score = app.outfitManager.grade_outfit(
            app.outfitManager.current_outfit['top'],
            "jeans.png",  # Placeholder for bottoms
            is_real_photo
        )
        app.outfit_grade = (feedback, status, score)
>>>>>>> Stashed changes

def redrawAll(app):
    if app.state == "welcome":
        drawWelcomeScreen(app)
    elif app.state == "instructions":
        drawInstructionsScreen(app)
    # elif app.state == "gameMode":
    #     drawGameMode(app)
    elif app.state == "main":
        drawMainGame(app)
<<<<<<< Updated upstream
    elif app.state == 'gameMode':
        drawGameMode(app)
=======
        if app.show_upload_dialog:
            drawUploadDialog(app)
>>>>>>> Stashed changes

runApp(width=800, height=600)