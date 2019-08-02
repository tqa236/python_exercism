import math
import re


def cipher_text(plain_text: str) -> None:
    pattern = re.compile(r"[\W_]+", re.UNICODE)
    clean_text = pattern.sub("", plain_text.lower())
    cipher_length = math.ceil(math.sqrt(len(clean_text)))
    clean_text = clean_text + "*" * (cipher_length ** 2 - len(clean_text))
    ciphered_text = " ".join(
        [clean_text[i : i + 3] for i in range(0, len(clean_text), 3)]
    )
    # if len(clean_text) < cipher_length**2:
    print(ciphered_text)
    return clean_text
