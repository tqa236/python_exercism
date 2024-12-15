"""English - Pig Latin translator."""

VOWELS = "aeiou"


def translate(text: str) -> str:
    """English - Pig Latin translator."""
    return " ".join(translate_one_word(word) for word in text.split())


def translate_one_word(word: str) -> str:
    """Translate one word from English to Pig Latin."""
    if word[:2] in ("xr", "yt"):
        return word + "ay"
    prefix_index = next(
        (index for index, char in enumerate(word) if char in VOWELS), -1
    )
    if word[prefix_index - 1 : prefix_index + 1] == "qu":
        prefix_index = prefix_index + 1
    if prefix_index == -1:
        prefix_index = next(index for index, char in enumerate(word) if char == "y")
    return word[prefix_index:] + word[:prefix_index] + "ay"
