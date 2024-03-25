from recording.record_turtle import pu, fd, rt, bk, lt

from .Number import Number


class Four(Number):
    value = 4
    def _draw(self, width: int, height: int):
        rt(90)
        fd(height // 2)
        lt(90)
        fd(width)
        lt(90)
        fd(height // 2)
        bk(height)
        pu()