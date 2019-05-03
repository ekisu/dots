from .image import ImageLoader, resize_with_factor
from .threshold import threshold_function
from .output import output_function

from argparse import ArgumentParser
from typing import Callable, Any, List, Dict, Tuple
from pathlib import Path
from ast import literal_eval

import numpy as np

FunctionArgs = Tuple[List[Any], Dict[str, Any]]

def function_args(args_string: str) -> FunctionArgs:
    def _parse_value(v):
        try:
            return literal_eval(v)
        except:
            return v
    
    args: List[Any] = []
    kwargs: Dict[str, Any] = {}

    for arg in args_string.split(','):
        if arg == '': continue
        
        if '=' in arg:
            [k, v] = arg.split('=')
            kwargs[k] = _parse_value(v)
        else:
            args.append(_parse_value(v))
    
    return args, kwargs

def create_argument_parser() -> ArgumentParser:
    parser = ArgumentParser()
    parser.add_argument("image_path", type=Path, help="path to the image")
    parser.add_argument("--threshold", type=threshold_function, default='adaptive_gaussian',
                        help="function used to binarize the image. can be one of: simple, otsu, adaptive_gaussian")
    parser.add_argument("--threshold-args", type=function_args, default='',
                        help="comma-separated arguments to the threshold function. k=v pairs will be passed as kwargs; other values as args.")
    parser.add_argument("--output", type=output_function, default='braille_3x2',
                        help="function used to output the binarized matrix. can be one of: braille_3x2, braille_4x2")
    parser.add_argument("--output-args", type=function_args, default='',
                        help="comma-separated arguments to the output function. k=v pairs will be passed as kwargs; other values as args.")
    parser.add_argument("--invert", action='store_true',
                        help="whether to invert the colors on the output or not.")
    parser.add_argument("--no-transparency-mask", action='store_true',
                        help="don't always emit transparent pixels as spaces.")
    parser.add_argument("--resize-factor", type=float, default=1,
                        help="the factor which the image will be resized, defaults to 1")
    return parser

def main(image_path: Path,
    resize_factor: float,
    threshold: Callable[[int], Any],
    threshold_args: FunctionArgs,
    invert: bool,
    no_transparency_mask: bool,
    output: Callable[[Any], List[str]],
    output_args: FunctionArgs):
    loader = ImageLoader(image_path)
    loader.resize_with_factor(resize_factor)

    grayscale_image = loader.as_grayscale()
    
    transparency_mask = loader.transparency_mask()

    t_args, t_kwargs = threshold_args
    binary_matrix = threshold(grayscale_image, *t_args, **t_kwargs)

    if invert:
        binary_matrix = np.invert(binary_matrix)
    
    if not no_transparency_mask:
        binary_matrix = np.logical_and(binary_matrix, transparency_mask)
    
    o_args, o_kwargs = output_args
    lines = output(binary_matrix, *o_args, **o_kwargs)

    print('\n'.join(lines))

if __name__ == "__main__":
    parser = create_argument_parser()
    args = parser.parse_args()
    main(**vars(args))
