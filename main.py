import sys
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def main():

    if len(sys.argv) < 2:
        print("Enter URL")
        return

    url = sys.argv[1]

    page = requests.get(url)
    html = page.text

    soup = BeautifulSoup(html, "html.parser")


    # title
    t = soup.find("title")

    if t:
        print(t.text)
    else:
        print("No title")


    # body text
    body = soup.find("body")

    if body:
        text = body.get_text()
        print(text)
    else:
        print("No body")


    print("Links:")

    links = soup.find_all("a")

    for i in links:

        href = i.get("href")

        if href:
            full = urljoin(url, href)
            print(full)


if __name__ == "__main__":
    main()