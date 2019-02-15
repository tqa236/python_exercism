"""Check if a sentence is a pangram."""
import string


def is_pangram(sentence):
    """Check if a sentence is a pangram."""
    return set(string.ascii_lowercase).issubset(sentence.lower())
