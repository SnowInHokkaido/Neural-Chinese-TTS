# Neural Chinese TTS Service #

## Introduction ##
This repo is an open-source TTS web server for Chinese text-to-speech task. The backend model was developed from Google Tacotron1 model. The training dataset was an open-source Chinese Speech Dataset released by Biaobei.

It is a very simple web server which could be a benchmark for Chinese TTS research.

## Demo Address ##

<http://116.85.43.87:8008/tts/>

## Model Training ##
The training code can be found here <https://github.com/mozilla/TTS>. The model training was accomplished in a NVIDIA 1070TI within 36 hours.

## Reference ##
Tacotron1 <https://github.com/mozilla/TTS>

Pypinyin <https://github.com/mozillazg/python-pinyin>

Cn-Text-normalier <https://github.com/open-speech/cn-text-normalizer>
