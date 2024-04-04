from abc import ABC

from Config import Config
from figures.Blank import Blank
from figures.Coma import Coma
from figures.Digits.Digit import Digit
from figures.Digits.One import One
from figures.Figure import Figure
from figures.Fraction import Fraction
from figures.Minus import Minus
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
        if value == 18:
            pass
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
    def from_fraction(cls, numerator: int, denominator: int, *args, **kwargs) -> Fraction | Sequence:
        if len(str(abs(numerator))) == len(str(abs(denominator))):
            if numerator * denominator < 0:
                figure = Fraction(
                    cls.from_int(abs(numerator))
                    if numerator != 1
                    else One(centered=True),
                    cls.from_int(abs(denominator))
                    if denominator != 1
                    else One(centered=True),
                )
                figure = Sequence(*(Minus(), figure), *args, **kwargs)
            else:
                figure = Fraction(
                    cls.from_int(abs(numerator))
                    if numerator != 1
                    else One(centered=True),
                    cls.from_int(abs(denominator))
                    if denominator != 1
                    else One(centered=True),
                    *args,
                    **kwargs
                )
        numerator_length = len(str(abs(numerator)))
        denominator_length = len(str(abs(denominator)))
        difference = abs(numerator_length - denominator_length)
        blank_width = Config.default_width * difference // 2
        if numerator_length < denominator_length:
            sequence_numerator = Sequence(
                *(
                    Blank(width=blank_width),
                    *(
                        cls.from_int(abs(numerator)).figures
                        if numerator_length > 1
                        else (
                            cls.from_int(abs(numerator))
                            if numerator != 1
                            else One(centered=True),
                        )
                    ),
                    Blank(width=blank_width),
                )
            )
            if numerator * denominator < 0:
                figure = Fraction(
                    sequence_numerator,
                    cls.from_int(abs(denominator))
                    if denominator != 1
                    else One(centered=True),
                )
                figure = Sequence(*(Minus(), figure), *args, **kwargs)
            else:
                figure = Fraction(
                    sequence_numerator,
                    cls.from_int(
                        abs(denominator),
                    ),
                    *args,
                    **kwargs
                )
        if numerator_length > denominator_length:
            sequence_denominator = Sequence(
                *(
                    Blank(width=blank_width),
                    *(
                        cls.from_int(abs(denominator)).figures
                        if denominator_length > 1
                        else (
                            cls.from_int(abs(denominator))
                            if denominator != 1
                            else One(centered=True),
                        )
                    ),
                    Blank(width=blank_width),
                )
            )
            if numerator * denominator < 0:
                figure = Fraction(
                    cls.from_int(abs(numerator))
                    if numerator != 1
                    else One(centered=True),
                    sequence_denominator,
                )
                figure = Sequence(*(Minus(), figure), *args, **kwargs)
            else:
                figure = Fraction(
                    cls.from_int(abs(numerator))
                    if numerator != 1
                    else One(centered=True),
                    sequence_denominator,
                    *args,
                    **kwargs
                )
        return figure
