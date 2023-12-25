from __future__ import annotations

import math


class ComplexNumber:
    """Implement a simple complex number class."""

    def __init__(self, real: float | int, imaginary: float | int) -> None:
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other: ComplexNumber) -> bool:
        return self.real == other.real and self.imaginary == other.imaginary

    def __add__(self, other: ComplexNumber | float | int) -> ComplexNumber:
        if isinstance(other, (float, int)):
            return ComplexNumber(self.real + other, self.imaginary)
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __radd__(self, other: ComplexNumber | float | int) -> ComplexNumber:
        return self.__add__(other)

    def __mul__(self, other: ComplexNumber | float | int) -> ComplexNumber:
        if isinstance(other, (float, int)):
            return ComplexNumber(self.real * other, self.imaginary * other)
        return ComplexNumber(
            self.real * other.real - self.imaginary * other.imaginary,
            self.imaginary * other.real + self.real * other.imaginary,
        )

    def __rmul__(self, other: ComplexNumber | float | int) -> ComplexNumber:
        return self.__mul__(other)

    def __sub__(self, other: ComplexNumber | float | int) -> ComplexNumber:
        if isinstance(other, (float, int)):
            return ComplexNumber(self.real - other, self.imaginary)
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    def __rsub__(self, other: ComplexNumber | float | int) -> ComplexNumber:
        if isinstance(other, (float, int)):
            other = ComplexNumber(other, 0)
        return other.__sub__(self)

    def __truediv__(self, other: ComplexNumber | float | int) -> ComplexNumber:
        if isinstance(other, (float, int)):
            return ComplexNumber(self.real / other, self.imaginary / other)
        denominator = other.real**2 + other.imaginary**2
        return ComplexNumber(
            (self.real * other.real + self.imaginary * other.imaginary) / denominator,
            (self.imaginary * other.real - self.real * other.imaginary) / denominator,
        )

    def __rtruediv__(self, other: ComplexNumber | float | int) -> ComplexNumber:
        if isinstance(other, (float, int)):
            other = ComplexNumber(other, 0)
        return other.__truediv__(self)

    def __abs__(self) -> float:
        return math.sqrt(self.real**2 + self.imaginary**2)

    def conjugate(self) -> ComplexNumber:
        """Conjugate a complex number."""
        return ComplexNumber(self.real, -self.imaginary)

    def exp(self) -> ComplexNumber:
        """Calculate the exponential of a complex number."""
        return ComplexNumber(
            math.exp(self.real) * math.cos(self.imaginary),
            math.exp(self.real) * math.sin(self.imaginary),
        )
