from cmu_graphics import *
from buttons import drawCategoryButtons
from tkinter import filedialog, Tk
import json, os, uuid
from PIL import Image
def drawImportMode(app):
        drawImage("images/importModeBackground.jpeg", 0, 0, width=app.width,
                  height=app.height)
        drawRect(app.width/2, app.height/2, 400, 300, fill="white")
        runImportMode(app)
        drawCategoryButtons(app)
        
def runImportMode(app):
    def openFilePicker(app):
        root = Tk()
        root.withdraw()  # Hide the root window
        filePath = filedialog.askopenfilename(
            filetypes=[("Image files", "*.png *.jpg *.jpeg")]
        )
        root.destroy()

        if filePath:
            saveImportedImage(app, filePath)

    def saveImportedImage(app, filePath):
        img = Image.open(filePath).convert("RGBA")
        filename = f"{uuid.uuid4().hex}.png"

        if app.category == 'top':
            savePath = os.path.join(app.uploadFolderTops, filename)
            app.tops.append(savePath)
        else:
            savePath = os.path.join(app.uploadFolderBottoms, filename)
            app.bottoms.append(savePath)

        img.save(savePath, 'PNG')
        saveCloset(app)

        def saveCloset(app):
            with open(app.closetFile, 'w') as file:
                json.dump({'tops': app.tops, 'bottoms': app.bottoms}, file, indent=2)

        def loadCloset(app):
            if os.path.exists(app.closetFile):
                with open(app.closetFile, 'r') as file:
                    data = json.load(file)
                    app.tops = data.get('tops', [])
                    app.bottoms = data.get('bottoms', [])
