import numpy as np
import cv2

class Trajectory:
    def __init__(self, x, y, a):
        self.x = x 
        self.y = y 
        self.a = a 

# accumulate the transform parameters to estimate a trajectory and use an 
# averaging window to smooth the trajectory
def get_smooth_trajectory(transform, smooth_radius = 30):
    a = 0
    x = 0
    y = 0

    file = open("outputFiles/outTrajectory.txt", "w")
    trajectories = []

    # accumulate transform parameters to get a trajectory
    for i in range(0, len(transform)):
        x += transform[i].dx
        y += transform[i].dy
        a += transform[i].da

        trajectories.append(Trajectory(x, y, a))

        file.write(str(i+1) + " " + str(x) + " " + str(y) + " " + str(a) + "\n")

    file.close()

    file = open("outputFiles/outSmoothTrajectory.txt", "w")
    smooth_trajectories = []

    # average the trajectory using a window size of 2*smooth_radius
    for i in range(0, len(trajectories)):
        sum_x = 0
        sum_y = 0
        sum_a = 0
        count = 0

        # calculate average trajectoryc
        for j in range(-smooth_radius, smooth_radius+1):
            if (i + j >= 0 and i + j < len(trajectories)):
                sum_x += trajectories[i+j].x
                sum_y += trajectories[i+j].y
                sum_a += trajectories[i+j].a
                count += 1

        sum_x /= count
        sum_y /= count
        sum_a /= count

        # save smooth directory
        smooth_trajectories.append(Trajectory(sum_x, sum_y, sum_a))

        file.write(str(i+1) + " " + str(sum_x) + " " + str(sum_y) + " " + str(sum_a) + "\n")

    print "Done"
    return smooth_trajectories
