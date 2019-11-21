ANIMAL_ACTION = [
    ("fly", "I don't know why she swallowed the fly."),
    ("spider", "It wriggled and jiggled and tickled inside her."),
]


def recite(start_verse: int, end_verse: int) -> None:
    song = [
        [
            f"I know an old lady who swallowed a {ANIMAL_ACTION[i][0]}.",
            f"{ANIMAL_ACTION[i][1]}",
        ]
        for i in range(end_verse - 1, -1, -1)
    ]
    song[-1][-1] = song[-1][-1] + " Perhaps she'll die."
    print(song)
    return [sentence for verse in song for sentence in verse]
