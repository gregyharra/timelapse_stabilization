import numpy as np
import cv2
import os.path

# save a video
def save_file(mov, name):
    # retieve the size of a frame
    rows = mov[0].shape[0]
    cols = mov[0].shape[1]

    filename = 'outputVideos/' + name
    # delete the file if it exist to remove conflicts
    if os.path.exists(filename):
        os.remove(filename)
    
    # initialize a video writer
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(filename, fourcc, 30.0, (cols, rows))

    for i in range(0, len(mov)):
        # write to the file
        out.write(mov[i]);

    # close the file once writing is done
    out.release()
