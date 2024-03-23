from typing import Callable

from Config import Config
from PassedVariables import PassedVariables
from figures.Figure import Figure


class Text(Figure):
    def __init__(self, width: int = None, height: int = None, x_coor: int = None, y_coor: int = None, text: str = None,
                 font_size: str = None):
        super().__init__(width, height, x_coor, y_coor)
        self.font_size = font_size
        if self.font_size is None:
            self.font_size = Config.font_size
        self.text = text

    def _draw(self, width: int, height: int):
        PassedVariables.texts.append(
            (self.x_coor - Config.start_x, Config.start_y - self.y_coor, self.text, self.font_size))

    def gen_add_text(self, text: str) -> Callable:
        return lambda: setattr(self, 'text', text)

    @staticmethod
    def clear():
        PassedVariables.texts = []
