import unittest
from dots.output import braille_3x2, braille_4x2, output_function
import numpy as np

class TestBraille3x2(unittest.TestCase):
    def test_single_line(self):
        input_matrix = np.array([
            [True, True, True, True]
        ])
        output = braille_3x2(input_matrix)
        self.assertEqual(len(output), 1)
        self.assertEqual(output[0], "⠉⠉")
    
    def test_single_column(self):
        input_matrix = np.array([
            [True],
            [True],
            [True],
        ])
        output = braille_3x2(input_matrix)
        self.assertEqual(len(output), 1)
        self.assertEqual(output[0], "⠇")

class TestBraille4x2(unittest.TestCase):
    def test_single_line(self):
        input_matrix = np.array([
            [True, True, True, True]
        ])
        output = braille_4x2(input_matrix)
        self.assertEqual(len(output), 1)
        self.assertEqual(output[0], "⠉⠉")
    
    def test_single_column(self):
        input_matrix = np.array([
            [True],
            [True],
            [True],
            [True],
        ])
        output = braille_4x2(input_matrix)
        self.assertEqual(len(output), 1)
        self.assertEqual(output[0], "⡇")

if __name__ == "__main__":
    unittest.main()