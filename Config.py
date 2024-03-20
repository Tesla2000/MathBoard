from pathlib import Path
from turtle import width


class Config:
    default_height = 100
    default_width = 50
    minimal_border_width = 3
    width(3)
    start_x = -640
    start_y = 280
    fps = 30

    root = Path(__file__).parent
    image_files = root / 'images'
    video_files = root / 'videos'
    image_files.mkdir(exist_ok=True)
    video_files.mkdir(exist_ok=True)
