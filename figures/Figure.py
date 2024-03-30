from abc import ABC, abstractmethod
from turtle import color as c

from Config import Config
from PassedVariables import PassedVariables
from figures import moveto
from recording.record_turtle import pu, pd


class Figure(ABC):
    border_width = True
    border_height = True
    width = Config.default_width
    height = Config.default_height

    def __init__(
        self,
        width: int = None,
        height: int = None,
        x_coor: int = None,
        y_coor: int = None,
    ):
        self.x_coor = x_coor
        self.y_coor = y_coor
        if height is not None:
            self.height = height
        if width is not None:
            self.width = width

    def draw(
        self,
        width: int = None,
        height: int = None,
        border_width: int = None,
        border_height: int = None,
        color: str = None,
    ):
        if color is not None:
            c(color)
        moveto(self.x_coor, self.y_coor)
        if width is None:
            width = round(self.width)
        if height is None:
            height = round(self.height)
        self.width = width
        self.height = height
        if border_width is None and self.border_width is True:
            border_width = Config.minimal_border_width
        if border_height is None and self.border_height is True:
            border_height = Config.minimal_border_width
        pd()
        self._draw(round(width - (border_width or 0)), round(height - (border_height or 0)))
        pu()

    def undo(
        self,
        width: int = None,
        height: int = None,
        border_width: int = None,
        border_height: int = None,
    ):
        c("white")
        prev_color = self.color
        self.color = "white"
        self.draw(
            width=width,
            height=height,
            border_width=border_width,
            border_height=border_height,
        )
        c(Config.color)
        self.color = prev_color

    def undo_no_record(
        self,
        width: int = None,
        height: int = None,
        border_width: int = None,
        border_height: int = None,
    ):
        PassedVariables.supress_recording = True
        self.undo(width, height, border_width, border_height)
        PassedVariables.supress_recording = False

    @abstractmethod
    def _draw(self, width: int, height: int):
        pass

    def __repr__(self):
        return f"{type(self).__name__},width={self.width},height={self.height}"
