from cmu_graphics import *
from clothesClasses import *

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

app.gradeButtonX = app.width/2 - 50
app.gradeButtonY = app.height - app.blackBarHeight - 60
app.gradeButtonWidth = 100
app.gradeButtonHeight = 40


# def drawGameMode(app):
#     #app.modeButtonWidth, app.modeButtonHeight = 160, 80
#     #app.blackBarHeight = 50
#     drawImage("images/cheetahBackground.png", 0, 0,
#                  width=app.width, height=app.height)
#     drawRect(0, 0, app.width, app.blackBarHeight, fill='black')
#     drawRect(0, app.height-app.blackBarHeight, app.width,
#              app.blackBarHeight, fill='black')
#     drawRect(app.width/3, app.blackBarHeight, app.width/3, 
#              app.height-app.blackBarHeight*2, fill='white')
#     #browse mode and dress me mode buttons
#     drawRect(2*(app.width/3), 
#              app.height-app.blackBarHeight-app.modeButtonHeight, 
#              app.modeButtonWidth, app.modeButtonHeight, fill='gray')
#     drawRect((app.width/3)-app.modeButtonWidth, 
#              app.height-app.blackBarHeight-app.modeButtonHeight, 
#              app.modeButtonWidth, app.modeButtonHeight, fill='gray')
    
    
#     if app.isSelectionMode:
#         drawRect(app.width/3, (app.height/2)-app.blackBarHeight, 
#                  app.width/3, app.blackBarHeight, fill='black')
#         drawRect(app.width/3, app.height-app.blackBarHeight*2, app.width/3, 
#                  app.blackBarHeight, fill='black')
        
#         #shirts and pants play buttons
#         drawRect(app.playButtonX, app.playButtonY, app.playButtonWidth,
#                  app.playButtonHeight, fill='gray')
#         drawRect(app.playButtonX, app.playButtonY+app.whiteBoxHeight/2,
#                  app.playButtonWidth, app.playButtonHeight, fill='gray')
#         #pants and shirts backwards buttons
#         drawRect(app.forwardButtonX, app.forwardButtonY, app.forwardButtonWidth,
#                  app.forwardButtonHeight, fill='gray')
#         drawRect(app.forwardButtonX, app.forwardButtonY+app.whiteBoxHeight/2, 
#                  app.forwardButtonWidth, app.forwardButtonHeight, fill='gray')
#         #pants and shirts forward buttons
#         drawRect(app.backwardButtonX, 
#                  app.forwardButtonY , app.forwardButtonWidth, 
#                  app.forwardButtonHeight, fill='gray')
#         drawRect(app.backwardButtonX,
#                  app.forwardButtonY+app.whiteBoxHeight/2, 
#                  app.forwardButtonWidth, app.forwardButtonHeight, fill='gray')
#         #images of tops and bottoms
#         drawImage(app.tops[app.currTopIndex].image, app.width/2, 
#                   ((app.height/2)-app.blackBarHeight*2), width=app.width/3, 
#                   height=((app.height/2)-app.blackBarHeight*2)/2, align='center')
#         drawImage(app.bottoms[app.currBottomIndex].image, app.width/2, 
#                   (app.height-app.blackBarHeight)/2, width=app.width/3, 
#                   height=((app.height/2)-app.blackBarHeight*2), align='center')

#     if app.isDressingMode:
#          drawImage("images/mannequin.png", 
#                  app.width/2, app.height/2-10,
#                  width=app.width/3, height=app.height-3*app.blackBarHeight,
#                  align='center')
#          drawImage(app.tops[app.currTopIndex].image, app.width/2, 
#                   ((app.height/2)-app.blackBarHeight*2), width=app.width/3, 
#                   height=((app.height/2)-app.blackBarHeight*2)/2, align='center')
#          drawImage(app.bottoms[app.currBottomIndex].image, app.width/2, 
#                   (app.height-app.blackBarHeight)/2, width=app.width/3, 
#                   height=((app.height/2)-app.blackBarHeight*2), align='center')


def drawGameMode(app):
    drawImage("images/cheetahBackground.png", 0, 0,
              width=app.width, height=app.height)
    drawRect(0, 0, app.width, app.blackBarHeight, fill='black')
    drawRect(0, app.height-app.blackBarHeight, app.width,
             app.blackBarHeight, fill='black')
    drawRect(app.width/3, app.blackBarHeight, app.width/3,
             app.height-app.blackBarHeight*2, fill='white')

    #mode switch buttons
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

        drawRect(app.backwardButtonX, app.forwardButtonY,  # Swapped X coordinates for backwardButton
                app.forwardButtonWidth, app.forwardButtonHeight, fill='gray')
        drawRect(app.backwardButtonX, app.forwardButtonY + app.whiteBoxHeight / 2,
                app.forwardButtonWidth, app.forwardButtonHeight, fill='gray')

        drawRect(app.forwardButtonX, app.forwardButtonY,  # Swapped X coordinates for forwardButton
                app.forwardButtonWidth, app.forwardButtonHeight, fill='gray')
        drawRect(app.forwardButtonX, app.forwardButtonY + app.whiteBoxHeight / 2,
                app.forwardButtonWidth, app.forwardButtonHeight, fill='gray')


    #nav for entire top row of buttons
#top buttons
        drawPolygon(app.backwardButtonX + 20, app.forwardButtonY + 10,
                    app.backwardButtonX + 20, app.forwardButtonY + app.forwardButtonHeight - 10,
                    app.backwardButtonX + 35, app.forwardButtonY + app.forwardButtonHeight / 2,
                    fill='white')
        drawPolygon(app.backwardButtonX + 40, app.forwardButtonY + 10,
                    app.backwardButtonX + 40, app.forwardButtonY + app.forwardButtonHeight - 10,
                    app.backwardButtonX + 55, app.forwardButtonY + app.forwardButtonHeight / 2,
                    fill='white')

        drawPolygon(app.playButtonX + 20, app.playButtonY + 10,
                    app.playButtonX + 20, app.playButtonY + app.playButtonHeight - 10,
                    app.playButtonX + app.playButtonWidth - 20, app.playButtonY + app.playButtonHeight / 2,
                    fill='white')

        drawPolygon(app.forwardButtonX + app.forwardButtonWidth - 20, app.forwardButtonY + 10,
                    app.forwardButtonX + app.forwardButtonWidth - 20, app.forwardButtonY + app.forwardButtonHeight - 10,
                    app.forwardButtonX + app.forwardButtonWidth - 35, app.forwardButtonY + app.forwardButtonHeight / 2,
                    fill='white')
        drawPolygon(app.forwardButtonX + app.forwardButtonWidth - 40, app.forwardButtonY + 10,
                    app.forwardButtonX + app.forwardButtonWidth - 40, app.forwardButtonY + app.forwardButtonHeight - 10,
                    app.forwardButtonX + app.forwardButtonWidth - 55, app.forwardButtonY + app.forwardButtonHeight / 2,
                    fill='white')


#bottom buttons
        drawPolygon(app.backwardButtonX + 20, app.forwardButtonY + app.whiteBoxHeight / 2 + 10,
                    app.backwardButtonX + 20, app.forwardButtonY + app.whiteBoxHeight / 2 + app.forwardButtonHeight - 10,
                    app.backwardButtonX + 35, app.forwardButtonY + app.whiteBoxHeight / 2 + app.forwardButtonHeight / 2,
                    fill='white')
        drawPolygon(app.backwardButtonX + 40, app.forwardButtonY + app.whiteBoxHeight / 2 + 10,
                    app.backwardButtonX + 40, app.forwardButtonY + app.whiteBoxHeight / 2 + app.forwardButtonHeight - 10,
                    app.backwardButtonX + 55, app.forwardButtonY + app.whiteBoxHeight / 2 + app.forwardButtonHeight / 2,
                    fill='white')

        drawPolygon(app.playButtonX + 20, app.playButtonY + app.whiteBoxHeight / 2 + 10,
                    app.playButtonX + 20, app.playButtonY + app.whiteBoxHeight / 2 + app.playButtonHeight - 10,
                    app.playButtonX + app.playButtonWidth - 20, app.playButtonY + app.whiteBoxHeight / 2 + app.playButtonHeight / 2,
                    fill='white')

        drawPolygon(app.forwardButtonX + app.forwardButtonWidth - 20, app.forwardButtonY + app.whiteBoxHeight / 2 + 10,
                    app.forwardButtonX + app.forwardButtonWidth - 20, app.forwardButtonY + app.whiteBoxHeight / 2 + app.forwardButtonHeight - 10,
                    app.forwardButtonX + app.forwardButtonWidth - 35, app.forwardButtonY + app.whiteBoxHeight / 2 + app.forwardButtonHeight / 2,
                    fill='white')
        drawPolygon(app.forwardButtonX + app.forwardButtonWidth - 40, app.forwardButtonY + app.whiteBoxHeight / 2 + 10,
                    app.forwardButtonX + app.forwardButtonWidth - 40, app.forwardButtonY + app.whiteBoxHeight / 2 + app.forwardButtonHeight - 10,
                    app.forwardButtonX + app.forwardButtonWidth - 55, app.forwardButtonY + app.whiteBoxHeight / 2 + app.forwardButtonHeight / 2,
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
        drawRect(app.width/2 - 50, app.height - app.blackBarHeight - 60,
                 100, 40, fill='plum', border='black')
        drawLabel("Grade", app.width/2, app.height - app.blackBarHeight - 40,
                  size=18, bold=True)

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

    # #tops forward button press
    # if (((app.backwardButtonX <= app.mouseX) and 
    #     (app.mouseX <= (app.backwardButtonX+
    #                     app.forwardButtonWidth))) and
    #     ((app.forwardButtonY <= app.mouseY) and 
    #     (app.mouseY <= app.forwardButtonY + app.forwardButtonHeight))):
        
    #     app.currTopIndex+=1
    #     app.currTopIndex %= len(app.tops)

    # #tops backward button press
    # if (((app.forwardButtonX <= app.mouseX) and 
    #     (app.mouseX <= app.forwardButtonX + app.forwardButtonWidth)) and
    #     ((app.forwardButtonY <= app.mouseY) and 
    #     (app.mouseY <= app.forwardButtonY + app.forwardButtonHeight))):

    #     app.currTopIndex-=1
    #     app.currTopIndex %= len(app.tops)

    # #tops play button press
    # if (((app.playButtonX <= app.mouseX) and 
    #     (app.mouseX <= app.playButtonX + app.playButtonWidth)) and
    #     ((app.playButtonY <= app.mouseY) and 
    #     (app.mouseY <= app.playButtonY + app.playButtonHeight))):

    #     pass

    # #bottoms forward button press
    # if (((app.backwardButtonX <= app.mouseX) and 
    #     (app.mouseX <= (app.backwardButtonX +
    #                     app.forwardButtonWidth))) and
    #     ((app.forwardButtonY+app.whiteBoxHeight/2<= app.mouseY) and 
    #     (app.mouseY <= app.forwardButtonY+app.whiteBoxHeight/2 + app.forwardButtonHeight))):

    #     app.currBottomIndex+=1
    #     app.currBottomIndex%=len(app.bottoms)

    # #bottoms backward button press
    # if (((app.forwardButtonX <= app.mouseX) and 
    #     (app.mouseX <= app.forwardButtonX + app.forwardButtonWidth)) and
    #     ((app.forwardButtonY+app.whiteBoxHeight/2 <= app.mouseY) and 
    #     (app.mouseY <= app.forwardButtonY+app.whiteBoxHeight/2 + app.forwardButtonHeight))):

    #     app.currBottomIndex-=1
    #     app.currBottomIndex%=len(app.bottoms)

    # #bottoms play button press
    # if (((app.playButtonX <= app.mouseX) and 
    #     (app.mouseX <= app.playButtonX + app.playButtonWidth)) and
    #     ((app.playButtonY+app.whiteBoxHeight/2 <= app.mouseY) and 
    #     (app.mouseY <= app.playButtonY+app.playButtonHeight+app.whiteBoxHeight/2))):

    #     pass