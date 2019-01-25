import string


def is_pangram(sentence):
    return set(string.ascii_lowercase).issubset(sentence.lower())
