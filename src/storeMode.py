from cmu_graphics import *
from buttons import *
import os

app.money = 500

def drawMoney(app):
    drawCircle(500, 20, 10, fill='lightYellow', border='black')
    drawLabel(f'$      {app.money}', 500, 20)

#drawLabel("ERROR: Insufficient funds!")
#drawLabel("Try selling some clothes from your closet to earn more money")
#drawLabel("or put together a 100% perfect outfit to earn $50")

def putImagesIntoLists(folderPath):
    storeList = []
    for filename in os.listdir(folderPath):
        fullPath = os.path.join(folderPath, filename)
        storeList.append(fullPath)
    return storeList

class StoreClothes:
    def __init__(self, folderPath):
        self.folderPath = folderPath
        self.type = folderPath.split('/')[-1]
        self.list = putImagesIntoLists(folderPath)
        if self.type in ['Tanks', 'Tees', 'LongSleeves', 'Hoodies', 'Sweaters']:
            self.topOrBottom = 'Top'
        else:
            self.topOrBottom = 'Bottom'

    def __repr__(self):
        return self.list, self.type, self.topOrBottom
    
storeClothes = [StoreClothes('CLOTHES/Tanks'), 
                StoreClothes('CLOTHES/Tees'),
                StoreClothes('CLOTHES/LongSleeves'),
                StoreClothes('CLOTHES/Hoodies'),
                StoreClothes('CLOTHES/Sweaters'),
                StoreClothes('CLOTHES/Jeans'),
                StoreClothes('CLOTHES/Shorts'),
                StoreClothes('CLOTHES/Skirts'),]
prices = [15, 20, 25, 40, 50, 50, 30, 40]
    
def drawStoreMode(app):
    whiteWidth = 136
    whiteHeight = 160
    drawRect(0, 0, app.width, app.height, fill='lightBlue')
    drawUniversalBackButton(app)

    if app.storePage == "pickType":
        drawLabel("Welcome to the Store!", app.width/2, 120)
        drawLabel("What are you shopping for?", app.width/2, 140)
        drawRect(20, 220, 175, 140, fill='white')
        drawLabel('Tanks - $15',107, 290)
        drawRect(215, 220, 175, 140, fill='white')
        drawLabel('Tees - $20',302, 290)
        drawRect(410, 220, 175, 140, fill='white')
        drawLabel('Long Sleeves - $25',497, 290)
        drawRect(605, 220, 175, 140, fill='white')
        drawLabel('Hoodies - $40',692, 290)
        drawRect(20, 380, 175, 140, fill='white')
        drawLabel('Sweaters - $50',107, 450)
        drawRect(215, 380, 175, 140, fill='white')
        drawLabel('Jeans - $50',302, 450)
        drawRect(410, 380, 175, 140, fill='white')
        drawLabel('Shorts - $30',497, 450)
        drawRect(605, 380, 175, 140, fill='white')
        drawLabel('Skirts - $40',692, 450)
    else:
        type = storeClothes[app.storePage]
        imageCount = 0
        drawLabel(f'{type.type} - ${prices[app.storePage]}', 50, 30)
        x = 20
        y = 70
        for image in type.list:
            imageCount += 1
            if imageCount > 1:
                x += 156
            if imageCount % 5 == 1 and imageCount != 1:
                x = 20
                y += 180  
            drawRect(x, y, whiteWidth, whiteHeight, fill='white')
            drawImage(image, x, y, width=whiteWidth, height=whiteHeight)
            
def pressPickType(app, x, y):
    if 20 <= x <= 195 and 220 <= y <= 360:
        app.storePage = 0
    elif 215 <= x <= 390 and 220 <= y <= 360:
        app.storePage = 1
    elif 410 <= x <= 585 and 220 <= y <= 360:
        app.storePage = 2
    elif 605 <= x <= 780 and 220 <= y <= 360:
        app.storePage = 3
    elif 20 <= x <= 195 and 360 <= y <= 500:
        app.storePage = 4
    elif 215 <= x <= 390 and 360 <= y <= 500:
        app.storePage = 5
    elif 410 <= x <= 585 and 360 <= y <= 500:
        app.storePage = 6
    elif 605 <= x <= 780 and 360 <= y <= 500:
        app.storePage = 7

def addToCloset(app, mouseX, mouseY):
    type = storeClothes[app.storePage]
    price = prices[app.storePage]
    imageCount = 0
    width = 136
    height = 160
    x = 20
    y = 70
    for image in type.list:
        imageCount += 1
        if imageCount > 1:
            x += 156
        if imageCount % 5 == 1 and imageCount != 1:
            x = 20
            y += 180  
        if x <= mouseX <= x + width and y <= mouseY <= y + height:
            if app.money < price:
                app.isInstructing = True
                #popup error
            else:
                app.money -= price
                type.list.pop(imageCount-1)
                if type.topOrBottom == 'Top':
                    app.closetTops.append(image)
                else:
                    app.closetBottoms.append(image)
           


