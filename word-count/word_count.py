"""Count the number of words in a phrase."""
import re
from collections import Counter


def word_count(phrase):
    """Count the number of words in a phrase."""
    phrase = re.sub(r"(\' | \')", " ", phrase.lower())
    return Counter(item for item in re.split('[^a-zA-Z0-9\']', phrase) if item)
