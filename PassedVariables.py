class PassedVariables:
    language = None
    texts_to_translate = list()
    record = False
    supress_recording = False
    texts = []

    @classmethod
    def reset(cls):
        cls.texts_to_translate = list()
        cls.record = False
        cls.supress_recording = False
        cls.texts = []

    @classmethod
    def turn_recording_on(cls):
        cls.record = True

    @classmethod
    def turn_recording_off(cls):
        cls.record = False
