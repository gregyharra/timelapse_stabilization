import numpy as np
import cv2

class TransformParam:
    def __init__(self, da, dx, dy):
        self.da = da
        self.dx = dx
        self.dy = dy
