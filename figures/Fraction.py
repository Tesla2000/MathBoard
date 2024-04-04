from Config import Config
from figures import moveto
from figures.Figure import Figure
from figures.Sequence import Sequence
from recording.record_turtle import pu, pd, fd, rt, lt


class Fraction(Figure):
    def __init__(
        self,
        numerator: Figure,
        denominator: Figure,
        width: int = Config.default_width,
        height: int = Config.default_height,
        numerator_height_factor: float = 0.5,
    ):
        super().__init__(width, height)
        self.numerator_height_factor = numerator_height_factor
        self.numerator = numerator
        self.denominator = denominator

    def _draw(self, width: int, height: int):
        self.numerator.x_coor = self.x_coor
        self.numerator.y_coor = self.y_coor
        if isinstance(self.numerator, Sequence):
            self.numerator.draw(width + Config.minimal_border_width, int(height * self.numerator_height_factor))
        else:
            self.numerator.draw(width, int(height * self.numerator_height_factor))
        moveto(self.x_coor, self.y_coor)
        pu()
        rt(90)
        fd(height // 2)
        pd()
        lt(90)
        fd(width - Config.minimal_border_width)
        self.denominator.x_coor = self.x_coor
        self.denominator.y_coor = (
            self.y_coor - height // 2 - Config.minimal_border_width
        )
        if isinstance(self.denominator, Sequence):
            self.denominator.draw(
                width + Config.minimal_border_width, height - int(height * self.numerator_height_factor)
            )
        else:
            self.denominator.draw(
                width, height - int(height * self.numerator_height_factor)
            )
