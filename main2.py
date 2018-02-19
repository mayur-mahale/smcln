from doc_util import  correction_punctuation, sentence_extractor
file = open('transcript.txt', 'r');
doc = file.read()
doc = correction_punctuation(doc)
doc_sentences = sentence_extractor(doc)

for sentence in doc_sentences:
    print sentence

from data_preprocessor import clean_documents
from doc_util import sentence_correction
from topic_modeler import topic_generator
print  "************applying corrections"
corrected_docs = [sentence_correction(sentence) for sentence in doc_sentences]
print corrected_docs
clean_documents = [clean_documents(doc) for doc in corrected_docs]
topic_generator(clean_documents)