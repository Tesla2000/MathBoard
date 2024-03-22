from Config import Config
from openai import OpenAI

client = OpenAI()


def generate_audio(text_to_translate: str):
    speech_file_path = Config.output_audios.joinpath(Config.audio_name_normalization(text_to_translate))
    if speech_file_path.exists():
        return
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=text_to_translate,
    )
    response.stream_to_file(speech_file_path)
