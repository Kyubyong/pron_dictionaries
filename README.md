# Pronunciation Dictionaries for multiple languages

Pronunciation dictionaries can be used for several purposes. Among them is Text-to-Speech. Generally speaking, you can't directly convert text to sound. Instead, you need to transform the text into pronunciation first. Because every language/script has its own pronouncing rules, ...


## Requirements
* lxml >= 3.3.3
	
## Background / References
* [CMU US English pronouncing dictionary](https://github.com/cmusphinx/cmudict)

## Work Flow
* STEP 1. Download the [wiktionary database backup dumps](http://ftp.acc.umu.se/mirror/wikimedia.org/dumps) of the language you want.
* STEP 2. Extract it to `data/raw/` folder.
* STEP 3. Run `build_corpus.py`.

## Pre-build dictionaries
Click the name of the language to download its prebuilt pronunciation dictionaries.

* [German](https://dl.dropboxusercontent.com/u/42868014/pron_dicts/de.csv.tar.gz)
