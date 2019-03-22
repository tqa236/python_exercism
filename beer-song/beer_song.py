"""Recite a beer song."""


def recite(start, take=1):
    """Recite a beer song."""
    return [i for verse in range(start, start - take, -1)
            for i in recite_one_verse(verse)][:-1]


def recite_one_verse(verse):
    """Recite one verse."""
    if verse == 0:
        return [f"No more bottles of beer on the wall,"
                f" no more bottles of beer.",
                f"Go to the store and buy some more,"
                f" 99 bottles of beer on the wall.", ""]
    return [f"{bottle_string(verse)} of beer on the wall,"
            f" {bottle_string(verse)} of beer.",
            f"{action_string(verse)}"
            f"{bottle_string(verse - 1)} of beer on the wall.", ""]


def bottle_string(verse):
    """Return the correct bottle string for a verse."""
    if verse > 1:
        return f"{verse} bottles"
    elif verse == 1:
        return f"{verse} bottle"
    return f"no more bottles"


def action_string(verse):
    """Return the correct action for a verse."""
    if verse > 1:
        return f"Take one down and pass it around, "
    return f"Take it down and pass it around, "
