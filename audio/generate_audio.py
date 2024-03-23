from pathlib import Path

from Config import Config
from openai import OpenAI

client = OpenAI()


def generate_audio(text_to_translate: str):
    speech_file_path = Config.output_audios.joinpath(Config.audio_name_normalization(text_to_translate))
    if speech_file_path.exists():
        return
    response = client.audio.speech.create(
        model=Config.model,
        voice=Config.voice,
        input=text_to_translate,
    )
    response.stream_to_file(speech_file_path)


if __name__ == '__main__':
    generate_audio("Przenisienie wykładnika z ułamka na licznik i mianownik.")
