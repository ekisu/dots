import cv2

_THRESHOLD_FUNCTION_MAP = {}


def threshold(description: str):
    def _threshold_decorator(f):
        _THRESHOLD_FUNCTION_MAP[f.__name__] = (f, description)
        return f
    return _threshold_decorator


@threshold("Simple")
def simple(matrix, point: int = 127):
    return matrix > point


@threshold("Otsu's method")
def otsu(matrix):
    _thresh, binary_matrix = cv2.threshold(matrix, 0, 255,
                                           cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return binary_matrix == 255


@threshold("Adaptive Gaussian")
def adaptive_gaussian(matrix, block_size: int = 11, c: int = 2):
    return cv2.adaptiveThreshold(matrix, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                 cv2.THRESH_BINARY, block_size, c) == 255


def threshold_function(name: str):
    function, _desc = _THRESHOLD_FUNCTION_MAP[name]
    return function


def available_threshold_functions():
    return list(_THRESHOLD_FUNCTION_MAP.items())
