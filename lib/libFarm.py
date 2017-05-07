import cv2
import numpy as np

class SPROUT:
    def __init__(self, reSize=(1000,563), vBlur=(5,5), vThresh=120, vErode=2, vDilate=4, debug=False):
        self.resize = reSize
        self.blur = vBlur
        self.thresh = vThresh
        self.erode = vErode
        self.dilate = vDilate
        self.indexNum = 0
        self.debug = debug

    def countSprout(self, image, size=2):
        self.indexNum += 1
        numSprouts = 0

        image = cv2.resize(image, self.resize, interpolation = cv2.INTER_AREA)
        if(self.debug==True):   
            cv2.imshow("Original #" + str(self.indexNum) , image)
            cv2.imwrite("original.png", image)

        #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        (H, S, gray) = cv2.split(hsv)
        blurred = cv2.GaussianBlur(gray, self.blur, 0) 
        (T, thresh) = cv2.threshold(blurred, self.thresh, 255, cv2.THRESH_BINARY)

        if(self.debug==True):
            cv2.imshow("Thresh A #" + str(self.indexNum) , thresh)

        thresh = cv2.dilate(thresh, None, iterations=self.dilate)
        thresh = cv2.erode(thresh, None, iterations=self.erode)

        if(self.debug==True):
            cv2.imshow("Thresh B #" + str(self.indexNum) , thresh)

        canny = cv2.Canny(thresh, 40, 150)

        if(self.debug==True):
            cv2.imshow("Canny #" + str(self.indexNum) , canny)

        (cnts, _) = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        for (i, c) in enumerate(cnts):
            area = cv2.contourArea(c)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            cv2.drawContours(image, [c], -1, (0, 255, 0), 2)

            if(area>=size):
                numSprouts += 1

        if(self.debug==True):
            font = cv2.FONT_HERSHEY_COMPLEX_SMALL
            cv2.putText(image, "Sprout count: " + str(numSprouts), (image.shape[1]-500, 40), font, 2, (255, 1, 126), 3)
            cv2.imshow("SPROUTS #" + str(self.indexNum) , image)

        return numSprouts

class PLANTSAREA:
    def __init__(self, imgPath, reSize=(250,250)):
        image = cv2.imread(imgPath)
        self.image = cv2.resize(image, reSize, interpolation = cv2.INTER_AREA)
        self.colorSpace = cv2.COLOR_BGR2LAB

    def extractPlantsArea(self, b_threshold=80, a_threshold=80):
        zeros = np.zeros(self.image.shape[:2], dtype = "uint8")

        imgLAB = cv2.cvtColor(self.image, self.colorSpace)
        (L, A, B) = cv2.split(imgLAB)

        (T_weeds_b, thresh_weeds_b) = cv2.threshold(B, b_threshold, 255, cv2.THRESH_BINARY)
        (T_weeds_a, thresh_weeds_a) = cv2.threshold(A, a_threshold, 255, cv2.THRESH_BINARY)
        imgRGB = cv2.merge([zeros, thresh_weeds_b, thresh_weeds_a])
        return imgRGB

    def countPlantsArea(self, image):
        width = image.shape[1]
        height = image.shape[0]
        gArea = 0.0
        rArea = 0.0
        grArea = 0.0

        for pixel_w in range(0, width, 1):
            for pixel_h in range(0, height, 1):
                (b, g, r) = image[pixel_h, pixel_w]
                if(g>0):
                    gArea += 1     
                if(r>0):
                    rArea += 1
                if(r>0 and g>0):
                    grArea += 1

        totalArea = width*height
        return (gArea/totalArea, rArea/totalArea, grArea/totalArea)
