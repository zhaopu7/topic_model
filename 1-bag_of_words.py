# coding=utf-8
import logging
from gensim import corpora, models, similarities
import jieba

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


def clean_sentence(sentence):
    # print sentence
    sentence = sentence.split('_')[0]  # 去 _ 之后的网页名
    r = ""
    for char in sentence:
        if u'\u4e00' <= char <= u'\u9fff':  # 汉字
            r += char
        elif u'\u0030' <= char <= u'\u0039':  # 数字
            r += char
        elif u'\u0041' <= char <= u'\u005a':  # 大写英文 -> 小写
            r += char.lower()
        elif u'\u0061' <= char <= u'\u007a':  # 小写英文
            r += char
    return r


# 停用词
stop_words = set([str(l).decode('utf-8').strip() for l in open('stop_words_pu.txt')])

# 分词
texts = []
for line in open('data.toy.txt'):
    ws = list(jieba.cut(clean_sentence(line.decode('utf-8'))))
    print ' '.join(ws)
    ws = [w for w in ws if w not in stop_words]
    print ' '.join(ws)
    print '---'
    texts.append(ws)

# remove words that appear only once
from collections import defaultdict

frequency = defaultdict(int)
for text in texts:
    for token in text:
        frequency[token] += 1
texts = [[token for token in text if frequency[token] > 1]
         for text in texts]
for t in texts:
    print ' '.join(t)

# dictionary
dictionary = corpora.Dictionary(texts)
dictionary.save('data.dict')
print dictionary.token2id

# to bag of words
corpus = [dictionary.doc2bow(text) for text in texts]
corpora.MmCorpus.serialize('data.mm', corpus)
print corpus
