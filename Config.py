import os
import re
import shutil
from pathlib import Path
from turtle import width


class _VideoElements:
    final_video_name = "Skracanie_ułamków.mp4"
    texts_to_translate = (
        "Cześć pokażę Ci dzisiaj jak skracać ułamki.",
        "Dziękuję za uwagę.",
    )


class Config(_VideoElements):
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
    open_ai_token = root.joinpath('open_ai_token').read_text()
    os.environ.setdefault("OPENAI_API_KEY", open_ai_token)
    temporary_picture = root / ".ps"
    temp_filename = str(root / '.mp4')
    images = root / 'images'
    output_videos = root / 'output_videos'
    output_audios = root / 'output_audios'
    last_frames = root / 'last_frames'
    first_frame = root / 'first_frame.jpg'
    final_videos = root / 'final_videos'
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
            'ą': 'a',
            'ć': 'c',
            'ę': 'e',
            'ł': 'l',
            'ń': 'n',
            'ó': 'o',
            'ś': 's',
            'ż': 'z',
            'ź': 'z',
            ' ': '_',
        }
        return ''.join(polish_to_english.get(letter, letter) for letter in re.sub(r'[,\.?!]', '', text).lower()) + ".mp3"


from recording.save_screen import save_screen

save_screen(Config.first_frame)
