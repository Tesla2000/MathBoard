from math import sqrt
from recording.record_turtle import fd, rt, pu, pd, lt, bk

from figures.Figure import Figure


class X(Figure):
    def _draw(self, width: int, height: int):
        rt(90)
        pu()
        fd(height // 4)
        pd()
        lt(45)
        fd(sqrt(width ** 2 + ((height // 2) ** 2)))
        bk(sqrt(width ** 2 + ((height // 2) ** 2)) // 2)
        lt(90)
        fd(sqrt(width ** 2 + ((height // 2) ** 2)) // 2)
        bk(sqrt(width ** 2 + ((height // 2) ** 2)))
