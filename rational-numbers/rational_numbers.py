"""Implement a basic ratinal number object."""
from __future__ import division

from math import gcd


class Rational(object):
    """Implement a basic ratinal number object."""

    def __init__(self, numer: int, denom: int) -> None:
        if denom == 0:
            raise ValueError("Denominator cannot be 0")
        if denom < 0:
            numer = numer * -1
        gcd_ = gcd(numer, denom)
        self.numer = numer // gcd_
        self.denom = abs(denom // gcd_)

    def __eq__(self, other: "Rational") -> bool:
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return "{}/{}".format(self.numer, self.denom)

    def __add__(self, other: "Rational") -> "Rational":
        return Rational(
            self.numer * other.denom + self.denom * other.numer,
            self.denom * other.denom,
        )

    def __sub__(self, other: "Rational") -> "Rational":
        return Rational(
            self.numer * other.denom - self.denom * other.numer,
            self.denom * other.denom,
        )

    def __mul__(self, other: "Rational") -> "Rational":
        return Rational(self.numer * other.numer, self.denom * other.denom)

    def __truediv__(self, other: "Rational") -> "Rational":
        return Rational(self.numer * other.denom, self.denom * other.numer)

    def __abs__(self) -> "Rational":
        return Rational(abs(self.numer), self.denom)

    def __pow__(self, power: int) -> "Rational":
        return Rational(self.numer ** power, self.denom ** power)

    def __rpow__(self, base: int) -> float:
        return base ** (self.numer / self.denom)
