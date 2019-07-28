from typing import List


def board(input_board_array: List[str]) -> None:
    if not input_board_array:
        return []
    board_array = [[char for char in line] for line in input_board_array]
    print(board_array)
    row_length = len(board_array)
    column_length = len(board_array[0])
    extended_board_array = board_array
    return input_board_array
