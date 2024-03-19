from turtle import pu, goto, pd, setheading, pos, fd, rt, bk, lt

from figures.Figure import Figure


class Two(Figure):
    def _draw(self, d: int):
        fd(d)
        rt(90)
        fd(d)
        lt(90)
        for i in range(2):
            bk(d)
            lt(90)
        bk(d)
