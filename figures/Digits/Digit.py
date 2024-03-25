from abc import ABC

from figures.Figure import Figure


class Digit(Figure, ABC):
    value: int
