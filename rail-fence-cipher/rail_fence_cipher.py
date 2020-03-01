def encode(message: str, rails: int) -> None:
    encoded_message = ""
    for i in range(rails):
        encoded_message = encoded_message + message[i::rails]
    return encoded_message


def decode(encoded_message: str, rails: int) -> None:
    return encoded_message
