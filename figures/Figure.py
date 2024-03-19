from abc import ABC, abstractmethod
from turtle import pu, goto, pd, setheading, pos, fd, rt, lt

from Config import Config


class Figure(ABC):
    def __init__(self, x_coordinate: int = None, y_coordinate: int = None):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    def draw(self, width: int, height: int = 50, border_width: int = None, border_height: int = None):
        point = pos()
        pu()
        if border_width is None:
            border_width = max(Config.minimal_border_width, width // 20)
        if border_height is None:
            border_height = max(Config.minimal_border_width, height // 20)
        fd(border_width)
        pd()
        self._draw(width - 2 * border_width, height - 2 * border_height, border_width, border_height)
        pu()
        goto(point)
        pd()
        setheading(0)

    @abstractmethod
    def _draw(self, width: int, height: int, border_width: int, border_height: int):
        pass
