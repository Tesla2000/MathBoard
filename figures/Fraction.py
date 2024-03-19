from turtle import pu, pd, fd, rt, bk, lt

from figures import moveto
from figures.Figure import Figure


class Fraction(Figure):
    def __init__(self, numerator: Figure, denominator: Figure, x_coordinate: int = None, y_coordinate: int = None):
        super().__init__(x_coordinate, y_coordinate)
        self.numerator = numerator
        self.denominator = denominator

    def _draw(self, width: int, height: int, border_width: int, border_height: int):
        self.numerator.draw(width, height // 2)
        moveto(self.x_coordinate, self.y_coordinate)
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
