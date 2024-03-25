import atexit
import json
import os
import re
from collections import defaultdict

import deepl

from Config import Config
from PassedVariables import PassedVariables

translated_texts = defaultdict(
    dict,
    dict(
        (file.with_suffix("").name, json.loads(file.read_text()))
        for file in Config.translations.iterdir()
    ),
)
_translator = deepl.Translator(Config.deepL_token)


def translate(text: str) -> str:
    if Config.base_language != PassedVariables.language:
        text = "\n".join(map(_translate_line, text.splitlines()))
    return text


def _translate_line(line: str) -> str:
    prefix = re.findall(r"^[.\d> ]+", line)
    if prefix:
        prefix = prefix[0]
    else:
        prefix = ""
    line = re.sub(r"^[.\d> ]+", "", line)
    if line not in translated_texts[PassedVariables.language]:
        translated = _translator.translate_text(
            line, target_lang=PassedVariables.language, source_lang=Config.base_language
        ).text
        translated_texts[PassedVariables.language][line] = translated
    return prefix + translated_texts[PassedVariables.language][line]


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
