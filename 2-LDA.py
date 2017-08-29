# coding=utf-8
import logging, gensim, bz2
from gensim import corpora, models, similarities

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

"""适合batch、不适合online，即适合数据稳定时用，当数据是增量时用lsa
be careful if using LDA to incrementally add new documents to the model over time. Batch usage of LDA
"""
# prepare data
id2word = corpora.Dictionary.load('data.dict')
mm = gensim.corpora.MmCorpus('data.mm')
print mm

# train
lda = gensim.models.ldamodel.LdaModel(
    corpus=mm,
    id2word=id2word,
    num_topics=5,
    update_every=1,
    chunksize=3,
    passes=10)

lda.save('model.lda')

print '---------print_topics:'
print lda.print_topics(num_topics=5, num_words=2)
print '---------show_topics: '
for topic in lda.show_topics(num_topics=-1, num_words=2, formatted=False):
    print 'topic: ', topic[0]
    for word_weight in topic[1]:
        print word_weight[0], word_weight[1]

# use
print '-----'
lda = gensim.models.LdaModel.load('model.lda')
doc_lda = lda[mm]
for topic in lda.show_topics(num_topics=-1, num_words=10, formatted=True):
    print topic[0], ':', topic[1].encode('utf-8')