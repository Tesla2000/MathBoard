from recording.record_turtle import fd, rt, bk, lt

from .Digit import Digit


class Two(Digit):
    value = 2

    def _draw(self, width: int, height: int):
        fd(width)
        rt(90)
        fd(height // 2)
        rt(90)
        fd(width)
        lt(90)
        fd(height - height // 2)
        lt(90)
        fd(width)
