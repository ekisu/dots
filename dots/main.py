from .image import ImageLoader, resize_with_factor
from .threshold import threshold_function
from .output import output_function

from argparse import ArgumentParser
from typing import Callable, Any, List, Dict, Tuple
from pathlib import Path
from ast import literal_eval

import numpy as np

def function_args(args_string: str) -> Tuple[List[Any], Dict[str, Any]]:
    args: List[Any] = []
    kwargs: Dict[str, Any] = {}

    for arg in args_string.split(','):
        if arg == '': continue
        
        if '=' in arg:
            [k, v] = arg.split('=')
            kwargs[k] = literal_eval(v)
        else:
            args.append(literal_eval(arg))
    
    return args, kwargs

def create_argument_parser() -> ArgumentParser:
    parser = ArgumentParser()
    parser.add_argument("image_path", type=Path)
    parser.add_argument("--threshold", type=threshold_function, default='adaptive_gaussian')
    parser.add_argument("--threshold-args", type=function_args, default='')
    parser.add_argument("--output", type=output_function, default='braille_3x2')
    parser.add_argument("--invert", action='store_true', default=False)
    parser.add_argument("--resize-factor", type=float, default=1)
    return parser

def main(image_path: Path,
    resize_factor: float,
    threshold: Callable[[int], Any],
    threshold_args: Tuple[List[Any], Dict[str, Any]],
    invert: bool,
    output: Callable[[Any], List[str]]):
    loader = ImageLoader(image_path)
    grayscale_image = loader.as_grayscale()
    resized_image = resize_with_factor(grayscale_image, resize_factor)
    t_args, t_kwargs = threshold_args
    binary_matrix = threshold(resized_image, *t_args, **t_kwargs)
    if invert:
        binary_matrix = np.invert(binary_matrix)
    lines = output(binary_matrix)

    print('\n'.join(lines))

if __name__ == "__main__":
    parser = create_argument_parser()
    args = parser.parse_args()
    main(**vars(args))
