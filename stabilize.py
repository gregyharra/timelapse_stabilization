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

        if not cur.size:
            break

        # encode transform according to new trajectory
        da = transform[i].da
        T[0, 0] = cos(da)
        T[0, 1] = -sin(da)
        T[1, 0] = sin(da)
        T[1, 1] = cos(da)

        T[0, 2] = transform[i].dx
        T[1, 2] = transform[i].dy
        T = np.asarray(T,dtype=np.float32)

    print "Done"
    return stabalized, compare
