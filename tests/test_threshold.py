import unittest
from dots.threshold import simple, otsu, adaptive_gaussian, threshold_function
import numpy as np


class TestSimpleThreshold(unittest.TestCase):
    def test_basic(self):
        image = np.array([[0, 127, 128, 255]], dtype=np.uint8)
        output = simple(image, point=127)
        self.assertTrue((output == [
            [False, False, True, True]
        ]).all())

    def test_different_point(self):
        image = np.array([[0, 127, 128, 255]], dtype=np.uint8)
        output = simple(image, point=128)
        self.assertTrue((output == [
            [False, False, False, True]
        ]).all())

    def test_via_threshold_function(self):
        image = np.array([[0, 127, 128, 255]], dtype=np.uint8)
        threshold_fn = threshold_function("simple")
        output = threshold_fn(image)
        self.assertTrue((output == [
            [False, False, True, True]
        ]).all())


class TestOtsuThreshold(unittest.TestCase):
    def test_basic(self):
        image = np.array([[0, 127, 255]], dtype=np.uint8)
        output = otsu(image)
        # The middle point value doesn't really matter...
        # Also we need to ignore the linter errors because
        # the inner numpy bool type can't be compared with "is".
        self.assertFalse(output[0][0] == True)  # noqa: E712
        self.assertTrue(output[0][2] == True)   # noqa: E712

    def test_peaks(self):
        image = np.array([
            [125, 125, 126, 126, 127, 127, 127, 128, 128, 128],
            [250, 251, 252, 253, 254, 254, 255, 255, 255, 255]
        ], dtype=np.uint8)
        output = otsu(image)
        self.assertTrue((output[0] == False).all())  # noqa: E712
        self.assertTrue((output[1] == True).all())   # noqa: E712

    def test_via_threshold_function(self):
        image = np.array([[0, 127, 255]], dtype=np.uint8)
        threshold_fn = threshold_function("otsu")
        output = threshold_fn(image)
        # The middle point value doesn't really matter...
        self.assertFalse(output[0][0] == True)  # noqa: E712
        self.assertTrue(output[0][2] == True)   # noqa: E712


class TestAdaptiveGaussianThreshold(unittest.TestCase):
    def test_basic(self):
        image = np.array([[0, 255]], dtype=np.uint8)
        output = adaptive_gaussian(image)
        self.assertTrue((output == [
            [False, True]
        ]).all())

    def test_via_threshold_function(self):
        image = np.array([[0, 255]], dtype=np.uint8)
        threshold_fn = threshold_function("adaptive_gaussian")
        output = threshold_fn(image)
        self.assertTrue((output == [
            [False, True]
        ]).all())


if __name__ == "__main__":
    unittest.main()
