import argparse
#import cv2
#import numpy as np
from lib.libFarm import WEEDS

reSize=(800,450)

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

weeds = WEEDS(args["image"], reSize)
weeds.displayImage(title="Original")

#weeds.applyMask(r=50)
#weeds.displayImage(title="Masked")

weeds.extractWeeds_all(160, 140)
weeds.displayImage(title="Weeds area")
weeds.waitClose()
