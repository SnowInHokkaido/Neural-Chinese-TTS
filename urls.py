#!/usr/bin/python

from handlers.WebHandler import WebHandler, WebTTSHandler
from handlers.TTSHandler import TTSHandler

urls = [
      (r'/tts/', WebHandler),
      (r'/tts/websynthesis/', WebTTSHandler),
      (r'/tts/synthesis/', TTSHandler)
]
