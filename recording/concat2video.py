import os
import shutil
from datetime import datetime

from moviepy.editor import ImageSequenceClip

from Config import Config


def concat2video(delete_images: bool = True):
    images = list(map(str, sorted(Config.images.iterdir(), key=os.path.getmtime)))
    if not images:
        images = list(map(str, sorted(Config.images.iterdir(), key=os.path.getmtime)))
        if images:
            images = 2 * [images[0]]
        else:
            images = 2 * [str(Config.first_frame)]
    clip = ImageSequenceClip(images, fps=Config.symbol_write_speed)
    video_file_name = datetime.now().strftime("%Y%m%d%H%M%S")
    output_video_path = Config.output_videos.joinpath(video_file_name).with_suffix(
        ".mp4"
    )
    clip.write_videofile(str(output_video_path), codec="libx264")
    shutil.copy(
        images[-1],
        Config.last_frames.joinpath(video_file_name).with_suffix(Config.image_format),
    )
    if delete_images:
        shutil.rmtree(Config.images)
        Config.images.mkdir()
