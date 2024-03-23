from Config import Config
from figures.Figure import Figure
from recording.record_turtle import fd, rt, pu, lt, dot, pd


class Coma(Figure):
    width = Config.default_width // 8

    def _draw(self, width: int, height: int):
        pu()
        fd(width)
        rt(90)
        fd(height - height // 20)
        rt(30)
        pd()
        fd(height // 10)
