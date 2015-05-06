import wikipedia
import sys

from IFinder import IFinder
from FindResult import FindResult


class WikipediaFinder(IFinder):
    """description of class"""

    def search(self, query):

        data = []

        result_pages = wikipedia.search(query)
        result_pages = result_pages[:8]

        for page_name in result_pages:
            page = wikipedia.page(page_name)
            title = page.title
            url = page.url
            content = "..."
            data.append(FindResult(title, url, content))

        return data

if __name__ == "__main__":
    finder = WikipediaFinder()
    links = finder.search('Solar system')
    for link in links:
        print(str(link) + '\r\n')