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
ratioPlants = plantsArea.countPlantsArea(imgPlants)

if (debugPrint==False):
    print (ratioPlants)

else:
    textRatio = str(int(ratioPlants * 100)) + "%"
    cv2.putText(imgPlants, textRatio, (imgPlants.shape[1]-150, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 1, 126), 5)
    cv2.imshow("Plants area", imgPlants)
    cv2.imwrite("output.png", imgPlants)
    cv2.waitKey(0)
