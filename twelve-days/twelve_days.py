"""Recite the twelve days song."""


from typing import List


def recite_one_verse(verse: int) -> List[str]:
    """Recite a single verse."""
    plural = "and " if verse > 1 else ""
    day_presents = [
        ("first", plural + "a Partridge in a Pear Tree."),
        ("second", "two Turtle Doves, "),
        ("third", "three French Hens, "),
        ("fourth", "four Calling Birds, "),
        ("fifth", "five Gold Rings, "),
        ("sixth", "six Geese-a-Laying, "),
        ("seventh", "seven Swans-a-Swimming, "),
        ("eighth", "eight Maids-a-Milking, "),
        ("ninth", "nine Ladies Dancing, "),
        ("tenth", "ten Lords-a-Leaping, "),
        ("eleventh", "eleven Pipers Piping, "),
        ("twelfth", "twelve Drummers Drumming, "),
    ]
    day = day_presents[verse - 1][0]
    presents = "".join([day_presents[i - 1][1] for i in range(verse, 0, -1)])
    return [f"On the {day} day of Christmas my true love gave to me: " f"{presents}"]


def recite(start_verse: int, end_verse: int) -> List[str]:
    """Recite the twelve days song."""
    return [recite_one_verse(verse)[0] for verse in range(start_verse, end_verse + 1)]
