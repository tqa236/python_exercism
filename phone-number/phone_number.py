import re


class Phone(object):
    def __init__(self, phone_number):
        self.number = self.valid_phone_number(phone_number)
        self.area_code = self.number[:3]

    def pretty(self):
        return f"({self.area_code}) {self.number[3:6]}-{self.number[6:]}"

    def valid_phone_number(self, phone_number):
        number = re.sub("\D", "", phone_number)
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
