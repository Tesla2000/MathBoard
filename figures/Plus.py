from Config import Config
from recording.record_turtle import fd, rt, pu, pd, lt, bk

from figures.Figure import Figure


class Plus(Figure):
    width = Config.default_width // 2

    def _draw(self, width: int, height: int):
        rt(90)
        pu()
        fd(height // 2)
        pd()
        lt(90)
        fd(width)
        bk(width // 2)
        lt(90)
        fd(height // 4)
        bk(height // 2)
