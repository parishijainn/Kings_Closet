from cmu_graphics import *
from clothesClasses import *
from buttons import *
#from handtracking import processCameraFeed, getFingerPosition


app.isSelectionMode = True
app.isDressingMode = False

app.currTopIndex = 0
app.currBottomIndex = 0
app.tops = [Tops("images/shirt1.png"), Tops("images/shirt2.png"), Tops("images/shirt3.png"), Tops("images/shirt4.png"), Tops("images/shirt5.png"), Tops("images/shirt6.png")]
app.bottoms = [Bottoms("images/skirt1.png"), Bottoms("images/skirt2.png"), Bottoms("images/skirt3.png")]
    
app.modeButtonWidth, app.modeButtonHeight = 160, 80

app.blackBarHeight = 50

app.whiteBoxWidth = app.width/3
app.whiteBoxHeight = app.height - 2*app.blackBarHeight
app.whiteBoxX = app.width/3


app.buttonAllowance = 10
app.forwardButtonWidth = app.whiteBoxWidth*0.33
app.forwardButtonHeight = app.blackBarHeight - app.blackBarHeight*0.2
app.forwardButtonX = app.whiteBoxWidth+app.buttonAllowance
app.forwardButtonY = ((app.height/2) - app.blackBarHeight +
                      (app.blackBarHeight-app.forwardButtonHeight)/2)

app.backwardButtonX = app.width - app.whiteBoxWidth - app.forwardButtonWidth - 2*app.buttonAllowance
app.playButtonWidth = app.forwardButtonWidth*0.66
app.playButtonHeight = app.forwardButtonHeight
app.playButtonX = app.width/2 - app.playButtonWidth/2
app.playButtonY = app.forwardButtonY
app.feedbackText = ""

app.gradeButtonX = app.width-200
app.gradeButtonY = 100
app.gradeButtonWidth = 100
app.gradeButtonHeight = 40
app.backButtonX = app.width/2 - 60
app.backButtonY = app.height - 60
app.backButtonWidth = 120
app.backButtonHeight = 40

def drawGameMode(app):
    drawImage("images/cheetahBackground.png", 0, 0,
              width=app.width, height=app.height)
    drawRect(0, 0, app.width, app.blackBarHeight, fill='black')
    drawRect(0, app.height-app.blackBarHeight, app.width,
             app.blackBarHeight, fill='black')
    drawRect(app.width/3, app.blackBarHeight, app.width/3,
             app.height-app.blackBarHeight*2, fill='white')

    #mode switch buttons
    drawModeButtons(app)
    

    if app.isSelectionMode:
        drawRect(app.width/3, (app.height/2)-app.blackBarHeight, 
                 app.width/3, app.blackBarHeight, fill='black')
        drawRect(app.width/3, app.height-app.blackBarHeight*2, app.width/3, 
                 app.blackBarHeight, fill='black')

        #navigation and selection buttons
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
        drawImportButton(app)
        drawTryOnButton(app)


    #nav for entire top row of buttons
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

        
        #draw outfit images 
        topY = 140
        bottomY = 395
        imgWidth = 180
        imgHeight = 180
        drawImage(app.tops[app.currTopIndex].image, app.width//2, topY,
                  width=imgWidth, height=imgHeight, align='center')
        drawImage(app.bottoms[app.currBottomIndex].image, app.width//2, bottomY,
                  width=imgWidth, height=imgHeight, align='center')

        #feedback text
        drawLabel(app.feedbackText, app.width//2, app.height - 100,
                  size=22, fill='darkmagenta')

        #grade button
        drawRect(app.gradeButtonX, app.gradeButtonY, app.gradeButtonWidth, app.gradeButtonHeight, fill='plum', border='black')
        drawLabel("Grade", app.gradeButtonX + 25, app.gradeButtonY +20,
                  size=18, bold=True, align='left')

    if app.isDressingMode:
        topY = 180
        bottomY = 280
        imgWidthTop = 100
        imgHeightTop = 100
        imgWidthBottom = 120
        imgHeightBottom = 120
        drawImage("images/mannequinCropped.png", 
                  app.width/2, app.height/2,
                  width=app.width/3 - 60, height=app.height - 60,
                  align='center')
        drawImage(app.tops[app.currTopIndex].image, app.width//2, topY,
                  width=imgWidthTop, height=imgHeightTop, align='center')
        drawImage(app.bottoms[app.currBottomIndex].image, app.width//2, bottomY,
                  width=imgWidthBottom, height=imgHeightBottom, align='center')
        
    # frame = processCameraFeed()
    # if frame is not None:
    #     drawImage(frame, 10, 10, width=160, height=120)
    # if hasattr(app, 'latestCameraFrame') and app.latestCameraFrame:
    #     drawImage(app.latestCameraFrame, 10, 10, width=160, height=120)
