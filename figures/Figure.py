from abc import ABC, abstractmethod
from turtle import pu, goto, pd, setheading, pos, fd


class Figure(ABC):

    def draw(self, width: int, height: int = 50, border_width: int = None, border_height: int = None):
        point = pos()
        pu()
        if border_width is None:
            border_width = max(1, width // 20)
        if border_height is None:
            border_height = max(1, height // 20)
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
