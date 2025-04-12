from cmu_graphics import *

def onAppStart(app):
    app.color = 'purple'
    app.x = 0
    app.y = 0
    app.speed = 5
    app.direction = 0


def redrawAll(app):
    drawRect(app.x, app.y, 20, 20, fill=app.color)

runApp()

hello world !!!!!