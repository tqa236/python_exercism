COLORS = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9,
}
PREFIXES = {0: "", 3: "kilo", 6: "mega", 9: "giga"}


def label(colors):
    resistance = (COLORS[colors[0]] * 10 + COLORS[colors[1]]) * 10 ** COLORS[colors[2]]
    magnitude = 0
    while resistance >= 1000:
        resistance = resistance // 1000
        magnitude += 3
    resistance_string = f"{resistance} {PREFIXES[magnitude]}ohms"
    return resistance_string
