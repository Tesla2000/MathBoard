from collections import defaultdict


class PassedVariables:
    texts_to_translate = list()
    translations = list()
    record = False
    supress_recording = False
    texts = defaultdict(list)

    @classmethod
    def reset(cls):
        cls.texts_to_translate = list()
        cls.translations = list()
        cls.record = False
        cls.supress_recording = False
        cls.texts = defaultdict(list)

    @classmethod
    def turn_recording_on(cls):
        cls.record = True

    @classmethod
    def turn_recording_off(cls):
        cls.record = False
