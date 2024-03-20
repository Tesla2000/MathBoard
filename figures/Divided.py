from math import sqrt
from turtle import fd, rt, pu, pd, lt, bk, Screen, getscreen, dot

from figures.Figure import Figure


class Divided(Figure):
    def _draw(self, width: int, height: int):
        rt(90)
        pu()
        fd(height // 2)
        pd()
        lt(90)
        fd(width)
        bk(width // 2)
        pu()
        rt(90)
        fd(height // 4)
        dot()
        rt(180)
        fd(height // 2)
        dot()
