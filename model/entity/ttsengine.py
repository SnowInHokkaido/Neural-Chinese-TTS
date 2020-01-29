from TTS.utils.generic_utils import load_config
from TTS.synthesizer import Synthesizer

config = load_config('./model/conf.json')

class TTSEngine(object):
    def __init__(self):
        self.synthesizer = Synthesizer(config)

    def translate(self, text):
        wav = self.synthesizer.tts(text)
        return wav
