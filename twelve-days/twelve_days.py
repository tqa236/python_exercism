"""Recite the twelve days song."""


def recite(start_verse, end_verse):
    """Recite the twelve days song."""
    presents = [("first", "a Partridge in a Pear Tree."),
                ("second", "two Turtle Doves, ")]
    day = presents[start_verse - 1][0]
    return [f"On the {presents[start_verse - 1][0]} day of Christmas my true love gave to me: {presents[start_verse - 1][1]}"]
