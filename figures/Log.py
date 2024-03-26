from Config import Config
from figures.Figure import Figure
from figures.Sequence import Sequence
from recording.record_turtle import rt, fd, lt, pos


class Log(Figure):
    border_height = False

    def __init__(self, base: Figure = None, width: int = None, height: int = None):
        super().__init__(width, height)
        self.base = base
        self.base_length = 1
        if isinstance(base, Sequence):
            self.base_length = len(base.figures)

    def _draw(self, width: int, height: int):
        rt(90)
        fd(height)
        lt(90)
        fd(width // (3 + self.base_length))
        lt(90)
        fd(height // 2)
        rt(90)
        fd(width // (3 + self.base_length))
        rt(90)
        fd(height // 2)
        rt(90)
        fd(width // (3 + self.base_length))
        rt(180)
        fd(width // (3 + self.base_length))
        lt(90)
        fd(height // 2)
        rt(90)
        fd(width // (3 + self.base_length))
        rt(90)
        fd(height)
        rt(90)
        fd(width // (3 + self.base_length))
        rt(180)
        fd(width // (3 + self.base_length))
        lt(90)
        fd(height // 2)
        lt(90)
        fd(width // (3 + self.base_length))
        x_coor, y_coor = pos()
        self.base.x_coor = x_coor + width // (3 + self.base_length) + Config.minimal_border_width
        self.base.y_coor = y_coor + height // 4
        self.base.width = width // (3 + self.base_length)
        self.base.height = height // 2
        self.base.draw()





