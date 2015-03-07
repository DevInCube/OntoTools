import nltk, re, pprint

class infoex(object):
    """Information Extractor"""

    def __init_():
        pass

    def __preprocess(document):
        sentences = nltk.sent_tokenize(document) [1]
        sentences = [nltk.word_tokenize(sent) for sent in sentences] [2]
        sentences = [nltk.pos_tag(sent) for sent in sentences] 


