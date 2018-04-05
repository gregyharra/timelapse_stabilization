import numpy as np
import cv2

from transform import TransformParam
from math import atan2

# estimate the affine transformation between the frame
def rigid_estimation(mov):
    nbFrames = len(mov)
    file = open("outputFiles/outTransform.txt", "w")

    lk_params = dict(winSize  = (15,15),
                     maxLevel = 2,
                     criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

    # retrieve initial frame
    prev = mov[0]
    gray_prev = cv2.cvtColor(prev, cv2.COLOR_BGR2GRAY)

    last_T = np.matrix('1 0 0; 0 1 0')
    prev_to_cur_transform = []

    # iterate over all frames
    k = 1
    for t in range(1, nbFrames):
        # retrieve current frame
        cur = mov[t]
        gray_cur = cv2.cvtColor(cur, cv2.COLOR_BGR2GRAY)

        # find features to track in previous frames
        prev_corner = cv2.goodFeaturesToTrack(gray_prev, 200, 0.01, 30)
        # calculate new coordinates of features in current frame
        cur_corner, status, err = cv2.calcOpticalFlowPyrLK(gray_prev, gray_cur, 
                                                           prev_corner, None, 
                                                           **lk_params) 

        # remove outliers
        prev_corner1 = []
        cur_corner1 = []
        for s in range(0, len(status)):
            if status[s]:
                prev_corner1.append(prev_corner[s])
                cur_corner1.append(cur_corner[s])

        print "Frame: " + str(k) +  "/" + str(nbFrames) +  " - good optical flow: "  + str(len(prev_corner1));

    print "Done"
    return prev_to_cur_transform

