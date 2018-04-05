import numpy as np
import cv2
from math import cos, sin

# stabilize movie according to smooth trajectory
def stabilize(mov, transform, BORDER_CROP = 20):
    # retrieve frame size
    rows = mov[0].shape[0]
    cols = mov[0].shape[1]

    # get correct aspect ration for vertical cropping 
    VERTICAL_BORDER = int(BORDER_CROP * rows / cols)

    nbFrames = len(mov)

    T = np.asarray([[1,0,0],[0,1,0]],dtype=np.float32)
    compare = []
    stabalized = []
    # iterate over every frame, except the last frame as it doesn't have a valid 
    #transform, and rectify them
    for i in range (0, nbFrames -1):
        cur = mov[i]

    print "Done"
    return stabalized, compare
