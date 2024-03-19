from turtle import fd, rt, bk

from figures.Figure import Figure


class Nine(Figure):
    def _draw(self, width: int, height: int, border_width: int, border_height: int):
        fd(width)
        rt(90)
        fd(height)
        rt(90)
        fd(width)
        bk(width)
        rt(90)
        fd(height // 2)
        rt(-90)
        fd(width)
        rt(90)
        fd(height // 2)
