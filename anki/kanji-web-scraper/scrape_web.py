import csv
from dataclasses import dataclass, asdict
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
        # Get the starting position (expected type: `<h4>`)
        current_pos = hiragana_section.find_next_sibling()
        while current_pos is not None:
            # If we reached the next hiragana section, break out of the loop
            if current_pos.name == "img":
                log.info("Breaking out of this hiragana section")
                log.info("-----")
                break

            # Check that the first element is an `<h4>`
            if current_pos.name != "h4":
                # TODO: find better way to leave loop
                current_pos = current_pos.find_next_sibling()
                continue

            # Extract the term and the furigana from the h4 heading
            # The string format is: "term (furigana)"
            heading = current_pos.get_text()
            term_and_furigana = re.search(r"([一-龯]+)（([ぁ-ん]+)）", heading)
            term = term_and_furigana.group(1)
            furigana = term_and_furigana.group(2)
            log.info(f"Got term: {term}, furigana: {furigana}")

            # Get the definition (which is a `<p>` that comes right after the `<h4>`)
            current_pos = current_pos.find_next_sibling()
            if current_pos.name != "p":
                log.error(f"No definition was found for {term}")
                # TODO: find better way to leave loop
                current_pos = current_pos.find_next_sibling()
                continue

            definition = current_pos.get_text()
            log.info(f"Got definition: {definition}")

            if current_pos.find_next_sibling().name == "hr":
                log.info("End of kanji entry")
            else:
                log.info("Extra notes found")
                # TODO: get the notes section

            # Create a kanji entry object and save it
            kanji_entry = KanjiEntry(term=term, furigana=furigana, definition=definition, notes="")
            kanji_entries.append(kanji_entry)
            log.info("-----")

            # Move to the next entry
            current_pos = current_pos.find_next_sibling()

    log.info(f"Created {len(kanji_entries)} kanji entries")
    return kanji_entries


def export_to_csv(kanji_entries):
    """Export kanji entries to a csv file"""
    header = ["term", "furigana", "definition", "notes"]
    outfile_name = "kanji.csv"
    with open(outfile_name, 'w', encoding="UTF8", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        for kanji_entry in kanji_entries:
            row = [asdict(kanji_entry)]
            writer.writerows(row)

    log.info(f"Exported kanji entries to: {outfile_name}")


def main():
    if len(sys.argv) < 2:
        log.error("Missing webpage URL to scrape")
        return 1

    url = sys.argv[1]
    kanji_entries = get_kanji_entries(url)
    export_to_csv(kanji_entries)


if __name__ == "__main__":
    sys.exit(main())
