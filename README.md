# Pronunciation Dictionaries for Multiple Languages

Pronunciation dictionaries can be used for several purposes. For example, one can convert text to a sequence of phonemes using them. Not surprisingly, you have free access to a great English pronunciation dictionary provided by [CMU](https://github.com/cmusphinx/cmudict), although the pronunciation symbols are Arpabets, not IPAs. Again not surprisingly, it's hard to get pronunciation dictionaries for other languages. One reason is that for several languages their scripts are phonetic more or less; the pronunciation of a word can be inferred by some rules. However, rules often fail to cover everything. Besides, not everybody is aware of them. Decent open-source pronunciation dictionaries are still necessary.

## Requirements
* lxml >= 3.3.3
* python >= 3.4
	
## References
* [CMU US English pronouncing dictionary](https://github.com/cmusphinx/cmudict)

## Work Flow
* STEP 1. Download the [wiktionary database backup dumps](http://ftp.acc.umu.se/mirror/wikimedia.org/dumps) of the language you want.
* STEP 2. Extract it to `data/raw/` folder.
* STEP 3. Run `make_dictionary.py`.

## Pre-built dictionaries
Click the name of the language to download the prebuilt dictionary.

* [German](https://www.dropbox.com/s/p38ercjip9gzj7g/de.csv.tar.gz?dl=0)
* [Italian](https://www.dropbox.com/s/vwtg4iphwpz1b7h/it.csv.tar.gz?dl=0)
* [Spanish](https://www.dropbox.com/s/r14cfgs0jjal2ta/es.csv.tar.gz?dl=0)
* [French](https://www.dropbox.com/s/22zicbk4t9kx1pl/fr.csv.tar.gz?dl=0)
* [Polish](https://www.dropbox.com/s/6uqhwjc3xz23pyr/pl.csv.tar.gz?dl=0)
* [Finnish](https://www.dropbox.com/s/du2k9p3ovpgeou6/fi.csv.tar.gz?dl=0)
* [Korean](https://dl.dropboxusercontent.com/s/346v029h4fthgx4/ko.csv.tar.gz)
* [Turkish](https://dl.dropboxusercontent.com/s/7gzitspqhyw0405/tr.csv.tar.gz)
* [Portuguese](https://dl.dropboxusercontent.com/s/m837tkkclfxswp8/pt.csv.tar.gz)
* [Russian](https://dl.dropboxusercontent.com/s/4j433o46ipcq1cj/ru.csv.tar.gz)

## Note

We will keep adding languages. Any contributions / error reports are welcome. 

## Disclaimer

We are not responsible for the content (headwords and pronunciations). They may contain mistakes made by us or the original creator.



