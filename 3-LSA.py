# coding=utf-8
import logging, gensim, bz2
from gensim import corpora, models, similarities

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

"""适合online，当数据是增量时用
so it is suitable for environments where the documents come as a non-repeatable stream
"""
# prepare data
id2word = corpora.Dictionary.load('data.dict')
mm = gensim.corpora.MmCorpus('data.mm')
print mm

# train: latent semantic indexing
lsi = gensim.models.lsimodel.LsiModel(corpus=mm, id2word=id2word, num_topics=5)
lsi.save('model.lsi')

print '---------print_topics:'
print lsi.print_topics(num_topics=5, num_words=2)
print '---------show_topics: '
for topic in lsi.show_topics(num_topics=-1, num_words=2, formatted=False):
    print 'topic: ', topic[0]
    for word_weight in topic[1]:
        print word_weight[0], word_weight[1]

# use
print '-----'
lsi = gensim.models.LsiModel.load('model.lsi')
doc_lda = lsi[mm]
for topic in lsi.show_topics(num_topics=-1, num_words=10, formatted=True):
    print topic[0], ':', topic[1].encode('utf-8')
