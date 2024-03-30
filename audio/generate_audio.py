import atexit
import json
import os
import random
from pathlib import Path

import elevenlabs

from Config import Config
import requests

audio_paths = json.loads(Config.audio_paths.read_text())


def generate_audio(text_to_translate: str) -> Path:
    normalized_text = Config.audio_name_normalization(text_to_translate)
    if normalized_text in audio_paths:
        speech_file_path = Path(audio_paths[normalized_text])
    else:
        speech_file_path = Config.output_audios.joinpath(
            str(random.randint(0, 1_000_000_000))
        ).with_suffix(".mp3")
    if speech_file_path.exists():
        return speech_file_path
    if Config.debug or Config.api_forbidden:
        raise ValueError
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{Config.voice_id}"

    payload = {
        "model_id": Config.model_id,
        "text": text_to_translate,
        "voice_settings": {
            "similarity_boost": Config.similarity_boost,
            "stability": Config.stability,
            "style": 0.5,
            "use_speaker_boost": True,
        },
    }
    headers = {
        "Content-Type": "application/json",
        "xi-api-key": Config.elevenlabs_api_key,
    }
    response = requests.request("POST", url, json=payload, headers=headers)
    if response.status_code != 200:
        raise ValueError(f"Response code {response.status_code}")
    elevenlabs.save(response.content, speech_file_path)
    audio_paths[normalized_text] = str(speech_file_path)
    return speech_file_path


@atexit.register
def saving_audio_paths():
    print("NO KILL! Saving audio paths...")
    Config.temp_audio_paths.write_text(json.dumps(audio_paths, indent=2))
    os.replace(Config.temp_audio_paths, Config.audio_paths)
    print("Saved.")


if __name__ == "__main__":
    generate_audio("Przeniesienie wykładnika z ułamka na licznik i mianownik.")
