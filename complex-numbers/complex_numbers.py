"""Implement a simple complex number class."""
import math


from typing import Union


class ComplexNumber(object):
    """Implement a simple complex number class."""

    def __init__(self, real: Union[int, float], imaginary: Union[float, int]) -> None:
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other: "ComplexNumber") -> bool:
        return self.real == other.real and self.imaginary == other.imaginary

    def __add__(self, other: "ComplexNumber") -> "ComplexNumber":
        return ComplexNumber(self.real + other.real,
                             self.imaginary + other.imaginary)

    def __mul__(self, other: "ComplexNumber") -> "ComplexNumber":
        return ComplexNumber(self.real * other.real
                             - self.imaginary * other.imaginary,
                             self.imaginary * other.real
                             + self.real * other.imaginary)

    def __sub__(self, other: "ComplexNumber") -> "ComplexNumber":
        return ComplexNumber(self.real - other.real,
                             self.imaginary - other.imaginary)

    def __truediv__(self, other: "ComplexNumber") -> "ComplexNumber":
        denominator = other.real ** 2 + other.imaginary ** 2
        return ComplexNumber((self.real * other.real
                              + self.imaginary * other.imaginary)/denominator,
                             (self.imaginary * other.real
                              - self.real * other.imaginary)/denominator)

    def __abs__(self) -> float:
        return math.sqrt(self.real ** 2 + self.imaginary ** 2)

    def conjugate(self) -> "ComplexNumber":
        """Conjugate a complex number."""
        return ComplexNumber(self.real, - self.imaginary)

    def exp(self) -> "ComplexNumber":
        """Calculate the exponential of a complex number."""
        return ComplexNumber(math.exp(self.real) * math.cos(self.imaginary),
                             math.exp(self.real) * math.sin(self.imaginary))

