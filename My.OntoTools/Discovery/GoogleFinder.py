import re
import json
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import urlencode

from IFinder import IFinder
from FindResult import FindResult

class GoogleFinder(IFinder):
    """ Google """

    def search(self, query):
        google_api_url = 'http://ajax.googleapis.com/ajax/services/search/web'
        urlparams = { 'v' : '1.0', 'q' : query, 'rsz' : 'large' }
        urlparams_encoded = urlencode(urlparams)
        url = '%s?%s' % (google_api_url, urlparams_encoded)

        html_page = urlopen(url)
        soup = BeautifulSoup(html_page)
        jres = json.loads(soup.decode('utf-8'))
        results = jres.get('responseData').get('results')

        data = []

        for result in results:
            title = result.get('title')
            url = result.get('url')
            content = result.get('content')
            data.append(FindResult(title, url, content))

        return data

if __name__ == "__main__":
    finder = GoogleFinder()
    links = finder.search('Solar system')
    for link in links:
        print(str(link) + '\r\n')