from openai import OpenAI

from Config import Config

client = OpenAI()


def generate_audio(text_to_translate: str):
    speech_file_path = Config.output_audios.joinpath(
        Config.audio_name_normalization(text_to_translate)
    )
    if speech_file_path.exists():
        return
    response = client.audio.speech.create(
        model=Config.model,
        voice=Config.voice,
        input=text_to_translate,
    )
    response.stream_to_file(speech_file_path)


if __name__ == "__main__":
    generate_audio("Przeniesienie wykładnika z ułamka na licznik i mianownik.")
