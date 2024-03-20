from turtle import pu, pd, fd, rt, bk, lt, position

from Config import Config
from figures import moveto
from figures.Figure import Figure


class Fraction(Figure):
    def __init__(self, numerator: Figure, denominator: Figure, width: int = Config.default_width, height: int = Config.default_height):
        super().__init__(width, height)
        self.numerator = numerator
        self.denominator = denominator

    def _draw(self, width: int, height: int):
        pos = position()
        self.numerator.draw(width, height // 2)
        moveto(*pos)
        pu()
        rt(90)
        fd(height // 2)
        pd()
        lt(90)
        fd(width)
        bk(width)
        pu()
        rt(90)
        fd(height // 20)
        lt(90)
        fd(width // 20)
        pd()
        self.denominator.draw(width, height // 2)
        pass
