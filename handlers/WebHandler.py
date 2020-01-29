#!/usr/bin/python
import datetime
import tornado.web
from model.entity.ttsfrontend import TTSFrontend
from model.entity.ttsuser import TTSUser
from model.entity.ttsengine import TTSEngine

tts_engine = TTSEngine()
tts_frontend = TTSFrontend()

class WebHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('../templates/index.html')


class WebTTSHandler(tornado.web.RequestHandler):
    def get(self):
        start_time = datetime.datetime.now()
        print('[%s] #########START##########'%(start_time))
        text = self.get_argument('text', None)
        print('[%s] input_text: %s' %(datetime.datetime.now(), text))
        pinyin = tts_frontend.chinese_to_pinyin(text)
        print('[%s] input_pinyin: %s' %(datetime.datetime.now(), pinyin))
        tts_user = TTSUser(pinyin) # Entity one
        wav_io = tts_engine.translate(tts_user.text) # Entity two 
        self.set_header("Content-type", "audio/wav")
        self.write(wav_io.read())
        self.finish()
        time_consuming = datetime.datetime.now() - start_time
        print('[%s] time_consuming: %s' %(datetime.datetime.now(), time_consuming))
        print('[%s] ##########DONE##########'%(datetime.datetime.now()))

