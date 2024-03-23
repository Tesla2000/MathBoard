from Config import Config
from figures.Figure import Figure
from recording.record_turtle import fd, rt, pu, lt, dot


class Times(Figure):
    width = Config.default_width // 10

    def _draw(self, width: int, height: int):
        rt(90)
        pu()
        fd(height // 2)
        lt(90)
        fd(width // 2)
        dot()
