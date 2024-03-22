import turtle

from Config import Config
from recording.save_screen import save_screen


def _wrapper(function):
    def inner(*args, **kwargs):
        if Config.record:
            save_screen()
        return function(*args, **kwargs)

    return inner


fd = _wrapper(turtle.fd)
bk = _wrapper(turtle.bk)
goto = _wrapper(turtle.goto)
dot = _wrapper(turtle.dot)

pos = turtle.pos
pd = turtle.pd
pu = turtle.pu
setheading = turtle.setheading
rt = turtle.rt
lt = turtle.lt
