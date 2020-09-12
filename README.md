# Kanji

I have been attempting to learn Japanese kanji and became curious about how a computer deals with kanji. The goal of this project is to answer two main questions:
1. When I draw out kanji, how does the computer figure out what kanji was drawn?
    * For example, how does the [Draw feature on Jisho](https://jisho.org/#handwriting) work? (I asked them this, let's see if they respond).
2. When I start typing in hiragana, how does the computer filter out the kanjis?
    * This just seems to be a one-to-many mapping between hiragana and possible kanji ([Wikipedia article on this](https://en.wikipedia.org/wiki/Japanese_input_method#Kana_to_kanji_conversion)).
    * How does the computer deal with onyomi and kunyomi readings (especially when they mix)? Are all of the possible combinations really stored in some map?

## Repository Organization
* `doc/` contains documentation and resources that I used, and my notes on some reading
