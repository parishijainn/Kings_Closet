from cmu_graphics import *

def drawGameMode(app):
    modeButtonWidth, modeButtonHeight = 160, 80
    blackBarHeight = 50
    drawImage("images/cheetahBackground.png", 0, 0,
                 width=app.width, height=app.height)
    drawRect(0, 0, app.width, blackBarHeight, fill='black')
    drawRect(0, app.height-blackBarHeight, app.width,
             blackBarHeight, fill='black')
    drawRect(app.width/3, blackBarHeight, app.width/3, 
             app.height-blackBarHeight*2, fill='white')
    if app.isSelectionMode:
        drawRect(app.width/3, (app.height/2)-blackBarHeight, 
                 app.width/3, blackBarHeight, fill='black')
        drawRect(app.width/3, app.height-blackBarHeight*2, app.width/3, 
                 blackBarHeight, fill='black')
        drawRect(2*(app.width/3), app.height-blackBarHeight-modeButtonHeight, 
                 modeButtonWidth, modeButtonHeight, fill='gray')
        drawRect((app.width/3)-modeButtonWidth, 
                 app.height-blackBarHeight-modeButtonHeight, 
                 modeButtonWidth, modeButtonHeight, fill='gray')
        
        #drawImage(bottoms[app.currBottomIndex], app.width/2, 
                  #((app.height/2)-blackBarIndex*2)/2, app.width/3, 
                  #((app.height/2)-blackBarIndex*2))
        #drawImage(tops[app.currTopIndex], app.width/2, 
                  #(app.height-blackBarIndex)/2, app.width/3, 
                  #((app.height/2)-blackBarHeight*2))

    if app.isDressingMode:
         drawImage("images/mannequin.png", 
                 app.width/2, app.height/2-10,
                 width=app.width/3, height=app.height-3*blackBarHeight,
                 align='center')
    
def onMousePress(app, mouseX, mouseY):
    if app.state == 'gameMode':    
        if ((2*(app.width/3) <= mouseX <= 2*(app.width/3) + modeButtonwidth) and
            ((app.height-blackBarHeight-modeButtonHeight <= mouseY) and 
            (mouseY <= app.height-blackBarHeight-modeButtonHeight + modeButtonHeight))):
            #dressme mode
                app.isDressingMode == True
                app.isSelectionMode == False
        if ((app.width-modeButtonWidth <= mouseX <= app.width-modeButtonWidth + modeButtonwidth) and
            (app.height-blackBarHeight-modeButtonHeight <= mouseY <= app.height-blackBarHeight-modeButtonHeight + modeButtonHeight)):
            #browse mode
                app.isDressingMode == False
                app.isSelectionMode == True
            