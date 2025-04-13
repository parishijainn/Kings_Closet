from cmu_graphics import *
import random

def drawWelcomeScreen(app):
    drawRect(0, 0, app.width, app.height, fill=rgb(30, 30, 30))
    
    # Draw all hangers
    for hanger in app.hangerManager.hangers:
        drawImage("images/hanger.png", 
                 hanger['x'], hanger['y'],
                 width=60, height=80,
                 rotateAngle=hanger['rotation'])
    
    drawLabel(app.welcomeText, 
             app.width/2, app.height/2 - 30, 
             size=36, bold=True, fill='gold')
    
    drawLabel(app.instructionText,
             app.width/2, app.height/2 + 30,
             size=20, fill='white')

def drawMainGame(app):
    # Pink background like Clueless
    drawRect(0, 0, app.width, app.height, fill='pink')
    
    # Decorative border
    drawCheetahBorder(app)
    
    # Main game UI
    drawLabel("CHER'S WARDROBE", app.width/2, 50, 
             size=28, font='monospace', bold=True)
    drawLabel("FALL FASHIONS", app.width/2, 80, 
             size=20, font='monospace')
    
    # Placeholder for outfit display
    drawLabel("OUTFIT SELECTION COMING SOON", 
             app.width/2, app.height/2, size=20)

def drawCheetahBorder(app):
    # Simple cheetah print pattern around edges
    for x in range(0, app.width, 40):
        for y in range(0, app.height, 40):
            if x < 40 or x > app.width-40 or y < 40 or y > app.height-40:
                if random.random() > 0.7:
                    drawCircle(x, y, 15, fill='black')
                    drawCircle(x+5, y+5, 5, fill='gold')

def drawInstructionsScreen(app):
        drawRect(0, 0, app.width, app.height, fill="lightgray")
        drawLabel("Instructions", app.width // 2, app.height // 4, size=30, bold=True)
        drawLabel("1. Use the mouse to interact.", app.width // 2, app.height // 2 - 20, size=20)
        drawLabel("2. Follow the on-screen prompts.", app.width // 2, app.height // 2 + 20, size=20)
        drawLabel("Click anywhere to continue.", app.width // 2, app.height - 50, size=20)