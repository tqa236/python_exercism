def tick(matrix):
    if not matrix:
        return []

    rows = len(matrix)
    cols = len(matrix[0])
    next_generation = [[0 for _ in range(cols)] for _ in range(rows)]

    for row in range(rows):
        for col in range(cols):
            live_neighbors = 0

            for row_offset in (-1, 0, 1):
                for col_offset in (-1, 0, 1):
                    if row_offset == 0 and col_offset == 0:
                        continue

                    neighbor_row = row + row_offset
                    neighbor_col = col + col_offset

                    if 0 <= neighbor_row < rows and 0 <= neighbor_col < cols:
                        live_neighbors += matrix[neighbor_row][neighbor_col]

            if matrix[row][col] == 1:
                next_generation[row][col] = 1 if live_neighbors in (2, 3) else 0
            else:
                next_generation[row][col] = 1 if live_neighbors == 3 else 0

    return next_generation
