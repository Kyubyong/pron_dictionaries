# Pronunciation Dictionaries for Multiple Languages

Pronunciation dictionaries can be used for several purposes. For example, one can convert text to a sequence of phonemes using them. Not surprisingly, you can freely access to a great English pronunciation dictionary provided by [CMU](https://github.com/cmusphinx/cmudict), although the pronunciation symbols are Arpabets, not IPAs. Again not surprisingly, it's hard to get pronunciation dictionaries for other languages. One reason is that for several languages their scripts are phonetic more or less; the pronunciation of a word can be inferred by some rules. However, neither rules always can cover everything nor everybody knows the rules. Decent and open-source pronunciation dictionaries are still necessary.

## Requirements
* lxml >= 3.3.3
* python >= 3.4
	
## References
* [CMU US English pronouncing dictionary](https://github.com/cmusphinx/cmudict)

## Work Flow
* STEP 1. Download the [wiktionary database backup dumps](http://ftp.acc.umu.se/mirror/wikimedia.org/dumps) of the language you want.
* STEP 2. Extract it to `data/raw/` folder.
* STEP 3. Run `build_corpus.py`.

## Pre-built dictionaries
Click the name of the language to download the prebuilt dictionary.

* [German](https://dl.dropboxusercontent.com/u/42868014/pron_dicts/de.csv.tar.gz)
* [Italian](https://dl.dropboxusercontent.com/u/42868014/pron_dicts/it.csv.tar.gz)
* [Spanish](https://dl.dropboxusercontent.com/u/42868014/pron_dicts/es.csv.tar.gz)
* [French](https://dl.dropboxusercontent.com/u/42868014/pron_dicts/fr.csv.tar.gz)
* [Polish](https://dl.dropboxusercontent.com/u/42868014/pron_dicts/pl.csv.tar.gz)
* [Finnish](https://dl.dropboxusercontent.com/u/42868014/pron_dicts/fi.csv.tar.gz)

## Note

Any contributions / error reports are welcome. We will keep adding languages.

## Disclaimer

We are not responsible for the content (headwords and pronunciations). They may contain mistakes and/or inconsistent use of symbols.



