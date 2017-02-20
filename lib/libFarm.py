import cv2
import numpy as np

class WEEDS:
    def __init__(self, imgPath, reSize=(250,250)):
        image = cv2.imread(imgPath)
        self.image = cv2.resize(image, reSize, interpolation = cv2.INTER_AREA)
        self.colorSpace = cv2.COLOR_BGR2LAB

    def displayImage(self, title="Image Display", image=None):
        if(image==None):
            cv2.imshow(title, self.image)
        else:
            cv2.imshow(title, image)

    def waitClose(self):
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def applyMask(self, r=55):
        maskPlant = np.zeros(self.image.shape[:2], dtype="uint8")
        cv2.circle(maskPlant, (125, 65), r, 255, -1)
        cv2.circle(maskPlant, (225, 75), r, 255, -1)
        cv2.circle(maskPlant, (320, 35), r, 255, -1)
        cv2.circle(maskPlant, (140, 245), r, 255, -1)
        cv2.circle(maskPlant, (255, 245), r, 255, -1)
        cv2.circle(maskPlant, (365, 210), r, 255, -1)

        self.image = cv2.bitwise_not(self.image, self.image, mask=maskPlant)

    def applyBlur(self, strong=(3,3)):
        self.image = cv2.GaussianBlur(imgB, strong, 0)

    def getImage(self):
        return self.image

    def extractWeeds(self, threshold=80, channel="B"):
        zeros = np.zeros(self.image.shape[:2], dtype = "uint8")

        imgLAB = cv2.cvtColor(self.image, self.colorSpace)
        (L, A, B) = cv2.split(imgLAB)
        if(channel=="B"):
            selectedChannel = B
        elif(channel=="L"):
            selectedChannel = L
        elif(channel=="A"):
            selectedChannel = A

        (T_weeds, thresh_weeds) = cv2.threshold(selectedChannel, threshold, 255, cv2.THRESH_BINARY)
        imgRGB = cv2.merge([zeros, thresh_weeds, zeros])
        self.image = imgRGB
        #imgGray = cv2.cvtColor(imgRGB, cv2.COLOR_BGR2GRAY)
