import csv
from dataclasses import dataclass
import logging
import re
import sys
from typing import List

from bs4 import BeautifulSoup
import requests


logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)


@dataclass
class KanjiEntry:
    term: str
    furigana: str
    definition: str
    notes: str


def get_kanji_entries(url: str) -> List[KanjiEntry]:
    """Create a list of KanjiEntry objects from the webpage"""
    response = requests.get(url)
    log.info(f"Obtained contents of {url}")

    webpage = BeautifulSoup(response.text, 'html.parser')
    log.info(f"Webpage title: {webpage.title}")

    # Narrow down the webpage content to the kanji section
    kanji_section = webpage.find("section", {"class": "entry-content cf"})

    # Each hiragana section starts with an `<img>`
    hiragana_sections = kanji_section.find_all("img", {"height": 110})
    log.info(f"Found {len(hiragana_sections)} hiragana sections")

    # Each kanji entry starts with a `<h4>` and ends with a `<hr/>
    # Iterate through each hiragana section
    kanji_entries = []
    for hiragana_section in hiragana_sections:
        first_entry = hiragana_section.find_next_sibling()
        # Check that the entry is an `<h4>`
        if first_entry.name != "h4":
            continue

        # Extract the term and the furigana
        # The string format is: term (furigana)
        first_entry_text = first_entry.get_text()
        print(f"<h4> contents: {first_entry_text}")
        term_and_furigana = re.search(r"([一-龯]+)（([ぁ-ん]+)）", first_entry.get_text())
        term = term_and_furigana.group(1)
        furigana = term_and_furigana.group(2)

        print(f"Got term {term}, furigana {furigana}")


    return kanji_entries


def main():
    if len(sys.argv) < 2:
        log.error("Missing webpage URL to scrape")
        return 1

    url = sys.argv[1]
    kanji_entries = get_kanji_entries(url)


if __name__ == "__main__":
    sys.exit(main())
