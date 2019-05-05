import unittest
from dots.image import ImageLoader
from pathlib import Path
import numpy as np

def asset_path_builder(sub_path: Path) -> Path:
    assets_folder = Path(__file__).parent
    return assets_folder.joinpath(Path("assets"), sub_path)

class TestImageLoader(unittest.TestCase):
    def test_inexistant_image(self):
        with self.assertRaises(RuntimeError):
            image = ImageLoader.from_path(asset_path_builder("inexistant_image.png"))

    def test_basic_jpg(self):
        image = ImageLoader.from_path(asset_path_builder("2x1_black_white.jpg"))
        expected_grayscale = np.array([
            [0, 255]
        ], dtype=np.uint8)
        self.assertTrue((image.as_grayscale() == expected_grayscale).all())
    
    def test_basic_png(self):
        image = ImageLoader.from_path(asset_path_builder("2x1_black_white.png"))
        expected_grayscale = np.array([
            [0, 255]
        ], dtype=np.uint8)
        self.assertTrue((image.as_grayscale() == expected_grayscale).all())

    def test_transparency_mask(self):
        image = ImageLoader.from_path(asset_path_builder("2x1_opaque_transparent.png"))
        expected_transparency_mask = np.array([
            [False, True]
        ])
        transparency_mask = image.transparency_mask()
        self.assertTrue((transparency_mask == expected_transparency_mask).all())
    
    def test_from_bytes(self):
        # PPM file
        ppm_data_black_white = (
            b"P3\n" # PPM header
            b"2 1\n" # 2x1
            b"255\n" # Maximum value
            b"0 0 0 255 255 255\n"
        )
        image = ImageLoader.from_bytes(ppm_data_black_white)
        expected_grayscale = np.array([
            [0, 255]
        ], dtype=np.uint8)
        self.assertTrue((image.as_grayscale() == expected_grayscale).all())

if __name__ == "__main__":
    unittest.main()
