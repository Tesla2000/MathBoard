import shutil
from turtle import reset, width

from Config import Config
from PassedVariables import PassedVariables
from audio.generate_audio import generate_audio
from recording.concat2video import concat2video
from recording.concat_videos import concat_videos
from recording.save_screen import save_screen
from translation import translate

if __name__ == "__main__":
    for language in Config.languages:
        PassedVariables.language = language
        module = getattr(
            __import__(f"{Config.scripts_package.name}.{Config.lesson_name}"),
            Config.lesson_name,
        )
        action_spaces = module.action_spaces
        PassedVariables.texts_to_translate = module.texts_to_translate
        first_iteration = True
        for action_space in action_spaces:
            for action in action_space:
                action()
            if not first_iteration:
                concat2video()
            else:
                first_iteration = False
                PassedVariables.turn_recording_on()
                save_screen(Config.first_frame)
                shutil.rmtree(Config.images)
                Config.images.mkdir()
            pass
        for text_to_translate in PassedVariables.texts_to_translate:
            generate_audio(translate(text_to_translate))
        concat_videos()
        PassedVariables.reset()
        reset()
        width(Config.line_width)

