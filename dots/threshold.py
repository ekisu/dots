import cv2

def simple(matrix, point = 127):
    return matrix > point

def simple_inv(matrix, point = 127):
    return matrix <= point

def otsu(matrix):
    _threshold_function, binary_matrix = cv2.threshold(matrix, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return binary_matrix

def adaptive_gaussian(matrix, block_size=11, c=2):
    return cv2.adaptiveThreshold(matrix, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, \
            cv2.THRESH_BINARY, block_size, c)

_THRESHOLD_FUNCTION_MAP = {
    'simple': simple,
    'simple_inv': simple_inv,
    'otsu': otsu,
    'adaptive_gaussian': adaptive_gaussian
}

def threshold_function(name):
    return _THRESHOLD_FUNCTION_MAP[name]
