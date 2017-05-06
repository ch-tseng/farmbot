import argparse
import cv2
#import numpy as np
from lib.libFarm import SPROUT

# You can adjust the values here ---------------
createImage = True
reSize=(1000,563)
#-----------------------------------------------

ap = argparse.ArgumentParser()
ap.add_argument("-n", "--noSprout", required=True, help="Path to the image path with no seeds not sprouted")
ap.add_argument("-s", "--Sprout", required=True, help="Path to the image with seeds sprouted")

args = vars(ap.parse_args())

objSprout = SPROUT(cv2.imread(args["noSprout"]), reSize, (5,5), 120, 2,4)
numSprout = objSprout.countSprout(cv2.imread(args["Sprout"])) - objSprout.notSprout
print("sprout count: {}".format(numSprout))
cv2.waitKey(0)
