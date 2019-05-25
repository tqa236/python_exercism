"""Transform legacy to new data format."""


def transform(legacy_data):
    """Transform legacy to new data format."""
    return {
        letter.lower(): score
        for score, letters in legacy_data.items()
        for letter in letters
    }
