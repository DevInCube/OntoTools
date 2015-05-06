import nltk, re, pprint
from nltk.tokenize import word_tokenize

sentence = "In computer science and information science, an ontology is a formal naming and definition of the types, properties, and interrelationships of the entities that really or fundamentally exist for a particular domain of discourse"

sent = word_tokenize(sentence)
print(nltk.pos_tag(sent))
"""
RDF/XML Syntax

<Definition rdf:about="Ontology">
    <rdf:Description>
       <mAttr:isA rdf:resource="Definition"/>
       <mAttr:contains rdf:resource="Type"/>
       <owl:differentFrom rdf:resource="Ontology (philosophical study)"/>
    </rdf:Description>
    <mAttr:Links>
        <mAttr:Link rdf:resource:="http://en.wikipedia.org/wiki/Ontology_(information_science)"/>
    </mAttr:Links>
</Definition>

"""