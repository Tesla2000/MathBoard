from turtle import reset, width, speed

from Config import Config
from PassedVariables import PassedVariables


def state_reset():
    PassedVariables.reset()
    reset()
    width(Config.line_width)
    speed(0)
