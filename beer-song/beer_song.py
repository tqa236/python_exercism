"""Recite a beer song."""

from typing import List


def recite(start: int, take: int = 1) -> List[str]:
    """Recite a beer song."""
    return [
        i for verse in range(start, start - take, -1) for i in recite_one_verse(verse)
    ][:-1]


def recite_one_verse(verse: int) -> List[str]:
    """Recite one verse."""
    if verse == 0:
        return [
            "No more bottles of beer on the wall," " no more bottles of beer.",
            "Go to the store and buy some more," " 99 bottles of beer on the wall.",
            "",
        ]
    return [
        f"{bottle_string(verse)} of beer on the wall,"
        f" {bottle_string(verse)} of beer.",
        f"{action_string(verse)}" f"{bottle_string(verse - 1)} of beer on the wall.",
        "",
    ]


def bottle_string(verse: int) -> str:
    """Return the correct bottle string for a verse."""
    if verse > 1:
        return f"{verse} bottles"
    elif verse == 1:
        return f"{verse} bottle"
    return "no more bottles"


def action_string(verse: int) -> str:
    """Return the correct action for a verse."""
    if verse > 1:
        return "Take one down and pass it around, "
    return "Take it down and pass it around, "
