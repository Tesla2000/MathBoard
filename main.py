import shutil
from time import sleep

from upload_video import upload_video
from Config import Config
from PassedVariables import PassedVariables
from audio.generate_audio import generate_audio
from recording.concat2video import concat2video
from recording.concat_videos import concat_videos
from recording.save_screen import save_screen
from state_reset import state_reset
from translation import translate


def main():
    for lesson_name in Config.lesson_names:
        module = getattr(
            __import__(f"{Config.scripts_package.name}.{lesson_name}"),
            lesson_name,
        )
        action_spaces = module.action_spaces
        PassedVariables.texts_to_translate = list(module.texts_to_translate)
        first_iteration = True
        for action_space in action_spaces:
            for action in action_space:
                action()
            if Config.debug:
                continue
            for language in Config.languages:
                if not first_iteration:
                    concat2video(language)
                else:
                    PassedVariables.turn_recording_on()
                    save_screen(Config.first_frames.joinpath(language).with_suffix(Config.image_format))
            shutil.rmtree(Config.images)
            Config.images.mkdir()
            first_iteration = False
        if Config.debug:
            sleep(3)
            return
        for language in Config.languages:
            translations = []
            for index, text_to_translate in enumerate(PassedVariables.texts_to_translate):
                translation = translate(text_to_translate, language)
                translations.append(translation)
                generate_audio(translation)
            output_video_path = concat_videos(lesson_name, language, translations)
            if Config.publish:
                upload_video(output_video_path, output_video_path.with_suffix('').name.replace('_', ' ').capitalize(), module.texts_to_translate[0])
        state_reset()


if __name__ == "__main__":
    main()
