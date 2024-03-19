from turtle import pu, goto, pd, setheading, pos, fd, rt, bk, lt

from figures.Figure import Figure


class Zero(Figure):
    def _draw(self, d: int):
        fd(d)
        rt(90)
        fd(d * 2)
        rt(90)
        fd(d)
        rt(90)
        fd(d * 2)
