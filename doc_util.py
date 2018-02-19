from gingerit.gingerit import GingerIt
import language_check
tool = language_check.LanguageTool("en-US")
parser = GingerIt()
def sentence_correction(doc):
    matches = tool.check(doc)
    corrected_text = language_check.correct(doc, matches)
    corrected_text = parser.parse(corrected_text)
    return corrected_text['result']


from nltk.tokenize import sent_tokenize
def sentence_extractor(doc):
    return sent_tokenize(doc)

def correction_punctuation(text):
    import requests
    payload = [
        ('text', text),
    ]
    r = requests.post('http://bark.phon.ioc.ee/punctuator', data=payload)
    print r.text


#doc2 = "Clarify relationship between, in domain experts and modeler. Define role respons ibilities, desired workflow in group  Domain expert adds s g ob ject descriptions and relationships Modeler puts them into the overall model Then iteration What is the status of round trip? Drupal to xmi to EA? Yes.Is there  machine actionable feedback into Drupal? No. It is possible but some work is required. It is not clear yet if there is resources for these task. Furthermore there are different positions on the issue if the roundtrip makes sense."
# doc2 =" This is an example sent The sentence splitter will split on sent markers Ohh really !!"
# print sentence_correction(doc2)
