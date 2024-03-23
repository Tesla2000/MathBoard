from math import cos, sin, radians
from turtle import color

from Config import Config
from PassedVariables import PassedVariables
from figures.Figure import Figure
from recording.record_turtle import pu, goto, pd


class Emphasize(Figure):

    def __init__(self, inner: Figure, width: int = None, height: int = None):
        super().__init__(width, height)
        self.inner = inner

    def draw(self, width: int = None, height: int = None, border_width: int = None, border_height: int = None):
        self.x_coor = self.inner.x_coor
        self.y_coor = self.inner.y_coor
        self.width = self.inner.width
        self.height = self.inner.height
        super().draw(width, height, border_width, border_height)

    def _draw(self, width: int, height: int):
        color('red')
        self._draw_ellipse(self.inner.width * 3 // 4, self.inner.height * 3 // 4)
        color(Config.color)

    def _draw_ellipse(self, a, b):
        pu()
        goto(self.x_coor + self.width // 2 + a, self.y_coor - self.height // 2)
        pd()
        for i in range(361):
            PassedVariables.record = False
            if i % 90 == 0:
                PassedVariables.record = True
            x = self.x_coor + a * cos(radians(i)) + self.width // 2
            y = self.y_coor + b * sin(radians(i)) - self.height // 2
            goto(x, y)
