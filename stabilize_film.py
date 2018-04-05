import numpy as np
import cv2

from load_film import load_film
from rigid_estimation import rigid_estimation, remap_rigid_transform
from trajectory import get_smooth_trajectory
from stabilize import stabilize
from save_file import save_file

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

    print "Estimating trajectory..."
    trajectories = get_smooth_trajectory(transforms)

    print "Remapping rigid transform..."
    new_transforms = remap_rigid_transform(transforms, trajectories)
    
    print "Stabilizing film..."
    stabilized, compare = stabilize(mov, new_transforms)

    print "Saving comparison video..."
    save_file(compare, "ComparisonVideo.avi")
    print "Done"

    print "Saving original video..."
    save_file(mov, "OriginalVideo.avi")
    print "Done"
    
    print "Saving stabilized video..."
    save_file(stabilized, "StabilizedVideo.avi")
    print "Done"
