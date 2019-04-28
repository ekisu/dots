from typing import List, Dict

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
            output_line += chr(0x2800 + offset)
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

def braille_3x2(binary_matrix) -> List[str]:
    return _braille_create_lines(binary_matrix, 3, 2, _BRAILLE_DOT_MAP)

def braille_4x2(binary_matrix) -> List[str]:
    return _braille_create_lines(binary_matrix, 4, 2, _BRAILLE_DOT_MAP)

_OUTPUT_FUNCTION_MAP = {
    'braille_3x2': braille_3x2,
    'braille_4x2': braille_4x2
}

def output_function(name):
    return _OUTPUT_FUNCTION_MAP[name]