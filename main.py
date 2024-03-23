import shutil

from Config import Config
from audio.generate_audio import generate_audio
from recording.concat2video import concat2video
from recording.concat_videos import concat_videos
from recording.record_turtle import Record
from recording.save_screen import save_screen

if __name__ == '__main__':
    action_spaces = getattr(__import__(f"{Config.scripts_package.name}.{Config.lesson_name}"), Config.lesson_name).action_spaces
    first_iteration = True
    for action_space in action_spaces:
        for action in action_space:
            action()
        if not first_iteration:
            concat2video()
        else:
            first_iteration = False
            Record.record = True
            save_screen(Config.first_frame)
            shutil.rmtree(Config.images)
            Config.images.mkdir()
    for text_translate in Config.texts_to_translate:
        generate_audio(text_translate)
    concat_videos()
