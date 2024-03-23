import os
import shutil
from datetime import datetime

from moviepy.editor import ImageSequenceClip

from Config import Config


def concat2video(delete_images: bool = True):
    images = list(map(str, sorted(Config.images.iterdir(), key=os.path.getmtime)))
    clip = ImageSequenceClip(images, fps=Config.symbol_write_speed)
    video_file_name = datetime.now().strftime('%Y%m%d%H%M')
    output_video_path = Config.output_videos.joinpath(video_file_name).with_suffix('.mp4')
    clip.write_videofile(str(output_video_path), codec='libx264')
    shutil.move(images[-1], Config.last_frames.joinpath(video_file_name).with_suffix('.jpg'))
    if delete_images:
        shutil.rmtree(Config.images)
        Config.images.mkdir()
