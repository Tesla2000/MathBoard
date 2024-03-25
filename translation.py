import atexit
import json
from collections import defaultdict

import deepl

from Config import Config
from PassedVariables import PassedVariables

translated_texts = defaultdict(dict, dict(
    (file.with_suffix('').name, json.loads(file.read_text())) for file in Config.translations.iterdir()))
_translator = deepl.Translator(Config.deepL_token)


def translate(text: str) -> str:
    if Config.base_language != PassedVariables.language:
        if text in translated_texts[PassedVariables.language]:
            text = translated_texts[PassedVariables.language][text]
        else:
            after_translation = '\n'.join(
                _translator.translate_text(
                    line, target_lang=PassedVariables.language, source_lang=Config.base_language).text for line in
                text.splitlines())
            translated_texts[PassedVariables.language][text] = after_translation
            text = after_translation
    return text


@atexit.register
def save_json():
    print("NO KILL! Saving...")
    for language, translations in translated_texts.items():
        Config.translations.joinpath(language).with_suffix(".json").write_text(json.dumps(translations, indent=2))
    print("Saved.")
