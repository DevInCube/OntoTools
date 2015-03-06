from nltk.book import text1

import nltk, re, pprint
from nltk import word_tokenize

print('Hello World')


def lexical_diversity(text):
    """
    Lexical divercity docs
    """
    return len(set(text)) / len(text)

# an idea: get less frequent words, mark them as 'external terms' #fdist1.hapaxes()
# then foreach term if it has bigger similarity with other words 
# it's more 'internal' term

fdist1 = FreqDist(text1)
print(fdist1)
fdist1.most_common(10)
fdist1.hapaxes(10)
V = set(text1)
long_words = [w for w in V if len(w) > 15]
#get text.collocations()

#@todo prepare own corpora of domain texts
#install plot and show statistical and graphical 
#features of my corpora

stopwords = nltk.corpus.stopwords.words('english')
content = [w for w in text1 if w.lower() not in stopwords]

from nltk.corpus import wordnet as wn

wn.synsets('motorcar')
wn.synset('car.n.01').lemma_names()
wn.synset('car.n.01').definition()
wn.synset('car.n.01').examples()

#idea text glue each word or collocation with ONLY one meaning is glued into one node 
#and keeps every relation to each place in text where it appeared
#we should save sentence position on relation
#if word is ambiguous every its instance may create an n-gram with glue float value (0..1) 

tokens = word_tokenize(raw)
text = nltk.Text(tokens)

#NLP pipeline
#HTML -> Text
html = urlopen(url).read()
raw=nltk.clean_html(html)
tokens = nltk.wordpunct_tokenize(raw)
text = nltk.Text(raw)
#text to vocab
words = [w.lower() for w in text]
vocab = sorted(set(words))

#Searching Tokenized Text
text1.findall(r"<a> (<.*>) <man>")
text1.findall(r"<h.*>{3,}")

#stemming
porter = nltk.PorterStemmer()
lancaster = nltk.LancasterStemmer()
[porter.stem(t) for t in tokens]

wnl = nltk.WordNetLemmatizer()
[wnl.lemmatize(t) for t in tokens]

#sentences
sents = nltk.sent_tokenize(text)

#lambda
list(map(lambda w: len(filter(lambda c: c.lower() in "aeiou", w)), sent))

#visual Graphs NetworkX

#POS tagger
nltk.pos_tag(text)