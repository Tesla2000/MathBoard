import os
import shutil
from itertools import zip_longest, chain, repeat, islice

from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.video.compositing.concatenate import concatenate_videoclips
from moviepy.video.io.VideoFileClip import VideoFileClip

from Config import Config
from recording.create_video_from_frame import create_video_from_frame


def concat_videos(delete_images: bool = True):
    video_clips = list(map(VideoFileClip, sorted(map(str, Config.output_videos.iterdir()), key=os.path.getctime)))
    pause_frames = [str(Config.first_frame)] + list(sorted(map(str, Config.last_frames.iterdir()), key=os.path.getctime))
    audio_clips = list(map(AudioFileClip, map(str, map(Config.output_audios.joinpath, map(Config.audio_name_normalization, Config.texts_to_translate)))))
    audio_clip = audio_clips.pop(0)
    final_clips = [create_video_from_frame(pause_frames.pop(0), audio_clip.duration, audio_clip=audio_clip)]

    for video_clip, pause_frame, audio_clip in zip_longest(video_clips, islice(chain.from_iterable((pause_frames, repeat(pause_frames[-1]))), len(audio_clips)), audio_clips):
        if video_clip is not None:
            final_clips.append(video_clip)
        if pause_frame is not None and audio_clip is not None:
            final_clips.append(create_video_from_frame(pause_frame, audio_clip.duration, audio_clip=audio_clip))
    final_clip = concatenate_videoclips(final_clips)
    final_clip.write_videofile(str(Config.final_videos.joinpath(Config.final_video_name)), codec="libx264", fps=24)
    final_clip.close()
    for clip in video_clips:
        clip.close()
    for clip in audio_clips:
        clip.close()
    if delete_images:
        shutil.rmtree(Config.output_videos)
        shutil.rmtree(Config.last_frames)


if __name__ == '__main__':
    concat_videos(False)
