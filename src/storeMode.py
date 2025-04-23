from cmu_graphics import *
from buttons import *
import os





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
        self.pageNum = len(self.list)//40
        if self.type in ['Tanks', 'Tees', 'LongSleeves', 'Hoodies', 'Sweaters']:
            self.topOrBottom = 'Top'
        else:
            self.topOrBottom = 'Bottom'

    def __repr__(self):
        return self.list, self.type, self.pageNum, self.topOrBottom
    
storeClothes = [StoreClothes('CLOTHES/Tanks'), 
                StoreClothes('CLOTHES/Tees'),
                StoreClothes('CLOTHES/LongSleeves'),
                StoreClothes('CLOTHES/Hoodies'),
                StoreClothes('CLOTHES/Sweaters'),
                StoreClothes('CLOTHES/Jeans'),
                StoreClothes('CLOTHES/Shorts'),
                StoreClothes('CLOTHES/Skirts'),]
    


def drawStoreMode(app):
    whiteWidth = 136
    whiteHeight = 160
    drawRect(0, 0, app.width, app.height, fill='lightBlue')
    drawUniversalBackButton(app)

    if app.storePage == "pickType":
        drawRect(20, 220, 175, 140, fill='white')
        drawLabel('Tanks',20, 220)
        drawRect(215, 220, 175, 140, fill='white')
        drawLabel('Tees',215, 220)
        drawRect(410, 220, 175, 140, fill='white')
        drawLabel('Long Sleeves',410, 220)
        drawRect(605, 220, 175, 140, fill='white')
        drawLabel('Hoodies',605, 220)
        drawRect(20, 360, 175, 140, fill='white')
        drawLabel('Sweaters',20, 360)
        drawRect(215, 360, 175, 140, fill='white')
        drawLabel('Jeans',215, 360)
        drawRect(410, 360, 175, 140, fill='white')
        drawLabel('Shorts',410, 360)
        drawRect(605, 360, 175, 140, fill='white')
        drawLabel('Skirts',605, 360)
    else:
        type = storeClothes[app.storePage]
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
        


    

    #background, back and forward buttons, type label, page coun
    
    

    
    
    
    

    #forward and back buttons, page numbers
    pass
def addToCloset(app, mouseX, mouseY):
    type = storeClothes[app.storePage]
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
            if type.topOrBottom == 'Top':
                app.closetTops.append(image)
            else:
                app.closetBottoms.append(image)
           


