import sys
import requests
import re
from urllib.parse import urljoin
from html.parser import HTMLParser


class PageReader(HTMLParser):
    def __init__(self, base):
        super().__init__()
        self.base = base
        self.in_title = False
        self.in_body = False
        self.title_text = ""
        self.body_text = []
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == "title":
            self.in_title = True
        if tag == "body":
            self.in_body = True
        if tag == "a":
            for k, v in attrs:
                if k == "href":
                    self.links.append(urljoin(self.base, v))

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False
        if tag == "body":
            self.in_body = False

    def handle_data(self, data):
        if self.in_title:
            self.title_text += data.strip()
        if self.in_body:
            cleaned = data.strip()
            if cleaned:
                self.body_text.append(cleaned)


def main():

    if len(sys.argv) < 2:
        print("Enter URL")
        return

    u = sys.argv[1]
    if not u.startswith(("http://", "https://")):
        u = "https://" + u

    try:
        page = requests.get(u, timeout=5)
    except:
        print("Failed")
        return

    parser = PageReader(u)
    parser.feed(page.text)

    print(parser.title_text if parser.title_text else "No title")
    print("\n".join(parser.body_text) if parser.body_text else "No body")

    for link in parser.links:
        print(link)


if __name__ == "__main__":
    main()