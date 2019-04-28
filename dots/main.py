from .image import ImageLoader, resize_with_factor
from .threshold import threshold_function
from .output import output_function

from argparse import ArgumentParser
from typing import Callable, Any, List
from pathlib import Path

def create_argument_parser() -> ArgumentParser:
    parser = ArgumentParser()
    parser.add_argument("image_path", type=Path)
    parser.add_argument("--threshold", type=threshold_function, default='otsu')
    parser.add_argument("--output", type=output_function, default='braille_3x2')
    parser.add_argument("--resize-factor", type=float, default=1)
    return parser

def main(image_path: Path,
    resize_factor: float,
    threshold: Callable[[int], Any],
    output: Callable[[Any], List[str]]):
    loader = ImageLoader(image_path)
    grayscale_image = loader.as_grayscale()
    resized_image = resize_with_factor(grayscale_image, resize_factor)
    binary_matrix = threshold(resized_image)
    lines = output(binary_matrix)

    print('\n'.join(lines))

if __name__ == "__main__":
    parser = create_argument_parser()
    args = parser.parse_args()
    main(**vars(args))
