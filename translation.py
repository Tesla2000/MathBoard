import atexit
import json
import os
import re
from collections import defaultdict
from functools import partial

import deepl

from Config import Config

translated_texts = defaultdict(
    dict,
    dict(
        (file.with_suffix("").name, json.loads(file.read_text()))
        for file in Config.translations.iterdir()
    ),
)
_translator = deepl.Translator(Config.deepL_token)


def translate(text: str, language: str) -> str:
    if not text:
        return text
    if Config.base_language != language:
        text = "\n".join(map(partial(_translate_line, language=language), text.splitlines()))
    return text


def _translate_line(line: str, language: str) -> str:
    prefix = re.findall(r"^[.\d> ]+", line)
    if prefix:
        prefix = prefix[0]
    else:
        prefix = ""
    line = re.sub(r"^[.\d> ]+", "", line)
    if line not in translated_texts[language]:
        if Config.debug or Config.api_forbidden:
            raise ValueError
        translated = _translator.translate_text(
            line, target_lang={"en": Config.default_english}.get(language.lower(), language), source_lang=Config.base_language
        ).text
        translated_texts[language][line] = translated
    return prefix + translated_texts[language][line]


@atexit.register
def save_translations():
    print("NO KILL! Saving translations...")
    for language, translations in translated_texts.items():
        Config.temp_translations.write_text(json.dumps(translations, indent=2))
        os.replace(
            Config.temp_translations,
            Config.translations.joinpath(language).with_suffix(".json"),
        )
    print("Saved.")
