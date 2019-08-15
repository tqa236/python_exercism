"""Recite a song."""

VERSE = [
    ("lay in", " the house that Jack built."),
    ("ate", " the malt"),
    ("killed", " the rat"),
    ("worried", " the cat"),
    ("tossed", " the dog"),
    ("milked", " the cow with the crumpled horn"),
    ("kissed", " the maiden all forlorn"),
    ("married", " the man all tattered and torn"),
    ("woke", " the priest all shaven and shorn"),
    ("kept", " the rooster that crowed in the morn"),
    ("belonged to", " the farmer sowing his corn"),
    ("", " the horse and the hound and the horn"),
]


def make_verse(verse: int) -> str:
    """Make one verse."""
    return (
        "This is"
        + "".join(VERSE[i][1] + " that " + VERSE[i - 1][0] for i in range(verse, 0, -1))
        + VERSE[0][1]
    )


def recite(start_verse: int, end_verse: int) -> None:
    """Recite all verses."""
    return [make_verse(verse) for verse in range(start_verse - 1, end_verse)]
