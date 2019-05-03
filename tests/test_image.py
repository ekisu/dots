import unittest
from dots.image import ImageLoader
from pathlib import Path
import numpy as np

def asset_path_builder(sub_path: Path) -> Path:
    assets_folder = Path(__file__).parent
    return assets_folder.joinpath(Path("assets"), sub_path)

class TestImageLoader(unittest.TestCase):
    def test_transparency_mask(self):
        image = ImageLoader(asset_path_builder("2x1_transparency_test.png"))
        expected_transparency_mask = np.array([
            [False, True]
        ])
        transparency_mask = image.transparency_mask()
        self.assertTrue((transparency_mask == expected_transparency_mask).all())

if __name__ == "__main__":
    unittest.main()
