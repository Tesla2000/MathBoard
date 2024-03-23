from Config import Config
from figures.Figure import Figure
from recording.record_turtle import pu, pd, fd, rt, bk


class One(Figure):
    width = Config.default_width // 2

    def __init__(
        self,
        width: int = None,
        height: int = None,
        x_coor: int = None,
        y_coor: int = None,
        centered: bool = False,
    ):
        super().__init__(width, height, x_coor, y_coor)
        self.centered = centered

    def _draw(self, width: int, height: int, centered: bool = None):
        pu()
        if centered is None:
            centered = self.centered
        fd(width // 2 if centered else width)
        pd()
        rt(90)
        fd(height)
        bk(height)
        rt(60)
        fd(width // 4)
