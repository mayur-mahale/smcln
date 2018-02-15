import gensim
#
from gensim import corpora
from gensim import models
#
#
def topic_generator(docs):
    dictionary = corpora.Dictionary(docs)
    doc_term_matrix = [dictionary.doc2bow(doc) for doc in docs]
    print doc_term_matrix
    Lda = models.LdaModel
    ldamodel = Lda(doc_term_matrix, num_topics=3, id2word = dictionary, passes=50)
    print(ldamodel.print_topics(num_topics=3, num_words=10))