VERSE = [("lay in", "the house that Jack built."), ("ate", "the malt")]


def make_verse(verse):
    return "This is " + VERSE[verse][1]


def recite(start_verse: int, end_verse: int) -> None:
    # return ["This is the house that Jack built."]
    return [make_verse(verse) for verse in range(start_verse - 1, end_verse)]
    return ["This is " + VERSE[start_verse - 1][1]]
