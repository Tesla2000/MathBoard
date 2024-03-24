import time
from typing import Callable

import requests

from Config import Config
from PassedVariables import PassedVariables
from figures.Figure import Figure


if __name__ == '__main__':
    from libretranslatepy import LibreTranslateAPI

    lt = LibreTranslateAPI("https://libretranslate.com/translate", "")

    print(lt.translate("LibreTranslate is awesome!", "en", "es"))
    # LibreTranslate es impresionante!

    print(lt.detect("Hello World"))
    # [{"confidence": 0.6, "language": "en"}]

    print(lt.languages())
    # [{"code":"en", "name":"English"}]

class Text(Figure):
    _translator = Translator()

    def __init__(
        self,
        width: int = None,
        height: int = None,
        x_coor: int = None,
        y_coor: int = None,
        text: str = None,
        font_size: str = None,
    ):
        super().__init__(width, height, x_coor, y_coor)
        self.font_size = font_size
        if self.font_size is None:
            self.font_size = Config.font_size
        self.text = text

    def draw(
        self,
        width: int = None,
        height: int = None,
        border_width: int = None,
        border_height: int = None,
    ):

        if (detected := self._translator.detect(self.text).lang) != PassedVariables.language:
            self.text = '\n'.join(
                self._translator.translate(line, dest=PassedVariables.language, src=detected).text for line in
                self.text.splitlines())
        PassedVariables.texts.append(
            (
                self.x_coor - Config.start_x,
                Config.start_y - self.y_coor,
                self.text,
                self.font_size,
            )
        )

    def gen_add_text(self, text: str) -> Callable:
        return lambda: setattr(self, "text", text)

    @staticmethod
    def clear():
        PassedVariables.texts = []

    def _draw(self, width: int, height: int):
        pass
