from cmu_graphics import *
from clothesClasses import *
from buttons import *
#from handtracking import processCameraFeed, getFingerPosition

def drawGameMode(app):
        drawImage("images/cheetahBackground.png", 0, 0,
                width=app.width, height=app.height)
        drawRect(0, 0, app.width, app.blackBarHeight, fill='black')
        drawRect(0, app.height-app.blackBarHeight, app.width,
                app.blackBarHeight, fill='black')
        drawRect(app.width/3, app.blackBarHeight, app.width/3,
                app.height-app.blackBarHeight*2, fill='white')
        
        if app.username:
                drawLabel(f"{app.username}'s closet", 10, 10, size=20, fill='white', align='left', bold=True)

        drawModeButtons(app)
        # if app.isSelectionMode:
        #         drawRect(app.width/3, (app.height/2)-app.blackBarHeight, 
        #                 app.width/3, app.blackBarHeight, fill='black')
        #         drawRect(app.width/3, app.height-app.blackBarHeight*2, app.width/3, 
        #                 app.blackBarHeight, fill='black')
        #         drawSelectionButtons(app)
        #         drawImportButton(app)
        #         drawTryOnButton(app)
                
        #         #draw outfit images 
        #         topY = 140
        #         bottomY = 395
        #         imgWidth = 180
        #         imgHeight = 180
        #         drawImage(app.tops[app.currTopIndex].image, app.width//2, topY,
        #                 width=imgWidth, height=imgHeight, align='center')
        #         drawImage(app.bottoms[app.currBottomIndex].image, app.width//2, bottomY,
        #                 width=imgWidth, height=imgHeight, align='center')

        #         #feedback text
        #         drawLabel(app.feedbackText, app.width//2, app.height - 100,
        #                 size=22, fill='darkmagenta')

        #         #grade button
        #         drawGradeButton(app)
        #         drawPopupMenu(app)
        # if app.isDressingMode:
        #         topY = 180
        #         bottomY = 280
        #         imgWidthTop = 100
        #         imgHeightTop = 100
        #         imgWidthBottom = 120
        #         imgHeightBottom = 120
        #         drawImage("images/mannequinCropped.png", 
        #                 app.width/2, app.height/2,
        #                 width=app.width/3 - 60, height=app.height - 60,
        #                 align='center')
        #         drawImage(app.tops[app.currTopIndex].image, app.width//2, topY,
        #                 width=imgWidthTop, height=imgHeightTop, align='center')
        #         drawImage(app.bottoms[app.currBottomIndex].image, app.width//2, bottomY,
        #                 width=imgWidthBottom, height=imgHeightBottom, align='center')
                
        # if app.handTrackingMode and app.cameraFrame:
        #         drawImage(app.cameraFrame, 20, 100, width=200, height=150)
        # if app.handTrackingMode:
        #         drawLabel("Swipe horizontally to change TOPS", 120, 300,
        #                 size=15, fill='maroon', bold=True)
        #         drawLabel("Swipe vertically to change BOTTOMS", 120, 320,
        #                 size=15, fill='maroon', bold=True)
        #         drawLabel("Hold up 5 fingers to get a random outfit!", 120, 340,
        #                 size=15, fill='maroon', bold=True)
        #         drawPopupMenu(app)
        if app.isSelectionMode:
                drawRect(app.width/3, (app.height/2)-app.blackBarHeight, app.width/3, app.blackBarHeight, fill='black')
                drawRect(app.width/3, app.height-app.blackBarHeight*2, app.width/3, app.blackBarHeight, fill='black')
                drawSelectionButtons(app)
                drawImportButton(app)
                drawTryOnButton(app)

                topY = 140
                bottomY = 395
                imgWidth = 180
                imgHeight = 180
                drawImage(app.tops[app.currTopIndex].image, app.width//2, topY, width=imgWidth, height=imgHeight, align='center')
                drawImage(app.bottoms[app.currBottomIndex].image, app.width//2, bottomY, width=imgWidth, height=imgHeight, align='center')

                drawLabel(app.feedbackText, app.width//2, app.height - 100, size=22, fill='darkmagenta')
                drawGradeButton(app)
                drawPopupMenu(app)

        if app.isDressingMode:
                topY = 180
                bottomY = 280
                imgWidthTop = 100
                imgHeightTop = 100
                imgWidthBottom = 120
                imgHeightBottom = 120
                drawImage("images/mannequinCropped.png", app.width/2, app.height/2, width=app.width/3 - 60, height=app.height - 60, align='center')
                drawImage(app.tops[app.currTopIndex].image, app.width//2, topY, width=imgWidthTop, height=imgHeightTop, align='center')
                drawImage(app.bottoms[app.currBottomIndex].image, app.width//2, bottomY, width=imgWidthBottom, height=imgHeightBottom, align='center')

        if app.handTrackingMode and app.cameraFrame:
                drawImage(app.cameraFrame, 20, 100, width=200, height=150)
        
        if app.handTrackingMode:
                drawLabel("Swipe horizontally to change TOPS", 120, 300, size=15, fill='maroon', bold=True)
                drawLabel("Swipe vertically to change BOTTOMS", 120, 320, size=15, fill='maroon', bold=True)
                drawLabel("Hold up 5 fingers to get a random outfit!", 120, 340, size=15, fill='maroon', bold=True)
                drawPopupMenu(app)