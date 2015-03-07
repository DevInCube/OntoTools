import nltk, re, pprint

def chunker(tagsetset, pattern):
    """
    tagsetset - nltk.corpus.brown.tagged_sents()
    pattern - 'CHUNK: {<V.*> <TO> <V.*>}'
    """
    cp = nltk.RegexpParser(pattern)
    tree = cp.parse(tagsetset[0])
    for subtree in tree.subtrees():
        print(subtree.label())

chunker(nltk.corpus.brown.tagged_sents(), 'CHUNK: {<V.*> <TO> <V.*>}')