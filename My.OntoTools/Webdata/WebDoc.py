import sys
import nltk
from bs4 import BeautifulSoup
#import html_preproc

class WebDoc(object):
    """description of class"""

    def __init__(self, meta, text, html, links):
        self.meta = meta
        self.text = text
        self.html = html
        self.links = links
    
    def prepare(self):
        if not self.text:
            text = BeautifulSoup(self.html).get_text()
            self.text = text
        #if not self.links:
            #self.links = html_preproc.extract_links(self.html)

    def tokenize(self):
        tokens = nltk.wordpunct_tokenize(self.text)
        return tokens


if __name__ == "__main__":
    with open("Resources/solar.html", "r", encoding='latin2') as html:
        # The NLP Pipeline, building a vocabulary 
        doc = WebDoc(None, None, html, None)
        doc.prepare()
        tokens = doc.tokenize()
        print(doc.text)
        text = nltk.Text(tokens)
        words = [w.lower() for w in text]
        vocab = sorted(set(words))