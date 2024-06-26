from recording.record_turtle import fd, rt, bk

from .Digit import Digit


class Nine(Digit):
    value = 9

    def _draw(self, width: int, height: int):
        fd(width)
        rt(90)
        fd(height)
        rt(90)
        fd(width)
        bk(width)
        rt(90)
        fd(height // 2)
        rt(-90)
        fd(width)
        rt(90)
        fd(height // 2)
