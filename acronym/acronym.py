import re


def abbreviate(words: str) -> str:
    word_list = list(filter(None, re.split("[^a-zA-Z']", words)))
    return "".join([x[0].upper() for x in word_list])
