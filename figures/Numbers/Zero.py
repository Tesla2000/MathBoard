from .Digit import Digit
from recording.record_turtle import fd, rt


class Zero(Digit):
    value = 0
    def _draw(self, width: int, height: int):
        fd(width)
        rt(90)
        fd(height)
        rt(90)
        fd(width)
        rt(90)
        fd(height)
