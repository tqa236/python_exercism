def recite(start, take=1):
    def number_to_word(n):
        words = {
            10: "ten",
            9: "nine",
            8: "eight",
            7: "seven",
            6: "six",
            5: "five",
            4: "four",
            3: "three",
            2: "two",
            1: "one",
            0: "no",
        }
        return words[n]

    def generate_verse(bottles):
        plural = "bottles" if bottles != 1 else "bottle"
        next_plural = "bottles" if bottles - 1 != 1 else "bottle"
        verse = [
            f"{number_to_word(bottles).capitalize()} green {plural} hanging on the wall,",
            f"{number_to_word(bottles).capitalize()} green {plural} hanging on the wall,",
            "And if one green bottle should accidentally fall,",
            f"There'll be {number_to_word(bottles - 1)} green {next_plural} hanging on the wall.",
        ]
        return verse

    lyrics = []
    for i in range(start, start - take, -1):
        lyrics.extend(generate_verse(i))
        if i > start - take + 1:
            lyrics.append("")

    return lyrics
