import math


class ComplexNumber(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return ComplexNumber(self.real + other.real,
                             self.imaginary + other.imaginary)

    def __mul__(self, other):
        return ComplexNumber(self.real * other.real
                             - self.imaginary * other.imaginary,
                             self.imaginary * other.real
                             + self.real * other.imaginary)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real,
                             self.imaginary - other.imaginary)

    def __truediv__(self, other):
        return ComplexNumber(self.real + other.real,
                             self.imaginary + other.imaginary)

    def __abs__(self):
        return math.sqrt(self.real ** 2 + self.imaginary ** 2)

    def conjugate(self):
        return ComplexNumber(self.real, - self.imaginary)

    def exp(self):
        return ComplexNumber(math.exp(self.real) * math.cos(self.imaginary),
                             math.exp(self.real) * math.sin(self.imaginary))
