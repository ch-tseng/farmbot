import argparse
import cv2
#import numpy as np
from lib.libFarm import PLANTSAREA

# You can adjust the values here ---------------
debugPrint = True
reSize=(800,450)
#-----------------------------------------------

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
ap.add_argument("-g", "--green", required=True, help="Threshold for green area (0~255)")
ap.add_argument("-r", "--red", required=True, help="Threshold for red area (0~255)")

args = vars(ap.parse_args())

plantsArea = PLANTSAREA(args["image"], reSize)

imgPlants = plantsArea.extractPlantsArea(b_threshold=int(args["green"]), a_threshold=int(args["red"]))
(greenArea, redArea, overlapArea) = plantsArea.countPlantsArea(imgPlants)
print greenArea, redArea, overlapArea

if (debugPrint==False):
    print (greenArea, redArea, overlapArea)

else:
    textRatio = str(int((greenArea+redArea-overlapArea) * 100)) + "%"

    font = cv2.FONT_HERSHEY_COMPLEX_SMALL
    cv2.putText(imgPlants, "green plants:" + str(int((greenArea+overlapArea)*100))+"%", (imgPlants.shape[1]-220, 20), font, 1, (255, 1, 126), 1)
    cv2.putText(imgPlants, "red plants:" + str(int(redArea*100))+"%", (imgPlants.shape[1]-220, 45), font, 1, (255, 1, 126), 1)
    cv2.putText(imgPlants, "total plants:" + textRatio, (imgPlants.shape[1]-220, 70), font, 1, (255, 1, 126), 1)
    cv2.imshow("Plants area", imgPlants)
    cv2.imwrite("output.png", imgPlants)
    cv2.waitKey(0)
