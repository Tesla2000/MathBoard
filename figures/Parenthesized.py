from Config import Config
from figures.Figure import Figure
from recording.record_turtle import fd, rt, pu, pd


class Parenthesized(Figure):

    def __init__(self, inner: Figure, width: int = None, height: int = None):
        super().__init__(width, height)
        self.inner = inner

    def _draw(self, width: int, height: int):
        fd(width // 10)
        pu()
        fd(width - 2 * (width // 10))
        pd()
        fd(width // 10)
        rt(90)
        fd(height)
        rt(90)
        fd(width // 10)
        pu()
        fd(width - 2 * (width // 10))
        pd()
        fd(width // 10)
        rt(90)
        fd(height)
        self.inner.x_coor = self.x_coor + Config.minimal_border_width
        self.inner.y_coor = self.y_coor - Config.minimal_border_width
        self.inner.width = self.width
        self.inner.height = self.height
        self.inner.draw()
