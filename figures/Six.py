from turtle import pu, goto, pd, setheading, pos, fd, rt, bk, lt

from figures.Figure import Figure


class Six(Figure):
    def _draw(self, d: int):
        fd(d)
        bk(d)
        rt(90)
        fd(d * 2)
        for i in range(3):
            lt(90)
            fd(d)
        rt(90)
        fd(d)
