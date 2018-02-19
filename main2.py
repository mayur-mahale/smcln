from doc_util import  correction_punctuation, sentence_extractor
file = open('transcript.txt', 'r');
doc = file.read()
doc = correction_punctuation(doc)
doc_sentences = sentence_extractor(doc)

for sentences in doc_sentences:
    print sentences