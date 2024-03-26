import turtle

from Config import Config
from PassedVariables import PassedVariables
from recording.save_screen import save_screen


def _record_wrapper(function):
    def inner(*args, **kwargs):
        result = function(*args, **kwargs)
        if (
            PassedVariables.record
            and not PassedVariables.supress_recording
            and not Config.debug
        ):
            save_screen()
        return result

    return inner


def _stop_recording_wrapper(function):
    def inner(*args, **kwargs):
        PassedVariables.turn_recording_off()
        return function(*args, **kwargs)

    return inner


def _start_recording_wrapper(function):
    def inner(*args, **kwargs):
        PassedVariables.turn_recording_on()
        return function(*args, **kwargs)

    return inner


fd = _record_wrapper(turtle.fd)
bk = _record_wrapper(turtle.bk)
goto = _record_wrapper(turtle.goto)
dot = _record_wrapper(turtle.dot)

pos = turtle.pos
pd = _start_recording_wrapper(turtle.pd)
pu = _stop_recording_wrapper(turtle.pu)
setheading = turtle.setheading
rt = turtle.rt
lt = turtle.lt
