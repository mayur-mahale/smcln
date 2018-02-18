import spacy
from spacy import displacy
from spacy.lang.en import English
import doc_util
import en_core_web_sm
nlp = English()
doc = "Do n't look, I'll give yo all the details however you mite need  to go through it ones .Apple is looking at buying U.K. startup for $1 billon."
doc = doc_util.sentence_correction(doc)
print doc
doc = nlp(doc)
lemmas = [token.lemma_ for token in doc if not token.is_stop]
print lemmas