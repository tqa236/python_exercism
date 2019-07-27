"""Pronounce a number in English."""

from typing import Union

NUMBERS_20_90 = [
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety",
]


NUMBERS_0_19 = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
]


NUMBERS_DICT = {
    100: "hundred",
    1000: "thousand",
    1000000: "million",
    1000000000: "billion",
    10 ** 12: "trillion",
}


def say(number: Union[float, int]) -> None:
    """Pronounce a number in English."""
    if number < 0:
        raise ValueError("Number must be a positive integer.")
    if number >= 1e12:
        raise ValueError("Number too large.")

    number = int(number)
    if number < 20:
        return NUMBERS_0_19[number]
    if number < 100:
        return NUMBERS_20_90[number // 10 - 2] + (
            "" if number % 10 == 0 else "-" + NUMBERS_0_19[number % 10]
        )

    maxkey = max([key for key in NUMBERS_DICT if key <= number])
    return (
        say(number // maxkey)
        + " "
        + NUMBERS_DICT[maxkey]
        + (
            ""
            if number % maxkey == 0
            else " " + say(number % maxkey)
            if maxkey > 100
            else " and " + say(number % maxkey)
        )
    )
