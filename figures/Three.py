from recording.record_turtle import fd, rt, bk, lt

from figures.Figure import Figure


class Three(Figure):
    def _draw(self, width: int, height: int):
        fd(width)
        rt(90)
        fd(height // 2)
        rt(90)
        fd(width)
        bk(width)
        lt(90)
        fd(height - height // 2)
        rt(90)
        fd(width)
