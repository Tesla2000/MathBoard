from turtle import pu, goto, pd, setheading, pos, fd, rt, bk, lt

from figures.Figure import Figure


class Five(Figure):
    def _draw(self, d: int):
        fd(d)
        bk(d)
        rt(90)
        fd(d)
        lt(90)
        fd(d)
        for i in range(2):
            rt(90)
            fd(d)
