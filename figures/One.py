from Config import Config
from figures.Figure import Figure
from recording.record_turtle import pu, pd, fd, rt, bk


class One(Figure):
    width = Config.default_width // 2

    def _draw(self, width: int, height: int):
        pu()
        fd(width)
        pd()
        rt(90)
        fd(height)
        bk(height)
        rt(60)
        fd(width)
