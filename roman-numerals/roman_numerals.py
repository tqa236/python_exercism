"""Convert a number to roman numerals."""


def roman(number: int) -> None:
    """Convert a number to roman numerals."""
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    roman_number = ""
    i = 0
    while number > 0:
        for _ in range(number // val[i]):
            roman_number = roman_number + syb[i]
            number = number - val[i]
        i += 1
    return roman_number
