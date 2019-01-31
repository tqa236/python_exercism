from __future__ import division
from math import gcd


class Rational(object):
    def __init__(self, numer, denom):
        if denom == 0:
            raise ValueError("Denominator cannot be 0")
        if denom < 0:
            numer = numer * -1
        gcd_ = gcd(numer, denom)
        self.numer = numer//gcd_
        self.denom = abs(denom//gcd_)

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        return Rational(self.numer * other.denom + self.denom * other.numer,
                        self.denom * other.denom)

    def __sub__(self, other):
        return Rational(self.numer * other.denom - self.denom * other.numer,
                        self.denom * other.denom)

    def __mul__(self, other):
        return Rational(self.numer*other.numer, self.denom*other.denom)

    def __truediv__(self, other):
        return Rational(self.numer*other.denom, self.denom*other.numer)

    def __abs__(self):
        return Rational(abs(self.numer), self.denom)

    def __pow__(self, power):
        return Rational(self.numer**power, self.denom**power)

    def __rpow__(self, base):
        return base**(self.numer/self.denom)
