NUMBERS = {
    "0": [" _ ", "| |", "|_|", "   "],
    "1": ["   ", "  |", "  |", "   "],
    "2": [" _ ", " _|", "|_ ", "   "],
    "3": [" _ ", " _|", " _|", "   "],
    "4": ["   ", "|_|", "  |", "   "],
    "5": [" _ ", "|_ ", " _|", "   "],
    "6": [" _ ", "|_ ", "|_|", "   "],
    "7": [" _ ", "  |", "  |", "   "],
    "8": [" _ ", "|_|", "|_|", "   "],
    "9": [" _ ", "|_|", " _|", "   "],
}


def convert_one_number(number: list[str]) -> str:
    for key in NUMBERS:
        if "\n".join(number) == "\n".join(NUMBERS[key]):
            return key
    return "?"


def convert(input_grid: list[str]) -> None:
    length = len(input_grid[0])
    width = len(input_grid)
    if width % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")
    if length % 3 != 0:
        raise ValueError("Number of input columns is not a multiple of three")
    numbers = [
        [
            [line[j : j + 3] for line in input_grid[i : i + 4]]
            for j in range(0, length, 3)
        ]
        for i in range(0, width, 4)
    ]
    return ",".join(
        ["".join([convert_one_number(number) for number in line]) for line in numbers],
    )
