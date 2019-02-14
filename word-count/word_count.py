import re


def word_count(phrase):
    phrase = re.sub(r"(\' | \')", " ", phrase)
    words = list(filter(None, re.split('[^a-zA-Z0-9\']', phrase.lower())))
    return {x: words.count(x) for x in set(words)}
