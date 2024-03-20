from turtle import getcanvas
from PIL import Image

from Config import Config

index = 0


def save_screen():
    global index
    getcanvas().postscript(file=Config.temporary_picture)
    with Image.open(Config.temporary_picture) as img:
        if img.mode != 'RGB':
            img = img.convert('RGB')
        img.save(Config.image_files / f'{index}.jpg')
        index += 1
