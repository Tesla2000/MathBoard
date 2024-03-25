from turtle import reset, width

from Config import Config
from PassedVariables import PassedVariables


def state_reset():
    PassedVariables.reset()
    reset()
    width(Config.line_width)
