class FindResult(object):
    """description of class"""

    def __init__(self, title, url, content):
        self.title = title
        self.url = url
        self.content = content

    def __repr__(self):
        return self.title + ':' + self.url + '\r\n' + self.content

