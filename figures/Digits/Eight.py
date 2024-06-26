from recording.record_turtle import fd, rt, bk, lt

from .Digit import Digit


class Eight(Digit):
    value = 8

    def _draw(self, width: int, height: int):
        fd(width)
        rt(90)
        fd(height)
        rt(90)
        fd(width)
        rt(90)
        fd(height // 2)
        rt(90)
        fd(width)
        bk(width)
        lt(90)
        fd(height // 2)
