# Resources
Compiled list of my notes and reading. Paper notes are named with the same name as the PDF in `papers/`, but as a Markdown file `.md`.
* `papers/` contain research papers for offline reading

## Kanji Libraries and Datasets

### Handwriting Recognition
* [Zinnia](http://taku910.github.io/zinnia/) library seems popular with mobile apps (for [Swift](https://github.com/tuanna-hsp/kanji-handwriting-swift), [Android](https://github.com/ichisadashioko/kanji-recognition-android), [Java](https://github.com/quen/kanjirecog))
* [Tegaki Project](https://tegaki.github.io/) (which actually uses Zinnia), also called Wagomu
    * [ctegaki](https://github.com/asdfjkl/ctegaki-lib) by the author of the `klein2019.pdf` paper [stroke correspondence problem, revisited](https://arxiv.org/pdf/1909.11995.pdf)
* [KanjiVG](https://github.com/KanjiVG/kanjivg): stroke order and vectors of kanji

### Other
* A lot of information on kanji datasets from [Jisho About page](https://jisho.org/about), including:
    * Kanji readings
    * Stroke order
    * Example sentences
    * Radicals
    * Stroke order (KanjiVG)
* [Pykakasi](https://github.com/miurahr/pykakasi): Python library for kanji/kana conversion (text-based only)

## Kanji Apps
Helpful to study how other apps includes the kanji recognition feature
* [Jisho](https://jisho.org) 
* [Kanji Canvas](https://asdfjkl.github.io/kanjicanvas/) and [source](https://github.com/asdfjkl/kanjicanvas) (author of `klein2019.pdf` paper)
* [Kanji Recognizer](https://sites.google.com/site/kanjirecognizer/acknowledgments?authuser=0)
* [Japanese app](https://www.japaneseapp.com/sources/)
* [Kanji alive](https://github.com/kanjialive/)

## Reading
* Many [algorithms on kanji](https://scholar.google.com/scholar?hl=en&as_sdt=0,33&q=kanji+algorithm) just with a quick Google Scholar search
    * [Stroke Correspondence Problem, Revisited](https://arxiv.org/pdf/1909.11995.pdf) Dec 2019, which cites Zinnia and the Tegaki Project
* [GitHub search on kanji](https://github.com/search?q=kanji)
* A class report on using [CNNs to recognize kanji](http://cs231n.stanford.edu/reports/2016/pdfs/262_Report.pdf)
    * This method is for recognizing kanji *already drawn*, versus recognizing kanji drawn on the fly (and filtering out kanji based on the current strokes drawn)
        * How different are these two methods?
* [Tutorial on using CNN to recognize hiragana/katagana](https://www.freecodecamp.org/news/build-a-handwriting-recognizer-ship-it-to-app-store-fcce24205b4b/)
* [Japanese language and computers](https://en.wikipedia.org/wiki/Japanese_language_and_computers), which is about how Japanese characters are encoded into bytes.
