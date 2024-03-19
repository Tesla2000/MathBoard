from turtle import pu, pd, fd, rt, bk

from figures.Figure import Figure


class One(Figure):
    def _draw(self, width: int, height: int, border_width: int, border_height: int):
        pu()
        fd(width)
        pd()
        rt(90)
        fd(height)
        bk(height)
        rt(60)
        fd(width // 2)
