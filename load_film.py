import numpy as np
import cv2

# load film
def load_film(path, timelapse):
    cap = cv2.VideoCapture(path)

    if not (cap.isOpened()):
        print "unable to open file: " + path
        return

    output = []
    
    # create timelapse depending on user initial input
    i = 0
    while (cap.isOpened()):
        ret, frame = cap.read()
        i += 1
        if ret and not timelapse:
            output.append(frame)
        elif ret and i % 4 == 0:
            output.append(frame)
        if not ret:
            break

    cap.release()
    print "Done"
    return output

