import shutil
from pathlib import Path
from turtle import width


class Config:
    default_height = 100
    default_width = 50
    minimal_border_width = 1
    width(3)
    # screensize(1000, 600)
    start_x = -640
    # start_x = -300
    start_y = 280
    frame_rate = 30

    root = Path(__file__).parent
    image_files = root / 'images'
    output_videos = root / 'output_videos'
    temporary_picture = root / ".ps"
    shutil.rmtree(image_files)
    image_files.mkdir()
    output_videos.mkdir(exist_ok=True)
