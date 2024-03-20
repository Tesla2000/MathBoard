from abc import ABC, abstractmethod
from turtle import pu, goto, pd, setheading, pos

from Config import Config


class Figure(ABC):
    def __init__(self, width: int = Config.default_width, height: int = Config.default_height):
        self.width = width
        self.height = height

    def draw(self, width: int = None, height: int = None, border_width: int = None, border_height: int = None):
        if width is None:
            width = self.width
        if height is None:
            height = self.height
        point = pos()
        if border_width is None:
            border_width = max(Config.minimal_border_width, width // 10)
        if border_height is None:
            border_height = max(Config.minimal_border_width, height // 20)
        pd()
        self._draw(width - border_width, height - border_height)
        pu()
        goto(point)
        pd()
        setheading(0)
        pu()

    @abstractmethod
    def _draw(self, width: int, height: int):
        pass

    def __repr__(self):
        return f"{type(self).__name__}"
