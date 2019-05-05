from typing import List, Dict

_OUTPUT_FUNCTION_MAP = {}

def output(description):
    def _output_decorator(f):
        _OUTPUT_FUNCTION_MAP[f.__name__] = (f, description)
        return f
    return _output_decorator

_BRAILLE_BASE = 0x2800

def _braille_create_lines(binary_matrix,
                          y_step: int,
                          x_step: int,
                          dot_map: Dict[int, int]) -> List[str]:
    output_lines: List[str] = []
    for y_pos in range(0, len(binary_matrix), y_step):
        output_line: str = ""
        for x_pos in range(0, len(binary_matrix[y_pos]), x_step):
            offset: int = 0
            for y_offset in range(y_step):
                for x_offset in range(x_step):
                    try:
                        if binary_matrix[y_pos + y_offset][x_pos + x_offset]:
                            offset += dot_map[y_offset][x_offset]
                    # This position might not exist, but it's okay.
                    except IndexError:
                        pass
            output_line += chr(_BRAILLE_BASE + offset)
        output_lines.append(output_line)
    return output_lines

# The Unicode braille character has a pattern, that, from the
# base U+2800 (hex), each "dot" can be activated by adding:
# 1   8
# 2  10    (all those in hex)
# 4  20
# 40 80
_BRAILLE_DOT_MAP: List[List[int]] = [
    [0x1, 0x8],
    [0x2, 0x10],
    [0x4, 0x20],
    [0x40, 0x80]
]

def _braille(binary_matrix, height_per_char, blank_substitution=None) -> List[str]:
    braille_text = _braille_create_lines(binary_matrix, height_per_char, 2, _BRAILLE_DOT_MAP)
    if blank_substitution is not None:
        braille_text = [line.replace(chr(_BRAILLE_BASE), blank_substitution) for line in braille_text]
    return braille_text

@output("Braille (3x2 grid)")
def braille_3x2(binary_matrix, blank_substitution=None) -> List[str]:
    return _braille(binary_matrix, 3, blank_substitution)

@output("Braille (4x2 grid)")
def braille_4x2(binary_matrix, blank_substitution=None) -> List[str]:
    return _braille(binary_matrix, 4, blank_substitution)

def output_function(name):
    function, _desc = _OUTPUT_FUNCTION_MAP[name]
    return function

def available_output_functions():
    return list(_OUTPUT_FUNCTION_MAP.items())
