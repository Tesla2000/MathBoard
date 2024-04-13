import os
from itertools import zip_longest, chain, repeat, islice
from pathlib import Path

from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.video.compositing.concatenate import concatenate_videoclips
from moviepy.video.io.VideoFileClip import VideoFileClip

from Config import Config
from audio.generate_audio import audio_paths
from recording.create_video_from_frame import create_video_from_frame


def concat_videos(lesson_name: str, language: str, translations: list[str]) -> Path:
    video_clips = list(
        map(
            VideoFileClip,
            sorted(set(map(str, Config.output_videos.glob(f"*{language}*"))), key=os.path.getctime),
        )
    )
    pause_frames = [str(Config.first_frames.joinpath(language).with_suffix(Config.image_format))] + list(
        sorted(set(map(str, Config.last_frames.glob(f"*{language}*"))), key=os.path.getctime)
    )
    audio_clips = list(
        map(
            AudioFileClip,
            map(
                str,
                map(
                    audio_paths.get,
                    map(
                        Config.audio_name_normalization,
                        translations,
                    ),
                ),
            ),
        )
    )
    repeated_frame = repeat(pause_frames[-1])
    audio_clip = audio_clips.pop(0)
    final_clips = [
        create_video_from_frame(
            pause_frames.pop(0), audio_clip.duration, audio_clip=audio_clip
        )
    ]

    for video_clip, pause_frame, audio_clip in zip_longest(
        video_clips,
        islice(chain.from_iterable((pause_frames, repeated_frame)), len(audio_clips)),
        audio_clips,
    ):
        if video_clip is not None:
            final_clips.append(video_clip)
        if pause_frame is not None and audio_clip is not None:
            final_clips.append(
                create_video_from_frame(
                    pause_frame, audio_clip.duration, audio_clip=audio_clip
                )
            )
    final_clip = concatenate_videoclips(final_clips)
    output_file_path = Config.final_videos.joinpath(
        Config.final_video_name(lesson_name, language)
    )
    final_clip.write_videofile(
        str(output_file_path),
        codec="libx264",
        fps=24,
    )
    final_clip.close()
    for clip in video_clips:
        clip.close()
    for clip in audio_clips:
        clip.close()
    return output_file_path
