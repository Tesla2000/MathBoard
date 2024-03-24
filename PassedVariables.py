class PassedVariables:
    texts_to_translate = tuple()
    record = False
    texts = []

    @classmethod
    def turn_recording_on(cls):
        cls.record = True

    @classmethod
    def turn_recording_off(cls):
        cls.record = False
