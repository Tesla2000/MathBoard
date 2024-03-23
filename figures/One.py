from figures.Figure import Figure
from recording.record_turtle import pu, pd, fd, rt, bk


class One(Figure):

    def _draw(self, width: int, height: int):
        pu()
        fd(3 * width // 4)
        pd()
        rt(90)
        fd(height)
        bk(height)
        rt(60)
        fd(width // 2)
