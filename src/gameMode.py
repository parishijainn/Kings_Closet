from cmu_graphics import *
from clothesClasses import *

app.isSelectionMode = True
app.isDressingMode = False

app.currTopIndex = 0
app.currBottomIndex = 0
app.tops = []
app.bottoms = [Bottoms("images/yellowskirt.png")]
    
app.modeButtonWidth, app.modeButtonHeight = 160, 80

app.blackBarHeight = 50

app.whiteBoxWidth = app.width/3
app.whiteBowHeight = app.height - 2*app.blackBarHeight
app.whiteBoxX = app.width/3

app.distanceBetweenButtons = (app.whiteBoxWidth - app.forwardButtonWidth - 
                              2*app.buttonAllowance)
app.buttonAllowance = 10

app.forwardButtonWidth = app.whiteBoxWidth*0.33
app.forwardButtonHeight = app.blackBarHeight - app.blackBarHeight*0.2
app.forwardButtonX = app.whiteBoxWidth+app.buttonAllowance
app.forwardButtonY = ((app.height/2) - app.blackBarHeight +
                      (app.blackBarHeight-app.forwardButtomHeight)/2)

app.playButtonWidth = app.forwardButtonWidth*0.66
app.playButtonHeight = app.forwardButtonHeight
app.playButtonX = app.width/2 - app.playButtonWidth/2
app.playButtonY = app.forwardButtonY

def drawGameMode(app):
    #app.modeButtonWidth, app.modeButtonHeight = 160, 80
    #app.blackBarHeight = 50
    drawImage("images/cheetahBackground.png", 0, 0,
                 width=app.width, height=app.height)
    drawRect(0, 0, app.width, app.blackBarHeight, fill='black')
    drawRect(0, app.height-app.blackBarHeight, app.width,
             app.blackBarHeight, fill='black')
    drawRect(app.width/3, app.blackBarHeight, app.width/3, 
             app.height-app.blackBarHeight*2, fill='white')
    
    
    
    if app.isSelectionMode:
        drawRect(app.width/3, (app.height/2)-app.blackBarHeight, 
                 app.width/3, app.blackBarHeight, fill='black')
        drawRect(app.width/3, app.height-app.blackBarHeight*2, app.width/3, 
                 app.blackBarHeight, fill='black')
        #browse mode and dress me mode buttons
        drawRect(2*(app.width/3), 
                 app.height-app.blackBarHeight-app.modeButtonHeight, 
                 app.modeButtonWidth, app.modeButtonHeight, fill='gray')
        drawRect((app.width/3)-app.modeButtonWidth, 
                 app.height-app.blackBarHeight-app.modeButtonHeight, 
                 app.modeButtonWidth, app.modeButtonHeight, fill='gray')
        #shirts and pants play buttons
        drawRect(app.playButtonX, app.playButtonY, app.playButtonWidth,
                 app.playButtonHeight, fill='gray')
        drawRect(app.playButtonX, app.playButtonY+app.whiteBoxHeight/2,
                 app.playButtonWidth, app.playButtonHeight, fill='gray')
        #pants and shirts backwards buttons
        drawRect(app.forwardButtonX, app.forwardButtonY, app.forwardButtonWidth,
                 app.forwardButtonY, fill='gray')
        drawRect(app.forwardButtonX, app.forwardButtonY+app.whiteBoxHeight/2, 
                 app.forwardButtonWidth, app.forwardButtonY, fill='gray')
        #pants and shirts forward buttons
        drawRect(app.forwardButtonX+app.distanceBetweenButtons, 
                 app.forwardButtonY , app.forwardButtonWidth, 
                 app.forwardButtonY, fill='gray')
        drawRect(app.forwardButtonX+app.distanceBetweenButtons,
                 app.forwardButtonY+app.whiteBoxHeight/2, 
                 app.forwardButtonWidth, app.forwardButtonY, fill='gray')
        #images of tops and bottoms
        drawImage(app.bottoms[app.currBottomIndex].image, app.width/2, 
                  ((app.height/2)-app.blackBarIndex*2)/2, app.width/3, 
                  ((app.height/2)-app.blackBarIndex*2))
        drawImage(app.tops[app.currTopIndex].image, app.width/2, 
                  (app.height-app.blackBarIndex)/2, app.width/3, 
                  ((app.height/2)-app.blackBarHeight*2))

    if app.isDressingMode:
         drawImage("images/mannequin.png", 
                 app.width/2, app.height/2-10,
                 width=app.width/3, height=app.height-3*blackBarHeight,
                 align='center')
    
#def onMousePress(app, mouseX, mouseY):
    #if app.state == 'gameMode':    
        #if ((2*(app.width/3) <= mouseX <= 2*(app.width/3) + modeButtonwidth) and
            #((app.height-blackBarHeight-modeButtonHeight <= mouseY) and 
            #(mouseY <= app.height-blackBarHeight-modeButtonHeight + modeButtonHeight))):
            #dressme mode
                #app.isDressingMode == True
                #app.isSelectionMode == False
        #if ((app.width-modeButtonWidth <= mouseX <= app.width-modeButtonWidth + modeButtonwidth) and
            #(app.height-blackBarHeight-modeButtonHeight <= mouseY <= app.height-blackBarHeight-modeButtonHeight + modeButtonHeight)):
            #browse mode
                #app.isDressingMode == False
                #app.isSelectionMode == True

    #tops forward button press
    if (((app.forwardButtonX + app.differenceBetweenButtons <= app.mouseX) and 
        (app.mouseX <= (app.forwardButtonX + app.differenceBetweenButtons +
                        app.forwardButtonWidth))) and
        ((app.forwardButtonY <= app.mouseY) and 
        (app.mouseY <= app.forwardButtonY + app.forwardButtonHeight))):
        
        app.currTopIndex+=1
        app.currTopIndex %= len(app.tops)

    #tops backward button press
    if (((app.forwardButtonX <= app.mouseX) and 
        (app.mouseX <= app.forwardButtonX + app.forwardButtonWidth)) and
        ((app.forwardButtonY <= app.mouseY) and 
        (app.mouseY <= app.forwardButtonY + app.forwardButtonHeight))):

        app.currTopIndex-=1
        app.currTopIndex %= len(app.tops)

    #tops play button press
    if (((app.playButtonX <= app.mouseX) and 
        (app.mouseX <= app.playButtonX + app.playButtonWidth)) and
        ((app.playButtonY <= app.mouseY) and 
        (app.mouseY <= app.playButtonY + app.playButtonHeight))):

        pass

    #bottoms forward button press
    if (((app.forwardButtonX + app.differenceBetweenButtons <= app.mouseX) and 
        (app.mouseX <= (app.forwardButtonX + app.differenceBetweenButtons +
                        app.forwardButtonWidth))) and
        ((app.forwardButtonY+app.whiteBoxHeight/2<= app.mouseY) and 
        (app.mouseY <= app.forwardButtonY+app.whiteBoxHeight/2 + app.forwardButtonHeight))):

        app.currBottomIndex+=1
        app.currBottomIndex%=len(app.bottoms)

    #bottoms backward button press
    if (((app.forwardButtonX <= app.mouseX) and 
        (app.mouseX <= app.forwardButtonX + app.forwardButtonWidth)) and
        ((app.forwardButtonY+app.whiteBoxHeight/2 <= app.mouseY) and 
        (app.mouseY <= app.forwardButtonY+app.whiteBoxHeight/2 + app.forwardButtonHeight))):

        app.currBottomIndex-=1
        app.currBottomIndex%=len(app.bottoms)

    #bottoms play button press
    if (((app.playButtonX <= app.mouseX) and 
        (app.mouseX <= app.playButtonX + app.playButtonWidth)) and
        ((app.playButtonY+app.whiteBoxHeight/2 <= app.mouseY) and 
        (app.mouseY <= app.playButtonY+app.playButtonHeight+app.whiteBoxHeight/2))):

        pass



            