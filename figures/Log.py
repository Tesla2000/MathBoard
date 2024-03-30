from Config import Config
from figures.Figure import Figure
from figures.Sequence import Sequence
from recording.record_turtle import rt, fd, lt, pos


class Log(Figure):
    border_height = False

    def __init__(
        self,
        base: Figure = None,
        width: int = None,
        height: int = None,
        base_length_factor: float = None,
        base_height_factor: float = 0.5,
    ):
        super().__init__(width, height)
        self.base = base
        self.base_length_factor = base_length_factor
        self.base_height_factor = base_height_factor
        if self.base_length_factor is None:
            if isinstance(base, Sequence):
                self.base_length_factor = 1 - (
                    len(base.figures) // (3 + len(base.figures))
                )
            else:
                self.base_length_factor = 0.75

    def _draw(self, width: int, height: int):
        rt(90)
        fd(height)
        lt(90)
        fd(self.base_length_factor * width // 3)
        lt(90)
        fd(height // 2)
        rt(90)
        fd(self.base_length_factor * width // 3)
        rt(90)
        fd(height // 2)
        rt(90)
        fd(self.base_length_factor * width // 3)
        rt(180)
        fd(self.base_length_factor * width // 3)
        lt(90)
        fd(height // 2)
        rt(90)
        fd(self.base_length_factor * width // 3)
        rt(90)
        fd(height)
        rt(90)
        fd(self.base_length_factor * width // 3)
        rt(180)
        fd(self.base_length_factor * width // 3)
        lt(90)
        fd(height // 2)
        lt(90)
        fd(self.base_length_factor * width // 3)
        x_coor, y_coor = pos()
        self.base.x_coor = (
            x_coor + self.base_length_factor * width // 3 + Config.minimal_border_width
        )
        self.base.y_coor = y_coor + height * self.base_height_factor // 2
        self.base.width = (1 - self.base_length_factor) * width
        self.base.height = height * self.base_height_factor
        self.base.draw()
