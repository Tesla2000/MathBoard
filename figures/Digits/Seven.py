from math import pi, atan, sqrt
from recording.record_turtle import fd, rt, bk, setheading

from .Digit import Digit


class Seven(Digit):
    value = 7

    def _draw(self, width: int, height: int):
        fd(width)
        rt(atan(width / height) * 180 / pi + 90)
        total_length = sqrt(height ** 2 + width ** 2)
        fd(total_length)
        bk(total_length // 2)
        setheading(0)
        fd(width // 4)
        bk(width // 2)
