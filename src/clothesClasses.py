#from proccessImages import makeTransparent
#from PIL import Image
class Tops:
    def __init__(self, image):
        self.image = image
        #outputImage = image.replace(".png", "TransParent.png")
        #makeTransparent(image, outputImage, backgroundColor=(255, 255, 255))
        #self.image = outputImage
        #self.image = makeTransparent(image, image.replace(".png", "Transparent.png"), backgroundColor=(255, 255, 255))

class Bottoms:
    def __init__(self, image):
        self.image = image
        #self.image = makeTransparent(image, image.replace(".png", "Transparent.png"), backgroundColor=(255, 255, 255))
