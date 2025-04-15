from cmu_graphics import *

#WELCOMEMODE
def drawStartPlayingButton(app):
     pass
def presStartPlayingButton(app):
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
    drawRect(app.gradeButtonX, app.gradeButtonY, app.gradeButtonWidth, 
             app.gradeButtonHeight, fill='lavenderBlush', border='maroon')
    drawLabel("Grade", app.gradeButtonX + app.gradeButtonWidth//2,
              app.gradeButtonY + app.gradeButtonHeight//2, size=15, bold=True)
def pressGradeButton(app):
    if (app.gradeButtonX <= app.mouseX <= (app.gradeButtonX + 
                                            app.gradeButtonWidth) and
        app.gradeButtonY <= app.mouseY <= (app.gradeButtonY +
                                            app.gradeButtonHeight)):
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
        #app.state = "tryOnMode"
        pass

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
