from turtle import pu, goto, pd, setheading, pos, fd, rt, bk, lt

from figures.Figure import Figure


class Three(Figure):
    def _draw(self, d: int):
        for i in range(2):
            fd(d)
            rt(90)
        fd(d)
        for i in range(2):
            bk(d)
            rt(90)
        bk(d)
