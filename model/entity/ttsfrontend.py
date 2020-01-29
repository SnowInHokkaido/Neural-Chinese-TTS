from TEXT.frontend import chinese_to_pinyin

class TTSFrontend(object):
    def __init__(self):
        pass

    def chinese_to_pinyin(self, text):
        pinyin = chinese_to_pinyin(text)
        return pinyin

    def check_length(self, text):
        return len(text)

