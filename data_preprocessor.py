from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import string

stop = set(stopwords.words('english'))
exclude = set(string.punctuation)
lemma = WordNetLemmatizer()

def __clean(doc):
    stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
    print "After stop word cleaning\n"+ stop_free
    punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
    print "After removing punctuation \n"+ punc_free
    normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
    print "After lemmatizing \n" + normalized
    return normalized

def clean_documents(docs):
    doc_clean = [__clean(doc).split() for doc in docs]
    print "After lemmatizing all docs \n"
    print doc_clean
    return doc_clean