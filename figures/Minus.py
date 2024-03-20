from turtle import fd, rt, pu, pd, lt, bk

from figures.Figure import Figure


class Minus(Figure):
    def _draw(self, width: int, height: int):
        rt(90)
        pu()
        fd(height // 2)
        pd()
        lt(90)
        fd(width)
