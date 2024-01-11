from string import ascii_uppercase


def make_space_pad(length: int) -> str:
    return "".join(" " for _ in range(length))


def make_row(letter: str, center_letter: str) -> str:
    center_pad_length = 2 * (ord(letter) - 65) - 1
    side_pad_length = ord(center_letter) - ord(letter)
    center = "A"
    if letter != "A":
        center = letter + make_space_pad(center_pad_length) + letter
    side_pad = make_space_pad(side_pad_length)
    return side_pad + center + side_pad


def rows(letter: str) -> str:
    upper_part = [
        make_row(row, letter)
        for row in ascii_uppercase[: ascii_uppercase.index(letter) + 1]
    ]
    return upper_part + upper_part[::-1][1:]
