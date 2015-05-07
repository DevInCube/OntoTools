import nltk
from nltk.corpus import brown

class WordLexer(object):
    """word lexer"""

    def __init__(self):
        self._porter = nltk.PorterStemmer()

    def stem(self, word):
        return self._porter.stem(word)

pattern = r'''(?x)        # set flag to allow verbose regexps
        ([A-Z]\.)+        # abbreviations, e.g. U.S.A.
      | \w+(-\w+)*        # words with optional internal hyphens
      | \$?\d+(\.\d+)?%?  # currency and percentages, e.g. $12.40, 82%
      | \.\.\.            # ellipsis
      | [][.,;"'?():-_`]  # these are separate tokens; includes ], [
    '''

def regex_tokenize(text):
    return nltk.regexp_tokenize(text, pattern)

def sent_tokenize(text):
    return nltk.sent_tokenize(text)

def tag_text(text):
    """
    POS-tagger, processes a sequence of words, and attaches a part of speech tag to each word 
    """
    return nltk.pos_tag(text)

def simple_tag(sent):
    patterns = [
        (r'.*ing$', 'VBG'),               # gerunds
        (r'.*ed$', 'VBD'),                # simple past
        (r'.*es$', 'VBZ'),                # 3rd singular present
        (r'.*ould$', 'MD'),               # modals
        (r'.*\'s$', 'NN$'),               # possessive nouns
        (r'.*s$', 'NNS'),                 # plural nouns
        (r'^-?[0-9]+(.[0-9]+)?$', 'CD'),  # cardinal numbers
        (r'.*', 'NN')                     # nouns (default)
    ]
    regexp_tagger = nltk.RegexpTagger(patterns)
    return regexp_tagger.tag(sent)

def chunk(sentence):
    grammar = "NP: {<DT>?<JJ>*<NN>}" # Noun Phrase Chunking
    cp = nltk.RegexpParser(grammar)
    result = cp.parse(sentence)
    return result

if __name__ == "__main__":
    sent = nltk.word_tokenize("Hello my old friend")
    tagged_sent = tag_text(sent);
    print(chunk(tagged_sent))