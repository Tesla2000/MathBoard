from moviepy.audio.AudioClip import AudioClip
from moviepy.video.io.ImageSequenceClip import ImageSequenceClip
from moviepy.video.io.VideoFileClip import VideoFileClip

from Config import Config


def create_video_from_frame(
    frame_path: str,
    duration_seconds: float,
    filename: str = Config.temp_filename,
    audio_clip: AudioClip = None,
) -> VideoFileClip:
    clip = ImageSequenceClip(2 * [frame_path], fps=2 / duration_seconds)
    clip.write_videofile(filename, codec="libx264")
    video_clip = VideoFileClip(filename)
    if audio_clip is not None:
        return video_clip.set_audio(audio_clip)
    return video_clip
