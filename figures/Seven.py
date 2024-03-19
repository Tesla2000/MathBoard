from math import pi, atan, sqrt
from turtle import fd, rt

from figures.Figure import Figure


class Seven(Figure):
    def _draw(self, width: int, height: int, border_width: int, border_height: int):
        fd(width)
        rt(atan(width / height) * 180 / pi + 90)
        fd(sqrt(height ** 2 + width ** 2))
