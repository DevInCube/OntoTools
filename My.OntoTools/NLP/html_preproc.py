#@todo create link parser and filter for html docs general and for wikipedia in one case

from bs4 import BeautifulSoup
import re
from urllib.request import urlopen

def test():
    html_page = urlopen("http://en.wikipedia.org/wiki/Solar_System")
    soup = BeautifulSoup(html_page)
    bodyName = 'mw-content-text'
    soup = soup.find("div", {"id": bodyName})
    i = 0
    for link in soup.findAll('a'):
        i += 1
        title = link.get('title')
        ref = link.get('href')
        if not title : title = '<none>'
        if not ref : ref = '<none>'
        try:
            print(i, ') ', title, ' | ', ref)
        except:
            print('<error>')

def extract_links(html_page):        
    links = []
    soup = BeautifulSoup(html_page)
    for link in soup.findAll('a'):
        title = link.get('title')
        ref = link.get('href')
        if not title : 
            title = '<no-title>'
        if not ref : 
            ref = '<no-reference>'
        links.append((title, ref))
    return links