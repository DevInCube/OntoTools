from rdflib import Graph

online_path = 'http://lists.w3.org/Archives/Public/www-archive/2001Nov/att-0033/tab.rdf'
offline_path = 'Resources/tab.rdf'
g = Graph()
g.parse(offline_path, format="xml")

print(len(g))