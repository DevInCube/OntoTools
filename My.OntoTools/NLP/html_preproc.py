#@todo create link parser and filter for html docs general and for wikipedia in one case

from bs4 import BeautifulSoup
import re
from urllib.request import urlopen

html_page = urlopen("http://en.wikipedia.org/wiki/Solar_System")
soup = BeautifulSoup(html_page)
bodyName = 'mw-content-text'
soup = soup.find("div", {"id": bodyName})
i = 0
for link in soup.findAll('a'):
    i += 1
    title = link.get('title')
    text = link.getText()
    ref = link.get('href')
    if not title : title = '<none>' #images
    if not text : title = '<none>'
    if not ref : ref = '<none>'
    try:
        print(i, ') ', title, ' (', text,') ', ' | ', ref)
    except:
        print('<error>')