from cmu_graphics import *

def drawMannequinAndClothes(app):
    drawRect(20, 20, app.width/3, app.height - 40, fill = 'white')
    drawImage("images/mannequin.png", 
                 app.width, app.height,
                 width=60, height=80,
                 align='center')
    