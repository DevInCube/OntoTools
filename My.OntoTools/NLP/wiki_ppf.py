#wikipedia preprocessor filter

import wikipedia
from urllib.request import urlopen
from bs4 import BeautifulSoup
from nltk import word_tokenize

wikipedia.set_lang("en")

def get_most_popular():
    """
    366.(5) links in average
    """
    page = urlopen('http://tools.wmflabs.org/wikitrends/2013.html')
    p = BeautifulSoup(page)
    links = p.find('table').findAll('a') + p.find('table', {'id':'tbl-en'}).findAll('a')
    return links

def filter_links(wiki_page):
    """
    get only most important links from wiki page     
    #print(*flinks, sep="\n")   
    """
    flinks = set()
    for tword in word_tokenize(wiki_page.title):
        [flinks.add(l) for l in wiki_page.links if re.search(tword, l, re.IGNORECASE)]
    return flinks

def get_random(count = 10):
    """
    max count is 10
    """
    randPages = wikipedia.random(pages=count)
    for page in randPages:
        try:
            print(len(wikipedia.page(page).links))
        except wikipedia.DisambiguationError:
            print("DisambiguationError")

def count_avg_links():
    pop = get_most_popular()
    linksCountList = []
    i = 0
    for page in pop:
        try:
            i += 1
            title = page.getText()        
            wp = wikipedia.page(title=title)
            lens = len(wp.links)
            linksCountList.append(lens)
            print(i, ') ', title.encode('ascii', 'ignore'), '\t', lens)
        except wikipedia.DisambiguationError:
            pass
    return sum(linksCountList)/len(linksCountList)

print(count_avg_links())