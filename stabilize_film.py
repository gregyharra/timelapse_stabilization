import numpy as np
import cv2

from load_film import load_film
from rigid_estimation import rigid_estimation, remap_rigid_transform

if __name__ == "__main__":
    import sys

    if not( len(sys.argv) == 2 or len(sys.argv) == 3):
        print 'use this program like so:' 
        print 'python stabilize_film.py <path/to/video>'
        print 'or'
        print 'python stabilize_film.py <path/to/video> true'
        sys.exit(-1);

    path = sys.argv[1]

    if len(sys.argv) == 2:
        timelapse = True
    else:
        timelapse = False

    print "Loading film..."
    mov = load_film(path, timelapse)

    print "Estimating rigid transform..."
    transforms = rigid_estimation(mov)
