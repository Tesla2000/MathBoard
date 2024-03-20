from turtle import fd, rt, bk, lt

from figures.Figure import Figure


class Six(Figure):
    def _draw(self, width: int, height: int):
        fd(width)
        bk(width)
        rt(90)
        fd(height)
        lt(90)
        fd(width)
        lt(90)
        fd(height // 2)
        lt(90)
        fd(width)
        rt(90)
        fd(height // 2)
