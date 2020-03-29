"""Refactor the food chain song."""

ANIMAL_ACTIONS = [
    ("fly", "I don't know why she swallowed the fly. Perhaps she'll die."),
    ("spider", "It wriggled and jiggled and tickled inside her."),
    ("bird", "How absurd to swallow a bird!"),
    ("cat", "Imagine that, to swallow a cat!"),
    ("dog", "What a hog, to swallow a dog!"),
    ("goat", "Just opened her throat and swallowed a goat!"),
    ("cow", "I don't know how she swallowed a cow!"),
    ("horse", "She's dead, of course!"),
]


def recite(start_verse: int, end_verse: int) -> None:
    song = []
    for i in range(start_verse, end_verse):
        song = song + recite_one_verse(i)
        song.append("")
    song = song + recite_one_verse(end_verse)
    return song


def recite_one_verse(verse: int):
    lyrics = []
    for i in range(verse - 1, -1, -1):
        if i == verse - 1:
            lyrics.append(f"I know an old lady who swallowed a {ANIMAL_ACTIONS[i][0]}.")
        elif i == 1:
            lyrics.append(
                f"She swallowed the {ANIMAL_ACTIONS[i+1][0]} to catch the {ANIMAL_ACTIONS[i][0]} that wriggled and jiggled and tickled inside her."
            )
        else:
            lyrics.append(
                f"She swallowed the {ANIMAL_ACTIONS[i+1][0]} to catch the {ANIMAL_ACTIONS[i][0]}."
            )
        if i == verse - 1 or i == 0:
            lyrics.append(f"{ANIMAL_ACTIONS[i][1]}")
        if i == len(ANIMAL_ACTIONS) - 1:
            break
    return lyrics
