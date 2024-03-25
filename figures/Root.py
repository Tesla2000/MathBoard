from math import sqrt, sin, radians

from Config import Config
from figures import moveto
from figures.Figure import Figure
from recording.record_turtle import pu, rt, fd, lt, pd, pos, setheading


class Root(Figure):
    def __init__(
        self,
        radical: Figure,
        index: Figure = None,
        width: int = None,
        height: int = None,
    ):
        super().__init__(width, height)
        self.index = index
        self.radical = radical

    def _draw(self, width: int, height: int):
        if self.index is not None:
            self.index.x_coor = self.x_coor
            self.index.y_coor = self.y_coor
            self.index.width = self.height // 4
            self.index.height = self.height // 2
            self.index.draw()
        moveto(self.x_coor, self.y_coor)
        pu()
        rt(90)
        fd(3 * self.height // 4)
        lt(30)
        pd()
        fd(2 * (self.height - (3 * self.height // 4)) // sqrt(3))
        lt(135)
        fd(self.height // sin(radians(75)))
        setheading(0)
        x_coor = pos()[0]
        width = self.width + self.x_coor - x_coor
        fd(width)
        self.radical.x_coor = x_coor + Config.minimal_border_width
        self.radical.y_coor = self.y_coor - Config.minimal_border_width
        self.radical.height = self.height - Config.minimal_border_width
        self.radical.width = width - Config.minimal_border_width
        self.radical.draw()
