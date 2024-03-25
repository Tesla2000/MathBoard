from abc import ABC
from typing import Self

from ..Figure import Figure
from ..Minus import Minus
from ..Sequence import Sequence


def _number_to_digits(number: int) -> list[int]:
    digits = []
    while number > 0:
        digit = number % 10
        digits.insert(0, digit)
        number //= 10
    return digits


class Number(Figure, ABC):
    value: int

    @classmethod
    def from_int(cls, value: int, *args, **kwargs) -> Self:
        if value in range(10):
            return next(number for number in Number.__subclasses__() if number.value == value)(*args, **kwargs)
        return Sequence(*([Minus(*args, *kwargs)] if value < 0 else []), *tuple(cls.from_int(digit, *args, **kwargs) for digit in _number_to_digits(value)))

