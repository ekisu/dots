from typing import List

def braille_3x2(binary_matrix) -> List[str]:
    # The Unicode braille character has a pattern, that, from the
    # base U+2800 (hex), each "dot" can be activated by adding:
    # 1   8
    # 2  10    (all those in hex)
    # 4  20
    dot_map: List[List[int]] = [
        [0x1, 0x8],
        [0x2, 0x10],
        [0x4, 0x20]
    ]

    output_lines: List[str] = []
    for y_pos in range(0, len(binary_matrix), 3):
        output_line: str = ""
        for x_pos in range(0, len(binary_matrix[y_pos]), 2):
            offset: int = 0
            for y_offset in range(3):
                for x_offset in range(2):
                    try:
                        if binary_matrix[y_pos + y_offset][x_pos + x_offset]:
                            offset += dot_map[y_offset][x_offset]
                    # This position might not exist, but it's okay.
                    except IndexError:
                        pass
            output_line += chr(0x2800 + offset)
        output_lines.append(output_line)
    return output_lines

_OUTPUT_FUNCTION_MAP = {
    'braille_3x2': braille_3x2,
}

def output_function(name):
    return _OUTPUT_FUNCTION_MAP[name]