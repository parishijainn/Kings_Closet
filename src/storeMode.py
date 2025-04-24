from cmu_graphics import *
from buttons import *
import os
from clothesClasses import *
from gameMode import *



def putImagesIntoLists(folderPath):
    storeList = []
    for filename in os.listdir(folderPath):
        fullPath = os.path.join(folderPath, filename)
        if os.path.isfile(fullPath):
            storeList.append(fullPath)
    return storeList

class StoreClothes:
    def __init__(self, folderPath):
        self.image = folderPath
        self.type = folderPath.split('/')[-1]
        self.list = putImagesIntoLists(folderPath)
        if self.type in ['Tanks', 'Tees']:
            self.topOrBottom = 'Top'
        else:
            self.topOrBottom = 'Bottom'

    def __repr__(self):
        return self.list, self.type, self.topOrBottom
    
storeClothes = [StoreClothes('CLOTHES/Tanks'), 
                StoreClothes('CLOTHES/Tees'),
                StoreClothes('CLOTHES/Shorts'),
                StoreClothes('CLOTHES/Skirts'),]
prices = [15, 25, 40, 50]
    
# def drawStoreMode(app):
#     whiteWidth = 136
#     whiteHeight = 160
#     drawRect(0, 0, app.width, app.height, fill='lightBlue')

#     if app.state == "pickType":
#         drawLabel("Welcome to the Store!", app.width/2, 120)
#         drawLabel("What are you shopping for?", app.width/2, 140)
#         drawRect(20, 220, 175, 140, fill='white')
#         drawLabel('Tanks - $15',107, 290)
#         drawRect(215, 220, 175, 140, fill='white')
#         drawLabel('Tees - $25',302, 290)
#         drawRect(410, 220, 175, 140, fill='white')
#         drawLabel('Shorts - $40',497, 290)
#         drawRect(605, 220, 175, 140, fill='white')
#         drawLabel('Skirts - $50',692, 290)
        
#     else:
#         type = storeClothes[app.state]
#         imageCount = 0
#         drawLabel(f'{type.type} - ${prices[app.state]}', 50, 30)
#         x = 20
#         y = 70
#         for image in type.list:
#             imageCount += 1
#             if imageCount > 1:
#                 x += 156
#             if imageCount % 5 == 1 and imageCount != 1:
#                 x = 20
#                 y += 180  
#             drawRect(x, y, whiteWidth, whiteHeight, fill='white')
#             drawImage(image, x, y, width=whiteWidth, height=whiteHeight)
            
# def pressPickType(app):
#     if 20 <= app.mouseX <= 195 and 220 <= app.mouseY <= 360:
#         app.state = 0
#     elif 215 <= app.mouseX <= 390 and 220 <= app.mouseY <= 360:
#         app.state = 1
#     elif 410 <= app.mouseX <= 585 and 220 <= app.mouseY <= 360:
#         app.state = 2
#     elif 605 <= app.mouseX <= 780 and 220 <= app.mouseY <= 360:
#         app.state = 3

# def drawStoreMode(app):
#     whiteWidth = 136
#     whiteHeight = 160
#     drawRect(0, 0, app.width, app.height, fill='lightBlue')

#     if app.state == "pickType":
#         drawLabel("Welcome to the Store!", app.width/2, 120)
#         drawLabel("What are you shopping for?", app.width/2, 140)
#         drawRect(20, 220, 175, 140, fill='white')
#         drawLabel('Tanks - $15', 107, 290)
#         drawRect(215, 220, 175, 140, fill='white')
#         drawLabel('Tees - $25', 302, 290)
#         drawRect(410, 220, 175, 140, fill='white')
#         drawLabel('Shorts - $40', 497, 290)
#         drawRect(605, 220, 175, 140, fill='white')
#         drawLabel('Skirts - $50', 692, 290)
#     else:
#         # Ensure app.state is an integer
#         if isinstance(app.state, int):
#             type = storeClothes[app.state]
#             imageCount = 0
#             drawLabel(f'{type.type} - ${prices[app.state]}', 50, 30)
#             x = 20
#             y = 70
#             for image in type.list:
#                 imageCount += 1
#                 if imageCount > 1:
#                     x += 156
#                 if imageCount % 5 == 1 and imageCount != 1:
#                     x = 20
#                     y += 180  
#                 drawRect(x, y, whiteWidth, whiteHeight, fill='white')
#                 drawImage(image, x, y, width=whiteWidth, height=whiteHeight)

def drawStoreMode(app):
    whiteWidth = 136
    whiteHeight = 160
    drawRect(0, 0, app.width, app.height, fill='lightBlue')

    if app.state == "pickType":
        drawLabel("Welcome to the Store!", app.width/2, 120)
        drawLabel("What are you shopping for?", app.width/2, 140)
        drawRect(20, 220, 175, 140, fill='white')
        drawLabel('Tanks - $15', 107, 290)
        drawRect(215, 220, 175, 140, fill='white')
        drawLabel('Tees - $25', 302, 290)
        drawRect(410, 220, 175, 140, fill='white')
        drawLabel('Shorts - $40', 497, 290)
        drawRect(605, 220, 175, 140, fill='white')
        drawLabel('Skirts - $50', 692, 290)
    elif isinstance(app.state, int) and app.state in range(len(storeClothes)):
        type = storeClothes[app.state]
        drawLabel(f'{type.type} - ${prices[app.state]}', 50, 30)

        imageCount = 0
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


def pressPickType(app):
    if 20 <= app.mouseX <= 195 and 220 <= app.mouseY <= 360:
        app.state = 0  # Tanks
    elif 215 <= app.mouseX <= 390 and 220 <= app.mouseY <= 360:
        app.state = 1  # Tees
    elif 410 <= app.mouseX <= 585 and 220 <= app.mouseY <= 360:
        app.state = 2  # Shorts
    elif 605 <= app.mouseX <= 780 and 220 <= app.mouseY <= 360:
        app.state = 3  # Skirts

def addToCloset(app):
    type = storeClothes[app.state]
    price = prices[app.state]
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
        if x <= app.mouseX <= x + width and y <= app.mouseY <= y + height:
            if app.money < price:
                app.isInstructing = True
                drawLabel("ERROR: Insufficient funds!", 400, 200)
                drawLabel("Try selling some clothes from", 400, 250)
                drawLabel("your closet or putting", 400, 300)
                drawLabel("together a 100% perfect", 400, 350)
                drawLabel("outfit to earn more money", 400, 400)
            else:
                app.money -= price
                
                if type.topOrBottom == 'Top':
                    app.tops.append(Tops(type.list[imageCount-1]))
                    type.list.pop(imageCount-1)
                    app.closetTopPrices.append(price)
                    app.closetTopTypes.append(type.type)
                else:
                    app.bottoms.append(Bottoms(type.list[imageCount-1]))
                    type.list.pop(imageCount-1)
                    app.closetBottomPrices.append(price)
                    app.closetBottomTypes.append(type.type)
def sellTop(app):
    if 150 <= app.mouseX <= 375 and 375 <= app.mouseY <= 425:
            app.money += app.closetTopPrices[app.currTopIndex]
            app.tops.pop(app.currTopIndex)
            app.closetTopPrices.pop(app.currTopIndex)
            app.closetTopTypes.pop(app.currTopIndex)
            app.isInstructing = False
            app.state = "browse"
    if 425 <= app.mouseX <= 650 and 375 <= app.mouseY <= 425:
            app.isInstructing = False
            app.state = "browse"

def sellClothes(app):
    if (266 <= app.mouseX <= 532 and 50 <= app.mouseY <= 250):
        app.isInstructing = True
        app.state = 'sellTop'
        
        
            
            
    elif (266 <= app.mouseX <= 532 and 300 <= app.mouseY <= 500):
        app.isInstructing = True
        app.state = 'sellBottom'

        if 150 <= app.mouseX <= 375 and 375 <= app.mouseY <= 425:
            app.money += app.closetBottomPrices[app.currBottomIndex]
            app.bottoms.pop(app.currBottomIndex)
            app.closetBottomPrices.pop(app.currBottomIndex)
            app.closetBottomTypes.pop(app.currBottomIndex)
            app.isInstructing = False
        if 425 <= app.mouseX <= 650 and 375 <= app.mouseY <= 425:
            app.isInstructing = False

def drawSellTop(app):
    if app.isInstructing:
        drawImage(app.tops[app.currTopIndex].image,550, 200, width=125, height=150)
        drawLabel('Would you like',350, 200)
        drawLabel('to sell this', 350, 300)
        drawLabel(f'{app.closetTopTypes[app.currTopIndex]} for {app.closetTopPrices[app.currTopIndex]}?', 350, 400)
        drawRect(150, 375, 225, 50, fill='lightPink')
        drawLabel('Yes', 267, 400)
        drawRect(425, 375, 225, 50, fill='lightPink')
        drawLabel('No', 537, 400)

def drawSellBottom(app):
    drawImage(app.bottoms[app.currBottomIndex].image,600, 200, width=250, height=300)
    drawLabel('Would you like',350, 200)
    drawLabel('to sell this', 350, 300)
    drawLabel(f'{app.closetBottomTypes[app.currBottomIndex]} for {app.closetBottomPrices[app.currBottomIndex]}?',350, 400)
    drawRect(150, 375, 225, 50, fill='lightPink')
    drawLabel('Yes', 267, 400)
    drawRect(425, 375, 225, 50, fill='lightPink')
    drawLabel('No', 537, 400)



