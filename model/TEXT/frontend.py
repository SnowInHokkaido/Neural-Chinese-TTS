import re
import jieba
from pypinyin import pinyin, Style, load_phrases_dict
from TEXT.cn_text_normalizer import text_normalize
#from cn_text_normalizer import text_normalize
jieba.initialize()
#jieba.load_userdict('')

def prepare_pinyin(text:str):
    '''
    Arg:
        text: string
    Return:
        py_results: list
    '''
    py_results =[]
    tmp_py_results = [i[0] for i in pinyin(text, style=Style.TONE3, heteronym=False)]
    for item in tmp_py_results:
        if str.isalpha(item):
            item = item + '5'
        py_results.append(item)
    return py_results

def whitelist(text):
    pat = re.compile('[^\u4e00-\u9fa5,.!?]') 
    return re.sub(pat, '', text)

def to_en_punc(text):
    zh ='，。！？；、（）；'
    en =',.!?,,,,,'
    transtable = str.maketrans(zh, en)
    res = text.translate(transtable)
    return res 

def split_long_sentence(text:str):
    '''
    Return: list
    '''
    start = 0
    i = 0 
    token = 'meaningless'
    sens = []
    punc_list = ',.!?'
    for letter in text:
        if letter in punc_list and token not in punc_list:
            sens.append(text[start:i+1])
            start = i+1
            i += 1

        else:
            i += 1
            token = list(text[start:i+2]).pop()
    if start < len(text):
         sens.append(text[start:])
    return sens

def concat_short_sentences(short_sentences:list, threshold:float):
    long_sentences = []
    tmp = []
    tmp_length = 0
    for sentence in short_sentences[:-1]:
        length = len(sentence)
        tmp_length += length
        if sentence[-1] in '.!?':
            tmp.append(sentence)
            long_sentence = ' '.join(tmp)
            long_sentences.append(long_sentence)
            tmp_length = 0
            tmp = []
        elif tmp_length >= threshold:
            tmp.append(sentence[:-1] + '.')
            long_sentence = ' '.join(tmp)
            long_sentences.append(long_sentence)
            tmp_length = 0
            tmp = []
        else:
            tmp.append(sentence)
    if short_sentences[-1][-1] not in ',!.?':
        tmp.append(short_sentences[-1] + '.')
    else:
        tmp.append(short_sentences[-1])
    result = ' '.join(tmp)
    long_sentences.append(result)
    return long_sentences    

def chinese_to_pinyin(text:str):
    '''
    Return: pinyin list
    '''
    pinyin_sentences = []
    text = to_en_punc(text)
    normalized_text = text_normalize(text)
    cleaned_text = whitelist(normalized_text)
    short_sentences = split_long_sentence(cleaned_text)
    long_sentences = concat_short_sentences(short_sentences, threshold=20) # CONCAT THRESHOLD
    for sentence in long_sentences:
        pinyin_sentence = []
        segmented_text = [i for i in jieba.cut(sentence, cut_all=False, HMM=True)]
        for word in segmented_text:
            pinyin = prepare_pinyin(word)
            pinyin = ''.join(pinyin) # NO SPACE
            pinyin_sentence.append(pinyin)
        pinyin_sentences.append(''.join(pinyin_sentence))
    return pinyin_sentences

def main(): 
    text = '劉愷威和楊冪, 去年12月! 宣布離婚，女兒「小糯米」由兩公婆!共同撫養。'
    print(chinese_to_pinyin(text))
 
if __name__ == '__main__':
     main() 
