# Kanji Web Scraper

This script reads in selected webpages under [Kanji by Grade Levels](#Kanji by Grade Levels) and outputs a `.csv` file with the format:

```csv
term,furigana,definition,notes
```

## How to Use

Ensure you are running Python 3:
```commandline
python --version
```

Note that this script has only been tested with Python `3.9.2` on MacOS.

Install the package requirements:
```commandline
pip install -r requirements.txt
```

Then run:
```commandline
python scrape_web.py <url>
```

Where `<url>` is any webpage under [Kanji by Grade Levels](#Kanji by Grade Level)

## Kanji by Grade Levels

* [Grades 1-3](https://proverb-encyclopedia.com/two/teigakunen/#i)
* [Grades 4-6](https://proverb-encyclopedia.com/two/kougakunen/)


## Notes
All the cards are in an `<article>` under `<main>`.

Each card format is roughly:
```html
        <h4>
         悪意（あくい）
        </h4>
        <p>
         人に害をあたえようとする気持ち。
        </p>
        <hr/>
```

The card ends when we see a `<hr/>`
