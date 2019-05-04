from pathlib import Path
import numpy as np
import cv2

class ImageLoader(object):
    def __init__(self, image):
        if type(image) is type(None):
            raise RuntimeError("image == None")
        self.image = image
    
    @classmethod
    def from_path(cls, path: Path):
        image = cv2.imread(path.resolve().as_posix(), cv2.IMREAD_UNCHANGED)
        return cls(image)
    
    @classmethod
    def from_bytes(cls, bytes):
        data_array = np.asarray(bytearray(bytes), dtype=np.uint8)
        image = cv2.imdecode(data_array, cv2.IMREAD_UNCHANGED)
        return cls(image)
    
    def resize_with_factor(self, factor: float):
        if factor == 1:
            return
        self.image = cv2.resize(self.image, None, fx = factor, fy = factor)
    
    def as_grayscale(self):
        return cv2.cvtColor(self.image, cv2.COLOR_RGB2GRAY)
    
    def transparency_mask(self, transparency_threshold = 127):
        w, h, channels = self.image.shape
        if channels < 4: # No alpha channel?
            return np.full((w, h), True)
        
        return self.image[:,:,3] < transparency_threshold

def resize_with_factor(image, factor):
    if factor == 1:
        return image
    
    return cv2.resize(image, None, fx = factor, fy = factor)

