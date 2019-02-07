import re


class Phone(object):
    def __init__(self, phone_number):
        self.number = re.sub("\D", "", phone_number)
        if len(self.number) < 10 or len(self.number) > 11:
            raise ValueError("Invalid phone number")
        if len(self.number) == 11 and self.number[0] != '1':
            raise ValueError("Invalid phone number")
