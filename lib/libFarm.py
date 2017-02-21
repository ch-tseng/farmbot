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

    def extractWeeds_all(self, b_threshold=80, a_threshold=80):
        zeros = np.zeros(self.image.shape[:2], dtype = "uint8")

        imgLAB = cv2.cvtColor(self.image, self.colorSpace)
        (L, A, B) = cv2.split(imgLAB)

        (T_weeds_b, thresh_weeds_b) = cv2.threshold(B, b_threshold, 255, cv2.THRESH_BINARY)
        (T_weeds_a, thresh_weeds_a) = cv2.threshold(A, a_threshold, 255, cv2.THRESH_BINARY)
        imgRGB = cv2.merge([zeros, thresh_weeds_b, thresh_weeds_a])
        self.image = imgRGB

    def countPlantArea(self):
        image = self.image
        width = image.shape[1]
        height = image.shape[0]
        greenArea = 0.0
        
        for pixel_w in range(0, width, 1):
            for pixel_h in range(0, height, 1):
                (b, g, r) = image[pixel_h, pixel_w]
                if((b+g+r)>0):
                    greenArea += 1     

        plantArea = greenArea / (width*height)
        ratio = str(int(plantArea * 100)) + "%"
        cv2.putText(image, ratio, (width-150, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 1, 126), 5)
        self.image = image

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
