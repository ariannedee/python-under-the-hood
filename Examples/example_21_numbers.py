"""
Dollars class that supports number operations.
  - Limits values to 2 decimal places.
  - Floats get rounded (up or down) when converting to Dollars.
"""
import pytest


class Dollars:
    def __init__(self, dollars=0, cents=0, negative=False):
        try:
            cents = round(float(cents))
            dollars = int(dollars)
        except (ValueError, TypeError):
            raise ValueError(f"Invalid integers {repr(dollars)} or {repr(cents)}")

        if dollars < 0 or cents < 0:
            raise ValueError("Cannot have negative dollar or cent values. Use negative=True.")
        elif cents > 99:
            raise ValueError("Cents must be 99 or less")

        self.negative = negative
        self.dollars = dollars
        self.cents = cents

    def __str__(self):
        as_str = f"${self.dollars}.{self.cents:0>2}"
        if self.negative:
            return '-' + as_str
        return as_str

    def __repr__(self):
        return f"Dollars(dollars={self.dollars}, cents={self.cents}, negative={self.negative})"

    def as_cents(self):
        cents = self.dollars * 100 + self.cents
        if self.negative:
            cents *= -1
        return cents

    @classmethod
    def from_cents(cls, cents):
        try:
            cents = float(cents)
        except ValueError:
            raise ValueError(f"Cannot create dollars from type {type(cents).__name__}")
        if cents < 0:
            negative = True
            cents = abs(cents)
        else:
            negative = False
        cents = round(cents)
        return Dollars(cents // 100, cents % 100, negative)

    def __add__(self, other):
        if isinstance(other, Dollars):
            other_as_cents = other.as_cents()
        elif not isinstance(other, (int, float)):
            raise ValueError(f"Operand '+' not implemented for Dollars and {type(other).__name__}")
        else:
            other_as_cents = other * 100
        total_cents = self.as_cents() + other_as_cents
        return Dollars.from_cents(total_cents)

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        if isinstance(other, Dollars):
            other = other.as_cents()
        elif not isinstance(other, (int, float)):
            raise ValueError(f"Operand '+' not implemented for Dollars and {type(other).__name__}")

        cents = self.as_cents() + other * 100
        self.dollars = int(cents // 100)
        self.cents = int(cents % 100)

        return self


# ----- TEST SUITE -----

def test_creating_dollars_from_cents():
    d1 = Dollars.from_cents(199.5)
    assert d1.dollars == 2
    assert d1.cents == 0
    assert d1.negative is False

    big_negative_float = -100_000_000_000_001
    d2 = Dollars.from_cents(big_negative_float)
    assert d2.dollars == 1_000_000_000_000
    assert d2.cents == 1
    assert d2.negative is True


def test_dollars_as_cents():
    d1 = Dollars()
    assert d1.as_cents() == 0

    d2 = Dollars(3, 33.33)
    assert d2.as_cents() == 333

    d3 = Dollars(1_000_000_000_000, 1, negative=True)
    assert d3.as_cents() == -100_000_000_000_001

    d4 = Dollars('12', '34.56')
    assert d4.as_cents() == 1235


def test_invalid_initialization():
    with pytest.raises(ValueError) as exc_info:
        Dollars(-4)

    assert 'negative' in str(exc_info).lower()

    with pytest.raises(ValueError) as exc_info:
        Dollars(0, 100)

    assert 'cents' in str(exc_info).lower()

    with pytest.raises(ValueError) as exc_info:
        Dollars([], 'bad')

    assert 'invalid integer' in str(exc_info).lower()


def test_dollars_add():
    d1 = Dollars.from_cents(111)
    d2 = Dollars.from_cents(222)
    d3 = d1 + d2
    assert d3.dollars == 3
    assert d3.cents == 33


if __name__ == '__main__':
    pytest.main()
