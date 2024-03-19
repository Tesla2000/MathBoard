from time import time, sleep
from turtle import getcanvas
from PIL import Image

from Config import Config

record = True


def save_screen():
    image_counter = 0
    start = time()
    next_time = time()
    while record:
        sleep_time = next_time - time()
        if sleep_time > 0:
            sleep(sleep_time)
        getcanvas().postscript(file='.ps')
        with Image.open('.ps') as img:
            if img.mode != 'RGB':
                img = img.convert('RGB')
            img.save(Config.image_files / f'{image_counter}.jpg')
            image_counter += 1
        next_time = start + 1 / Config.fps
