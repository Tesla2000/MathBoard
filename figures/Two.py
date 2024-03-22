from recording.record_turtle import fd, rt, bk, lt

from figures.Figure import Figure


class Two(Figure):
    def _draw(self, width: int, height: int):
        fd(width)
        rt(90)
        fd(height // 2)
        lt(90)
        bk(width)
        lt(90)
        bk(height // 2)
        lt(90)
        bk(width)
