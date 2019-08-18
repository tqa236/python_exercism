"""A simple crypto square encoder."""
import math
import re


def cipher_text(plain_text: str) -> None:
    """Encode."""
    if not plain_text:
        return ""
    pattern = re.compile(r"[\W_]+", re.UNICODE)
    clean_text = pattern.sub("", plain_text.lower())

    sqr = math.sqrt(len(clean_text))
    rows = math.ceil(sqr)
    columns = round(sqr)
    return " ".join(
        f"{row:<{columns}}" for row in (clean_text[i::rows] for i in range(rows))
    )
