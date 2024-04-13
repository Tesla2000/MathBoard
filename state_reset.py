import shutil
from turtle import reset, width, speed, hideturtle

from Config import Config
from PassedVariables import PassedVariables


def state_reset():
    shutil.rmtree(Config.output_videos)
    shutil.rmtree(Config.last_frames)
    Config.output_videos.mkdir()
    Config.last_frames.mkdir()

    PassedVariables.reset()
    reset()
    width(Config.line_width)
    speed(0)
    hideturtle()
