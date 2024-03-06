
import os
imgPath = "Images/Notations"

class ImageGenerator:
    def __init__(self):
        pass

    def getImage(self, notation):
        for f in os.listdir(imgPath):
            if f.startswith(notation):
                imgFullPath = imgPath + "/" + f
                return imgFullPath
