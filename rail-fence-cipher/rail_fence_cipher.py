def make_rails(rails: int, length: int) -> list:
    return [["" for i in range(length)] for j in range(rails)]


def get_next_location(x, y, direction, y_max):
    x = x + 1
    if direction == "down":
        y = y + 1
    if direction == "up":
        y = y - 1
    if y == 0:
        direction = "down"
    if y == y_max:
        direction = "up"
    return x, y, direction


def get_indices(rails: int, length: int):
    indices = []
    x, y, direction = 0, 0, "down"
    for _ in range(length):
        indices.append((x, y))
        x, y, direction = get_next_location(x, y, direction, rails - 1)
    return indices


def fill_rails(message: str, indices: tuple, full_rails: list):
    for i, letter in enumerate(message):
        x, y = indices[i]
        full_rails[y][x] = letter
    return full_rails


def get_message(full_rails: list, indices: list):
    return "".join(full_rails[y][x] for x, y in indices)


def encode(message: str, rails: int) -> None:
    full_rails = make_rails(rails, len(message))
    indices = get_indices(rails, len(message))
    sorted_indices = sorted(indices, key=lambda index: (index[1], index[0]))
    full_rails = fill_rails(message, indices, full_rails)
    return get_message(full_rails, sorted_indices)


def decode(encoded_message: str, rails: int) -> None:
    full_rails = make_rails(rails, len(encoded_message))
    indices = get_indices(rails, len(encoded_message))
    sorted_indices = sorted(indices, key=lambda index: (index[1], index[0]))
    full_rails = fill_rails(encoded_message, sorted_indices, full_rails)
    return get_message(full_rails, indices)
