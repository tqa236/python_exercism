def saddle_points(matrix: list[list[int]]) -> set[tuple[int, int]]:
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise ValueError("irregular matrix")
    max_row = [max(row) for row in matrix]
    min_col = [min(col) for col in zip(*matrix, strict=False)]
    points = set(
        (nr + 1, nc + 1)
        for nr, row in enumerate(max_row)
        for nc, col in enumerate(min_col)
        if row == col
    )
    return [{"row": point[0], "column": point[1]} for point in points]
