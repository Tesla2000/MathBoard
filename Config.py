import os
import shutil
from pathlib import Path
from turtle import width

from recording.save_screen import save_screen


class _VideoElements:
    final_video_name = "Skracanie_ułamków.mp4"
    texts_to_translate = (
        "Cześć pokażę Ci dzisiaj jak skracać ułamki.",
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
    record = True
    temporary_picture = root / ".ps"
    temp_filename = str(root / '.mp4')
    image_files = root / 'images'
    output_videos = root / 'output_videos'
    output_audios = root / 'output_audios'
    last_frames = root / 'last_frames'
    first_frame = root / 'first_frame.jpg'
    final_videos = root / 'final_videos'
    shutil.rmtree(image_files)
    shutil.rmtree(last_frames)
    final_videos.mkdir(exist_ok=True)
    output_videos.mkdir(exist_ok=True)
    output_audios.mkdir(exist_ok=True)
    last_frames.mkdir(exist_ok=True)
    save_screen(first_frame)
