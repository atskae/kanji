# Kanji Web Scraper

This script reads in selected webpages under [Kanji by Grade Levels](#Kanji by Grade Levels) and outputs a `.csv` file with the format:

```csv
term,furigana,definition,notes
```

## How to Use

Check that you are running Python 3:
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

The output file `kanji.csv` will be generated.

## Kanji by Grade Levels

* [Grades 1-3](https://proverb-encyclopedia.com/two/teigakunen/)
* [Grades 4-6](https://proverb-encyclopedia.com/two/kougakunen/)

## Dev Notes
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

### Japanese Regex
* [Regex patterns for Japanese](https://gist.github.com/terrancesnyder/1345094)

I spent way to long trying to figure out why my pattern was not matching. TIL `）` is not the same parenthesis as `)` OTL

The following pattern:
```python
r"([一-龯]+)（([ぁ-ん]+)）"
```

matches strings like `"約束（やくそく）"`, `"永遠（えいえん）"`, etc.
