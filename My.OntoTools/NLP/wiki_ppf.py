#wikipedia preprocessor filter

import wikipedia
from urllib.request import urlopen
from bs4 import BeautifulSoup

wikipedia.set_lang("en")

def get_most_popular():
    """
    366.(5)
    """
    page = urlopen('http://tools.wmflabs.org/wikitrends/2013.html')
    p = BeautifulSoup(page)
    links = p.find('table').findAll('a') + p.find('table', {'id':'tbl-en'}).findAll('a')
    return links

def get_random(count = 10):
    randPages = wikipedia.random(pages=count)
    for page in randPages:
        try:
            print(len(wikipedia.page(page).links))
        except wikipedia.DisambiguationError:
            print("DisambiguationError")

"""
ny = wikipedia.page("Solar system")
print("SUMMARY: ", wikipedia.summary("Solar system"))
print(ny.title)
print(ny.url)
print(ny.content.encode('ascii', 'ignore'))
print(len(ny.links))
for link in ny.links:
    print(link.encode('ascii', 'ignore'))
"""

pop = get_most_popular()
linksCountList = []
i = 0
for page in pop:
    try:
        i += 1
        title = page.getText()
        print(i, ') ', title.encode('ascii', 'ignore'))
        wp = wikipedia.page(title=title)
        linksCountList.append(len(wp.links))
    except wikipedia.DisambiguationError:
        pass

print(sum(linksCountList)/len(linksCountList))