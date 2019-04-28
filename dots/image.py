from pathlib import Path
import numpy as np
import cv2

class ImageLoader(object):
    def __init__(self, path: Path):
        self.path: Path = path
        self.image = cv2.imread(self.path.resolve().as_posix(), cv2.IMREAD_GRAYSCALE)
    
    def as_grayscale(self):
        return self.image

def resize_with_factor(image, factor):
    if factor == 1:
        return image
    
    return cv2.resize(image, None, fx = factor, fy = factor)

