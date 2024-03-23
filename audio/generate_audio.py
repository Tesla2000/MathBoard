import elevenlabs

from Config import Config
import requests


def generate_audio(text_to_translate: str):
    speech_file_path = Config.output_audios.joinpath(
        Config.audio_name_normalization(text_to_translate)
    )
    if speech_file_path.exists():
        return
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{Config.voice_id}"

    payload = {
        "model_id": Config.model_id,
        "text": text_to_translate,
        "voice_settings": {
            "similarity_boost": Config.similarity_boost,
            "stability": Config.stability,
            "style": .5,
            "use_speaker_boost": True
        }
    }
    headers = {"Content-Type": "application/json"}
    response = requests.request("POST", url, json=payload, headers=headers)
    elevenlabs.save(response.content, speech_file_path)


if __name__ == "__main__":
    generate_audio("Przeniesienie wykładnika z ułamka na licznik i mianownik.")
