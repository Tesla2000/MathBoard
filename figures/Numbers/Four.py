from recording.record_turtle import pu, fd, rt, bk, lt

from .Digit import Digit


class Four(Digit):
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
