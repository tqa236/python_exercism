def spiral_matrix(size: int) -> None:
    if size == 0:
        return []
    # matrix = [[[None] for i in range(size)] for j in range(size)]
    # i = j = 0
    # direction = "left"
    # for value in range(size ** 2):
    #     matrix[j][i] = value
    #     if direction == "left":
    #         if i < size - 1:
    #             i = i + 1
    #         else:
    #             j = j + 1
    #             direction = "down"
    #     elif direction == "down":
    #         if j < size - 1:
    #             j = j + 1
    #         else:
    #             i = i - 1
    #             direction = "right"
    #     elif direction == "right":
    #         if i > 0:
    #             i = i - 1
    #         else:
    #             j = j - 1
    #             direction = "up"
    #     elif direction == "up":
    #         if j > 0:
    #             j = j + 1
    #         else:
    #             i = i - 1
    #             direction = "right"
    # return matrix
