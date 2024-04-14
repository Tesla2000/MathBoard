from pathlib import Path
from turtle import getcanvas
from PIL import Image
from PIL.ImageDraw import Draw
from PIL.ImageFont import truetype

from Config import Config
from PassedVariables import PassedVariables

_index = 0


def save_screen(path: Path = None):
    global _index
    getcanvas().postscript(file=Config.temporary_picture)
    are_texts = any(any(text for x, y, text, font_size in PassedVariables.texts[language]) for language in Config.languages)
    for language in (Config.languages if are_texts else ("",)):
        if path is not None and language not in str(path):
            continue
        with Image.open(Config.temporary_picture) as img:
            if img.mode != "RGB":
                img = img.convert("RGB")
            if PassedVariables.texts[language]:
                draw = Draw(img)
            for (x, y, text, font_size) in PassedVariables.texts[language]:
                font = truetype(Config.font_path, font_size)
                draw.text((x, y), text, fill=Config.color, font=font, encoding="utf-8")
            img = img.resize((960, 540))
            if path is None:
                img.save(Config.images / f"{_index}{language if language else "".join(Config.languages)}{Config.image_format}")
            else:
                img.save(path)
    _index += 1
