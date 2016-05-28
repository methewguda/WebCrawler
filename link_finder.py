from html.parser import HTMLParser
from urllib import parse

class LinkFinder(HTMLParser):
    def __init__(self):
        super().__init__()

    def handle_startendtag(self, tag, attrs):
        print(tag)

    def error(self, message):
        pass
