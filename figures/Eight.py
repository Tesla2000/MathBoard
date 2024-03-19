from turtle import pu, goto, pd, setheading, pos, fd, rt, bk, lt

from figures.Figure import Figure


class Eight(Figure):
    def _draw(self, d: int):
        fd(d)
        rt(90)
        fd(d * 2)
        for i in range(3):
            rt(90)
            fd(d)
        bk(d)
        lt(90)
        fd(d)
