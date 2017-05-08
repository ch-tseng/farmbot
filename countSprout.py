import argparse
import cv2
#import numpy as np
from lib.libFarm import SPROUT

# You can adjust the values here ---------------
reSize=(800,450)
#-----------------------------------------------

ap = argparse.ArgumentParser()
ap.add_argument("-n", "--noSprout", required=True, help="Path to the image path with no seeds not sprouted")
ap.add_argument("-s", "--Sprout", required=True, help="Path to the image with seeds sprouted")

args = vars(ap.parse_args())

objSprout = SPROUT(reSize=reSize, vThresh1=200, vThresh2=150, vErode=1, vDilate=2, debug=True)

# objSprout.countSprout( "image file" , "Sprout Size" )
numNoSprout = objSprout.countSprout(cv2.imread(args["noSprout"]), 35)
numSprout = objSprout.countSprout(cv2.imread(args["Sprout"]), 35)
countSprout = (numSprout-numNoSprout) if (numSprout-numNoSprout>0) else 0

print("sprout count: {} - {} = {}".format(numSprout, numNoSprout, countSprout))

cv2.waitKey(0)
