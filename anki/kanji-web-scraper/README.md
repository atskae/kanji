# Kanji Web Scraper

This script reads in selected webpages under [Kanji by Grade Levels](#kanji-by-grade-levels) and outputs a `.csv` file with the format:

```csv
term,furigana,definition,notes,warnings,example1,example2
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

Where `<url>` is any webpage under [Kanji by Grade Levels](#kanji-by-grade-levels)

The output file `kanji.csv` will be generated.

For Grades 1-3, run:
```commandline
 python scrape_web.py https://proverb-encyclopedia.com/two/teigakunen/
```

For Grades 4-6, run:
```commandline
python scrape_web.py https://proverb-encyclopedia.com/two/kougakunen/
```

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

### The "notes" Section

There are various types of "notes" (anything that come after the definition in `<p>`):

* **Example sentences** always start with `"例文"` and contains a list:
```html
 <p>
  <strong>
   【例文】
  </strong>
 </p>
 <ol>
  <li>
   校舎とグラウンドを何度も
   <span style="color: #ff0000;">
    往復
   </span>
   する。
  </li>
  <li>
   一
   <span style="color: #ff0000;">
    往復
   </span>
   するのに３０分かかる。
  </li>
 </ol>
```
There seems to always be at most 2 example sentences.

* **Supplement normal** (yellow rectangles containing text)
```html
 <div class="supplement normal">
  特別な読みで、「きのう」とも読む。
 </div>
```

* **Supplement warning** (red rectangles containing text)

```html
 <div class="supplement warning">
  「遅」という漢字は、小学生では習いません。
 </div>
```

### Japanese Regex
* [Regex patterns for Japanese](https://gist.github.com/terrancesnyder/1345094)

I spent way to long trying to figure out why my pattern was not matching. TIL `）` is not the same parenthesis as `)` OTL

The following pattern:
```python
r"([一-龯]+)（([ぁ-ん]+)）"
```

matches strings like `"約束（やくそく）"`, `"永遠（えいえん）"`, etc.
