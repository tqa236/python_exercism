"""Verify if a number is a valid phone number."""
import re


class Phone(object):
    """Verify if a number is a valid phone number."""

    def __init__(self, phone_number: str) -> None:
        self.number = valid_phone_number(phone_number)
        self.area_code = self.number[:3]

    def pretty(self) -> str:
        """Pretify a phone number."""
        return f"({self.area_code}) {self.number[3:6]}-{self.number[6:]}"


def valid_phone_number(phone_number: str) -> str:
    """Verify if a number is a valid phone number."""
    number = re.sub(r"\D", "", phone_number)
    if len(number) < 10 or len(number) > 11:
        raise ValueError("Invalid phone number")
    if len(number) == 11 and number[0] != '1':
        raise ValueError("Invalid phone number")
    number = number[-10:]
    if number[0] in '01':
        raise ValueError("Invalid area code")
    if number[3] in '01':
        raise ValueError("Invalid exchange code")
    return number
