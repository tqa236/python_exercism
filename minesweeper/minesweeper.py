from typing import List


def board(input_board_array: List[str]) -> None:
    if not input_board_array:
        return []
    row_length = [len(row) for row in input_board_array]
    if min(row_length) != max(row_length):
        raise ValueError("Bad-shaped board.")
    invalid_char = [
        char for row in input_board_array for char in row if char not in " *"
    ]
    if invalid_char:
        raise ValueError("Invalid char.")
    column_length = len(input_board_array)
    row_length = len(input_board_array[0])
    extended_board_array = (
        [[" " for i in range(row_length + 2)]]
        + [[" "] + [char for char in row] + [" "] for row in input_board_array]
        + [[" " for i in range(row_length + 2)]]
    )
    for i in range(1, column_length + 1):
        for j in range(1, row_length + 1):
            if extended_board_array[i][j] != "*":
                extended_board_array[i][j] = str(
                    sum(
                        [
                            extended_board_array[ii][jj] == "*"
                            for ii in range(i - 1, i + 2)
                            for jj in range(j - 1, j + 2)
                        ]
                    )
                )
    return ["".join(row[1:-1]).replace("0", " ") for row in extended_board_array[1:-1]]
