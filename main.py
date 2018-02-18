
doc1 = "Status update. Where are  now with SimpleDataDescription?"
doc2 = "Clarify relationship between in domain experts and modeler. " \
       "Define role respons ibilities, desired workflow in group  Domain expert adds s g ob ject descriptions and relationships Modeler puts them into the overall model Then iteration What is the status of round trip? " \
       "Drupal to xmi to EA? Yes.Is there  machine actionable feedback into Drupal? No. " \
       "It is possible but some work is required. " \
       "It is not clear yet if there is resources for these task. " \
       "Furthermore there are different positions on the issue if the roundtrip makes sense."

doc3 = "Doctors suggest that driving may cause increased stress and blood pressure."
doc4 = "Sometimes I feel pressure to perform well at school, but my father never seems to drive my sister to do better."
doc5 = "Health experts say that Sugar is not good for your lifestyle."

doc_complete = [doc1, doc2, doc3, doc4, doc5]
print doc_complete
from doc_util import sentence_correction
from data_preprocessor import clean_documents
from topic_modeler import topic_generator
corrected_docs = [sentence_correction(doc) for doc in doc_complete]
print corrected_docs
cleaned_docs = clean_documents(corrected_docs)
topic_generator(cleaned_docs)
