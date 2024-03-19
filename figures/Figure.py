from abc import ABC, abstractmethod
from turtle import pu, goto, pd, setheading, pos


class Figure(ABC):
    def draw(self, d: int = 50):
        point = pos()
        self._draw(d)
        pu()
        goto(point)
        pd()
        setheading(0)

    @abstractmethod
    def _draw(self, d: int):
        pass
