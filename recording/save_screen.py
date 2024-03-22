from pathlib import Path
from turtle import getcanvas
from PIL import Image

from Config import Config

index = 0


def save_screen(path: Path = None):
    global index
    getcanvas().postscript(file=Config.temporary_picture)
    with Image.open(Config.temporary_picture) as img:
        if img.mode != 'RGB':
            img = img.convert('RGB')
        if path is None:
            img.save(Config.images / f'{index}.jpg')
        else:
            img.save(path)
        index += 1
