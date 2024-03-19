from turtle import pu, goto, pd, setheading, pos, fd, rt, bk, lt

from figures.Figure import Figure


class Four(Figure):
    def _draw(self, d: int):
        rt(90)
        fd(d)
        for i in range(2):
            lt(90)
            fd(d)
        bk(d * 2)
        pu()
