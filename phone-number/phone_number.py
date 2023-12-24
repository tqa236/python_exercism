import string


class PhoneNumber(object):
    def __init__(self, phone_number: str) -> None:
        self.number = self.valid_phone_number(phone_number)
        self.area_code = self.number[:3]

    def pretty(self) -> str:
        return f"({self.area_code})-{self.number[3:6]}-{self.number[6:]}"

    def valid_phone_number(self, phone_number):
        number = (
            phone_number.replace(" ", "")
            .replace("+", "")
            .replace("(", "")
            .replace(")", "")
            .replace(".", "")
            .replace("-", "")
        )
        if any(digit.isalpha() for digit in number):
            raise ValueError("letters not permitted")
        if any(digit in string.punctuation for digit in number):
            raise ValueError("punctuations not permitted")
        if len(number) < 10:
            raise ValueError("must not be fewer than 10 digits")
        if len(number) > 11:
            raise ValueError("must not be greater than 11 digits")
        if len(number) == 11 and number[0] != "1":
            raise ValueError("11 digits must start with 1")
        number = number[-10:]
        if number[0] == "0":
            raise ValueError("area code cannot start with zero")
        if number[0] == "1":
            raise ValueError("area code cannot start with one")
        if number[3] == "0":
            raise ValueError("exchange code cannot start with zero")
        if number[3] == "1":
            raise ValueError("exchange code cannot start with one")
        return number
