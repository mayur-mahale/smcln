
doc1 = "Status update. Where are we now with SimpleDataDescription?"
doc2 = "Clarify relationship between domain experts and modeler. " \
       "Define role responsibilities, desired workflow in group  Domain expert adds object descriptions and relationships Modeler puts them into the overall model Then iteration What is the status of round trip? " \
       "Drupal to xmi to EA? Yes.Is there  machine actionable feedback into Drupal? No. " \
       "It is possible but some work is required. " \
       "It is not clear yet if there are resources for this task. " \
       "Furthermore there are different positions on the issue if the roundtrip makes sense."

doc3 = "Doctors suggest that driving may cause increased stress and blood pressure."
doc4 = "Sometimes I feel pressure to perform well at school, but my father never seems to drive my sister to do better."
doc5 = "Health experts say that Sugar is not good for your lifestyle."

doc_complete = [doc1, doc2, doc3, doc4, doc5]

from data_preprocessor import clean_documents
from topic_modeler import topic_generator

cleaned_docs = clean_documents(doc_complete)
topic_generator(cleaned_docs)
