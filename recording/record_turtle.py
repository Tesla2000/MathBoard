import turtle

from recording.save_screen import save_screen

record = True


def _wrapper(function):
    def inner(*args, **kwargs):
        result = function(*args, **kwargs)
        if record:
            save_screen()
        return result

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
