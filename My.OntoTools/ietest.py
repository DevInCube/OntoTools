import nltk, re, pprint

sentence = [("the", "DT"), ("little", "JJ"), ("yellow", "JJ"),
            ("dog", "NN"), ("barked", "VBD"), ("at", "IN"),  ("the", "DT"), ("cat", "NN")]

grammar = "NP: {<DT>?<JJ>*<NN>}"

cp = nltk.RegexpParser(grammar)
result = cp.parse(sentence)

#print(result)

#result.draw()


def chunker(tagsetset, pattern):
    """
    tagsetset - nltk.corpus.brown.tagged_sents()
    pattern - 'CHUNK: {<V.*> <TO> <V.*>}'
    """
    cp = nltk.RegexpParser(pattern)
    for sent in tagsetset:
        tree = cp.parse(sent)
        for subtree in tree.subtrees():
            if subtree.label() == 'CHUNK':
                print(subtree)

chunker(nltk.corpus.brown.tagged_sents(), 'CHUNK: {<V.*> <TO> <V.*>}')