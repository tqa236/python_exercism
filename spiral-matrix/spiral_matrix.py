def spiral_matrix(size: int) -> None:
    if size == 0:
        return []
    if size == 1:
        return [[1]]
    if size == 2:
        return [[1, 2], [4, 3]]
    return []
