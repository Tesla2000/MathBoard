import os
from datetime import datetime

from moviepy.editor import ImageSequenceClip

from Config import Config


def concat2video():
    clip = ImageSequenceClip(list(map(str, sorted(Config.image_files.iterdir(), key=os.path.getmtime))), fps=Config.frame_rate)
    output_video_path = str(Config.output_videos.joinpath(datetime.now().strftime('%Y%m%d%H%M') + '.mp4'))
    clip.write_videofile(output_video_path, codec='libx264')
