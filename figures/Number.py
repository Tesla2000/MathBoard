from abc import ABC
from fractions import Fraction as mathFraction

from Config import Config
from figures.Blank import Blank
from figures.Coma import Coma
from figures.Figure import Figure
from figures.Fraction import Fraction
from figures.Minus import Minus
from figures.Digits.Digit import Digit
from figures.Sequence import Sequence


def _number_to_digits(number: int) -> list[int]:
    digits = []
    while number > 0:
        digit = number % 10
        digits.insert(0, digit)
        number //= 10
    return digits


class Number(Figure, ABC):
    @classmethod
    def from_int(cls, value: int, *args, **kwargs) -> Digit | Sequence:
        if value in range(10):
            return next(
                number for number in Digit.__subclasses__() if number.value == value
            )(*args, **kwargs)
        if value in range(-9, 0):
            return next(
                Sequence(*(Minus(), number()), *args, **kwargs)
                for number in Digit.__subclasses__()
                if number.value == abs(value)
            )
        return Sequence(
            *([Minus()] if value < 0 else []),
            *tuple(cls.from_int(digit) for digit in _number_to_digits(abs(value))),
            *args,
            *kwargs
        )

    @classmethod
    def from_float(cls, value: float, *args, **kwargs) -> Sequence:
        return Sequence(
            *([Minus()] if value < 0 else []),
            *tuple(
                cls.from_int(int(char)) if char != "." else Coma()
                for char in str(value)
            ),
            *args,
            **kwargs
        )

    @classmethod
    def from_fraction(cls, value: mathFraction, *args, **kwargs) -> Fraction | Sequence:
        if len(str(abs(value.numerator))) == len(str(abs(value.denominator))):
            if value.numerator * value.denominator < 0:
                figure = Fraction(
                    cls.from_int(abs(value.numerator)),
                    cls.from_int(abs(value.denominator)),
                )
                figure = Sequence(*(Minus(), figure), *args, **kwargs)
            else:
                figure = Fraction(
                    cls.from_int(abs(value.numerator)),
                    cls.from_int(
                        abs(value.denominator),
                    ),
                    *args,
                    **kwargs
                )
        numerator_length = len(str(abs(value.numerator)))
        denominator_length = len(str(abs(value.denominator)))
        difference = abs(numerator_length - denominator_length)
        blank_width = Config.default_width * difference / 2
        if numerator_length < denominator_length:
            numerator = Sequence(
                *(
                    Blank(width=blank_width),
                    *(
                        cls.from_int(abs(value.numerator)).figures
                        if numerator_length > 1
                        else (cls.from_int(abs(value.numerator)),)
                    ),
                    Blank(width=blank_width),
                )
            )
            if value.numerator * value.denominator < 0:
                figure = Fraction(
                    numerator,
                    cls.from_int(abs(value.denominator)),
                )
                figure = Sequence(*(Minus(), figure), *args, **kwargs)
            else:
                figure = Fraction(
                    numerator,
                    cls.from_int(
                        abs(value.denominator),
                    ),
                    *args,
                    **kwargs
                )
        if numerator_length > denominator_length:
            denominator = Sequence(
                *(
                    Blank(width=blank_width),
                    *(
                        cls.from_int(abs(value.denominator)).figures
                        if denominator_length > 1
                        else (cls.from_int(abs(value.denominator)),)
                    ),
                    Blank(width=blank_width),
                )
            )
            if value.numerator * value.denominator < 0:
                figure = Fraction(
                    cls.from_int(abs(value.numerator)),
                    denominator,
                )
                figure = Sequence(*(Minus(), figure), *args, **kwargs)
            else:
                figure = Fraction(
                    cls.from_int(abs(value.numerator)), denominator, *args, **kwargs
                )
        return figure
