"""Encoder and decoder for run length encoding."""
from itertools import groupby


def decode(string):
    """Decode."""
    counter, result = 1, ""
    for is_digit, group in groupby(string, str.isdigit):
        if is_digit:
            counter = int("".join(group))
        else:
            result = result + counter * next(group) + "".join(group)
    return result


def encode_one_char(char, counter):
    """Encode one character."""
    if counter > 1:
        return str(counter) + char
    return char


def encode(string):
    """Encode."""
    return "".join(encode_one_char(k, len(list(g))) for k, g in groupby(string))
