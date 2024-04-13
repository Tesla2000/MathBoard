import os
import shutil
from datetime import datetime
from random import randint

from moviepy.editor import ImageSequenceClip

from Config import Config


def concat2video(language: str):
    images = list(map(str, sorted((image for image in Config.images.iterdir() if language in image.name or image.with_suffix("").name.isnumeric()), key=os.path.getmtime)))
    if not images:
        images = list(map(str, sorted((image for image in Config.last_frames.iterdir() if language in image.name or image.with_suffix("").name.isnumeric()), key=os.path.getmtime)))
        if images:
            images = 2 * [images[-1]]
        else:
            images = 2 * [str(next((image for image in Config.first_frames.iterdir() if language in image.name or image.with_suffix("").name.isnumeric())))]
    clip = ImageSequenceClip(images, fps=Config.symbol_write_speed)
    video_file_name = datetime.now().strftime(f"%Y%m%d%H%M%S{language}{randint(0, 10**12)}")
    output_video_path = Config.output_videos.joinpath(video_file_name).with_suffix(
        ".mp4"
    )
    clip.write_videofile(str(output_video_path), codec="libx264")
    shutil.copy(
        images[-1],
        Config.last_frames.joinpath(video_file_name).with_suffix(Config.image_format),
    )
