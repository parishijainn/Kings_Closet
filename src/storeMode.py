from cmu_graphics import *
from buttons import *
import os

app.money = 500
app.closetTopPrices = [20, 20, 20, 20, 20, 20]
app.closetBottomPrices = [20, 20, 20, 20, 20, 20]
app.closetTopTypes = ["Tees", "Tees", "Tees", "Tees", "Tees", "Tees"]
app.closetBottomTypes = ['Jeans', 'Jeans', 'Jeans', 'Jeans', 'Jeans', 'Jeans']
#drawMoney(app)
#drawStoreMode(app)
#if app.storePage == 'sellTop':
#drawSellTop(app)
#elif app.storePage == 'sellBottom':
#drawSellBottom(app)

def drawMoney(app):
    drawCircle(500, 20, 10, fill='lightYellow', border='black')
    drawLabel(f'$      {app.money}', 500, 20)

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
                drawLabel("ERROR: Insufficient funds!", 400, 200)
                drawLabel("Try selling some clothes from", 400, 250)
                drawLabel("your closet or putting", 400, 300)
                drawLabel("together a 100% perfect", 400, 350)
                drawLabel("outfit to earn more money", 400, 400)
            else:
                app.money -= price
                type.list.pop(imageCount-1)
                if type.topOrBottom == 'Top':
                    app.tops.append(image)
                    app.closetTopPrices.append(price)
                    app.closetTopTypes.append(type.type)
                else:
                    app.bottoms.append(image)
                    app.closetBottomPrices.append(price)
                    app.closetBottomTypes.append(type.type)

def sellClothes(app, mouseX, mouseY):
    if (app.whiteBoxX <= mouseX <= app.whiteBoxX+app.whiteBoxWidth and 
        50 <= mouseY <= 325):
        app.isInstructing = True
        app.storePage = 'sellTop'
        
        if 200 <= mouseX <= 450 and 550 <= mouseY <= 630:
            app.money += app.closetTopPrices[app.currTopIndex]
            app.tops.pop(app.currTopIndex)
            app.closetTopPrices.pop(app.currTopIndex)
            app.closetTopTypes.pop(app.currTopIndex)
            app.isInstructing = False
        if 550 <= mouseX <= 800 and 550 <= mouseY <= 630:
            app.isInstructing = False
    elif (app.whiteBoxX <= mouseX <= app.whiteBoxX+app.whiteBoxWidth and 
          375 <= mouseY <= 700):
        app.isInstructing = True
        app.storePage = 'sellBottom'
        if 200 <= mouseX <= 450 and 550 <= mouseY <= 630:
            app.money += app.closetBottomPrices[app.currBottomIndex]
            app.bottoms.pop(app.currBottomIndex)
            app.closetBottomPrices.pop(app.currBottomIndex)
            app.closetBottomTypes.pop(app.currBottomIndex)
            app.isInstructing = False
        if 550 <= mouseX <= 800 and 550 <= mouseY <= 630:
            app.isInstructing = False

def drawSellTop(app):
    drawImage(app.tops[app.currTopIndex],600, 200, width=250, height=300)
    drawLabel('Would you like',350, 200)
    drawLabel('to sell this', 350, 300)
    drawLabel(f'{app.closetTopTypes[app.currTopIndex]} for {app.closetTopPrices[app.currTopIndex]}?', 350, 400)
    drawRect(200, 550, 250, 80, fill='lightPink')
    drawLabel('Yes', 325, 590)
    drawRect(550, 550, 250, 80, fill='lightPink')
    drawLabel('No', 675, 590)
def drawSellBottom(app):
    drawImage(app.bottoms[app.currBottomIndex],600, 200, width=250, height=300)
    drawLabel('Would you like',350, 200)
    drawLabel('to sell this', 350, 300)
    drawLabel(f'{app.closetBottomTypes[app.currBottomIndex]} for {app.closetBottomPrices[app.currBottomIndex]}?',350, 400)
    drawRect(200, 550, 250, 80, fill='lightPink')
    drawLabel('Yes', 325, 590)
    drawRect(550, 550, 250, 80, fill='lightPink')
    drawLabel('No', 675, 590)



