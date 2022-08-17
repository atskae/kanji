import logging
import sys

from bs4 import BeautifulSoup
import requests


logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)


def get_csv(url: str):
    """Create a CSV object from a URL"""
    response = requests.get(url)
    log.info(f"Obtained contents of {url}")

    webpage = BeautifulSoup(response.text, 'html.parser')
    log.info(f"Webpage title: {webpage.title}")

    print(webpage.prettify())


def main():
    if len(sys.argv) < 2:
        log.error("Missing webpage URL to scrape")
        return 1

    url = sys.argv[1]
    kanji_csv = get_csv(url)


if __name__ == "__main__":
    sys.exit(main())
