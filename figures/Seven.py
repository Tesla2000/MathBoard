from turtle import pu, goto, pd, setheading, pos, fd, rt, bk, lt

from figures.Figure import Figure


class Seven(Figure):
    def _draw(self, d: int):
        fd(d)
        rt(90)
        fd(d * 2)
        bk(d * 2)
        lt(90)
        bk(d)
