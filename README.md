# Kanji

I have been attempting to learn Japanese kanji and became curious about how a computer deals with kanji. The goal of this project is to answer two main questions:
1. When I draw out kanji, how does the computer figure out what kanji was drawn?
    * For example, how does the [Draw feature on Jisho](https://jisho.org/#handwriting) work? (I asked them this, let's see if they respond).
2. When I start typing in hiragana, how does the computer filter out the kanjis?
    * This just seems to be a one-to-many mapping between hiragana and possible kanji ([Wikipedia article on this](https://en.wikipedia.org/wiki/Japanese_input_method#Kana_to_kanji_conversion)).
    * How does the computer deal with onyomi and kunyomi readings (especially when they mix)? Are all of the possible combinations really stored in some map?

## Mini Goals
- [x] Do basic research on what kanji libraries exist
- [ ] Read some research papers and articles on the algorithms behind kanji handwriting recognition
- [ ] Install a basic kanji handwriting library in some app (Android, web, etc.) and try using it

## Repository Organization
* `res/` contains resources that I used for learning, and my notes on some reading
* `doc/` documentation on any code I write, such as for `KanjiDrawer`
* `KanjiDrawer` Android app to test out a kanji recognition library

## Random Thought
* How would I generate a 巨大 graph of all the kanji (including compounds) and connect words based on the kanji in that word? Is this even possible?
    * So one of many words that 目 would connect with would be 種目, then this word can connect with 目次, etc...
* This would be helpful for learning new words. For example, let's use 種目 (しゅもく) again. This word uses the onyomi シュ. A kanji with that onyomi is 種類 - しゅるい - species, types of. The second part 目 uses the onyomi モク (same as 目的)
* There *would* be repeats I guess...
