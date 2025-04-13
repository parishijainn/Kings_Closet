from cmu_graphics import *

def drawGameMode(app):
    app.isSelectionMode = True
    app.isDressingMode = False
    app.currTopIndex = 0
    app.currBottomIndex = 0
    
    modeButtonWidth, modeButtonHeight = 30, 60
    blackBarHeight = 20
    drawImage("images/cheetahBackground.png", 0, 0,
                 width=app.width, height=app.height)
    drawRect(0, 0, width=app.width, height=blackBarHeight, fill='black')
    drawRect(0, app.height-blackBarHeight, width=app.width,
             height=blackBarHeight, fill='black')
    drawRect(app.width/3, blackBarHeight, width=app.width/3, 
             height=app.height-blackBarHeight*2, fill='white')
    if app.isSelectionMode:
        drawRect(app.width/3, (app.height/2)-blackBarHeight, 
                 width=app.width/3, height=blackBarHeight, fill='black')
        drawRect(app.width/3, app.height-blackBarHeight*2, width=app.width/3, 
                 height=blackBarHeight, fill='black')
        drawRect(2*(app.width/3), app.height-blackBarHeight-modeButtonHeight, 
                 width=modeButtonWidth, height=modeButtonHeight, fill='gray')
        drawRect(app.width-modeButtonWidth, 
                 app.height-blackBarHeight-modeButtonHeight, 
                 width=modeButtonWidth, height=modeButtonHeight, fill='gray')
        drawImage(bottoms[app.currBottomIndex], app.width/2, 
                  ((app.height/2)-blackBarIndex*2)/2, width=app.width/3, 
                  height=((app.height/2)-blackBarIndex*2))
        drawImage(tops[app.currTopIndex], app.width/2, 
                  (app.height-blackBarIndex)/2, width=app.width/3, 
                  height=((app.height/2)-blackBarHeight*2))

    if app.isDressingMode:
    
def onMousePress(app, mouseX, mouseY):
    if isGameMode:    
        if ((2*(app.width/3) <= mouseX <= 2*(app.width/3) + modeButtonwidth) and
            ((app.height-blackBarHeight-modeButtonHeight <= mouseY) and 
            (mouseY <= app.height-blackBarHeight-modeButtonHeight + modeButtonHeight))):
            #dressme mode
            app.isDressingMode == True
            app.isSelectionMode == False
        if ((app.width-modeButtonWidth <= mouseX <= app.width-modeButtonWidth + modeButtonwidth) and
            (app.height-blakcBarHeight-modeButtonHeight <= mouseY <= app.height-blackBarHeight-modeButtonHeight + modeButtonHeight)):
            #browse mode
            app.isDressingMode == False
            app.isSelectionMode == True
            