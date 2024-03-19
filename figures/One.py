from turtle import pu, goto, pd, setheading, pos, fd, rt, bk, lt

from figures.Figure import Figure


class One(Figure):
    def _draw(self, d: int):
        pu()
        fd(d)
        pd()
        rt(90)
        fd(d * 2)
        bk(d * 2)
        rt(60)
        fd(d / 2)
