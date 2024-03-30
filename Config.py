import os
import re
import shutil
from pathlib import Path
from turtle import width, speed


class _VideoElements:
    lesson_name = "Dodawanie_ułamków"
    script = f"{lesson_name}.py"
    final_video_name = (lesson_name + "_{}.mp4").format


class _AudioElements:
    similarity_boost = .9
    stability = .9
    model_id = "eleven_multilingual_v2"
    voice_id = "2EiwWnXFnvU5JabPnv8n"

    model = "tts-1"
    voice = "alloy"


class Config(_VideoElements, _AudioElements):
    base_language = "pl"
    languages = (
        "uk",
        # "pl",
    )
    font_size = 12
    font_path = "DejaVuSans"
    color = "black"
    default_height = 100
    default_width = 50
    symbol_write_speed = 10
    minimal_border_width = 7
    line_width = 3
    width(line_width)
    speed(0)
    start_x = -640
    # start_x = -300
    start_y = 280
    # debug = True
    debug = False
    # api_forbidden = True
    api_forbidden = False

    root = Path(__file__).parent
    image_format = ".jpg"
    images = root / "images"
    output_videos = root / "output_videos"
    output_audios = root / "output_audios"
    last_frames = root / "last_frames"
    final_videos = root / "final_videos"
    scripts_package = root / "scripts"
    translations = root / "translations"
    audio_paths = root / "audio_paths.json"

    temporary_files = root / "temporary_files"
    temporary_picture = temporary_files / ".ps"
    temp_translations = temporary_files / "translations.json"
    first_frame = temporary_files / f"first_frame{image_format}"
    temp_filename = str(temporary_files / ".mp4")
    temp_audio_paths = temporary_files / "audio_paths.json"

    tokens = root / "api_keys"
    deepL_token = tokens.joinpath("deepL_token").read_text()
    open_ai_token = tokens.joinpath("open_ai_token").read_text()
    elevenlabs_api_key = tokens.joinpath("elevenlabs").read_text()
    os.environ.setdefault("OPENAI_API_KEY", open_ai_token)

    temporary_files.mkdir(exist_ok=True)
    tokens.mkdir(exist_ok=True)
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
    translations.mkdir(exist_ok=True)

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
