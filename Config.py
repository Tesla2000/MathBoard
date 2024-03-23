import os
import re
import shutil
from pathlib import Path
from turtle import width


class _VideoElements:
    lesson_name = "Znajdowanie_liczby_niewymiernej"
    script = f"{lesson_name}.py"
    final_video_name = f"{lesson_name}.mp4"


class _AudioElements:
    similarity_boost = 1
    stability = 1
    model_id = "eleven_multilingual_v2"
    voice_id = "2EiwWnXFnvU5JabPnv8n"

    model = "tts-1"
    voice = "alloy"


class Config(_VideoElements, _AudioElements):
    font_size = 12
    font_path = "DejaVuSans"
    color = "black"
    default_height = 100
    default_width = 50
    symbol_write_speed = 10
    minimal_border_width = 7
    width(3)
    # screensize(1000, 600)
    start_x = -640
    # start_x = -300
    start_y = 280

    root = Path(__file__).parent
    open_ai_token = root.joinpath("open_ai_token").read_text()
    os.environ.setdefault("OPENAI_API_KEY", open_ai_token)
    temporary_picture = root / ".ps"
    temp_filename = str(root / ".mp4")
    images = root / "images"
    output_videos = root / "output_videos"
    output_audios = root / "output_audios"
    last_frames = root / "last_frames"
    first_frame = root / "first_frame.jpg"
    final_videos = root / "final_videos"
    scripts_package = root / "scripts"
    output_videos.mkdir(exist_ok=True)
    images.mkdir(exist_ok=True)
    last_frames.mkdir(exist_ok=True)
    shutil.rmtree(output_videos)
    shutil.rmtree(images)
    shutil.rmtree(last_frames)
    final_videos.mkdir(exist_ok=True)
    output_videos.mkdir(exist_ok=True)
    output_audios.mkdir(exist_ok=True)
    last_frames.mkdir(exist_ok=True)
    images.mkdir(exist_ok=True)

    @staticmethod
    def audio_name_normalization(text: str) -> str:
        polish_to_english = {
            "ą": "a",
            "ć": "c",
            "ę": "e",
            "ł": "l",
            "ń": "n",
            "ó": "o",
            "ś": "s",
            "ż": "z",
            "ź": "z",
            " ": "_",
        }
        return (
            "".join(
                polish_to_english.get(letter, letter)
                for letter in re.sub(r"[,.?!]", "", text.strip()).lower()
            )
            + ".mp3"
        )
