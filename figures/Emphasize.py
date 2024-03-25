from turtle import color as c, width as w

from Config import Config
from figures.Figure import Figure
from recording.record_turtle import fd, rt


class Emphasize(Figure):
    def __init__(
        self, inner: Figure, width: int = None, height: int = None, color: str = "red"
    ):
        super().__init__(width, height)
        self.inner = inner
        self.color = color

    def draw(
        self,
        width: int = None,
        height: int = None,
        border_width: int = None,
        border_height: int = None,
    ):
        self.x_coor = self.inner.x_coor - Config.line_width
        self.y_coor = self.inner.y_coor + Config.line_width
        self.width = self.inner.width
        self.height = self.inner.height
        w(1)
        super().draw(width, height, border_width, border_height)
        w(Config.line_width)

    def _draw(self, width: int, height: int):
        c(self.color)
        self._draw_rectangle(width + 2 * Config.line_width, height + 2 * Config.line_width)
        c(Config.color)

    def _draw_rectangle(self, width: int, height: int):
        for _ in range(2):
            fd(width)
            rt(90)
            fd(height)
            rt(90)
