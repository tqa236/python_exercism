from string import ascii_uppercase, digits
from random import choice


class Robot(object):
    def __init__(self):
        self.name = self.generate_name()
        self.used_name = [self.name]

    def reset(self):
        while self.name in self.generate_name():
            self.name = self.generate_name()
            self.used_name.append(self.name)

    def generate_name(self):
        return ''.join([choice(ascii_uppercase)
                        for i in range(2)] +
                       [choice(digits) for i in range(3)])
