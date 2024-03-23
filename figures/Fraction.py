from Config import Config
from figures import moveto
from figures.Figure import Figure
from recording.record_turtle import pu, pd, fd, rt, lt


class Fraction(Figure):
    def __init__(self, numerator: Figure, denominator: Figure, width: int = Config.default_width, height: int = Config.default_height):
        super().__init__(width, height)
        self.numerator = numerator
        self.denominator = denominator

    def _draw(self, width: int, height: int):
        self.numerator.x_coor = self.x_coor
        self.numerator.y_coor = self.y_coor
        self.numerator.draw(width, height // 2)
        moveto(self.x_coor, self.y_coor)
        pu()
        rt(90)
        fd(height // 2)
        pd()
        lt(90)
        fd(width - Config.minimal_border_width)
        self.denominator.x_coor = self.x_coor
        self.denominator.y_coor = self.y_coor - height // 2 - Config.minimal_border_width
        self.denominator.draw(width, height // 2)
