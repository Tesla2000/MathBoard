from Config import Config
from recording.record_turtle import fd, rt, pu, pd, lt

from figures.Figure import Figure


class Equals(Figure):
    def _draw(self, width: int, height: int):
        rt(90)
        pu()
        fd(3 * height // 8)
        pd()
        lt(90)
        fd(width - Config.minimal_border_width)
        pu()
        rt(90)
        fd(height // 4)
        rt(90)
        pd()
        fd(width - Config.minimal_border_width)
