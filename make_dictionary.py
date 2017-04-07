#!/usr/bin/python3
# coding: utf-8
import argparse
import codecs
import os
import sys
import re
import lxml.etree as ET
import unicodedata

# namespace
ns = "{http://www.mediawiki.org/xml/export-0.10/}" 

# arguments setting 
lcode = sys.argv[1]
fname = "{}wiktionary-20161201-pages-articles-multistream.xml".format(lcode)    

def _refine_pron(pron):
    """Refines pronunciation (string)"""
    # remove punctuations
    pron = re.sub("[\u2000-\u206F.,·/#!$%\^&*;:{}=\-_`~()<>\[\]]", "", pron)

    # unicode normalization
    pron = unicodedata.normalize('NFD', pron)
    
    # digraph normalization
    dict = {"ʣ":"dz", "ʤ":"dʒ", "ʦ":"ts", "ʧ":"tʃ"}
    for k, v in dict.items():
        pron = pron.replace(k, v)
    
    # split into single phonemes
    ## stress symbols
    pron = re.sub("[ʼ']", "ˈ", pron)
    pron = re.sub("([ˈˌ])", r" \1", pron)
    
    ## diacritics must combine with their preceding letters.
    pron = re.sub("([^\U00000300-\U0000036F\U000002B0-\U000002FF])", r' \1', pron)

    # squeeze spaces
    pron = re.sub("[ ]+", " ", pron)
    
    return pron.strip()

def _get_hw(elem):
    '''Returns a headword (string) from elem (element)'''
    try:
        hw = elem.find('./{}title'.format(ns)).text
        
        # validity check
        if any(word in hw for word in [' ', ',', 'Wiktionary:']): # We will NOT cover multi-word headwords.
            return None
        else:
            return hw
    except:
        return None

def _get_entry_block(text):
    """Returns a relevant block (string) from text"""
    ltags = {"de":"Sprache|Deutsch",
             "es":"lengua|es",
             "fi":"Suomi",
             "fr":"langue|fr",
             "it":"{{-it-}}",
             "pl":"język polski",
             "pt": "{{-pt-}}",
             "ru": "{{-ru-}}",
             "ko": "한국어 ==",
             "tr": "Söz türü|Ad|Türkçe",
             }
    ltag = ltags.get(lcode)
    # language specifier in Portuguese and Russian Wiktionary dump is surrounded with "=", not "=="
    if lcode in ["pt", "ru"]:
        for entry_block in re.split("(?m)^=(?!=)", text):
            if ltag in entry_block:
                return entry_block
    else:
        for entry_block in re.split("(?m)^==(?!=)", text):
            if ltag in entry_block:
                return entry_block
    return None
        
def _get_prons(elem):
    '''returns list of pronunciations from elem (element)'''
    try:
        text = elem.find('./{0}revision/{0}text'.format(ns)).text
        entry_block = _get_entry_block(text)
        if lcode in ['de']:
            pron_blocks = re.findall("(?m){{IPA}} {{Lautschrift\|([^}]+)}}(?:[^{]+{{Lautschrift\|([^}]+)}})?", entry_block)
            prons = {_refine_pron(pron) for pron_block in pron_blocks for pron in pron_block if len(pron) > 0 and "..." not in pron and "…" not in pron}
        elif lcode in ['it', 'fi', 'pl', 'ko', 'tr']:
            pron_blocks = re.findall("(?m){{IPA\d?\|([^}]+)", entry_block)
            prons = {_refine_pron(pron) for pron_block in pron_blocks for pron in pron_block.split("|")}
        elif lcode in ['es']:
            pron_blocks = re.findall("(?m){{pron-graf\|([^}]+)", entry_block)
            prons = {_refine_pron(re.sub("^[^=]+=", "", pron)) for pron_block in pron_blocks for pron in pron_block.split("|") if 'fone=' in pron}
        elif lcode in ['fr']:
            pron_blocks = re.findall("(?m){{pron\|([^}\|]+)", entry_block)
            prons = {_refine_pron(pron_block) for pron_block in pron_blocks}
        elif lcode in ['pt']:
            pron_blocks = re.findall("(?m)\[?\[?AFI\]?\]?: \/([^\/]+)\/", entry_block) + \
                          re.findall("(?m){{AFI\|\/([^\/]+)\/}}", entry_block)
            prons = {_refine_pron(pron_block) for pron_block in pron_blocks}
        elif lcode in ['ru']:
            pron_blocks = re.findall("(?m){{transcriptions(?:-ru)?\|([^}]+)}}", entry_block)
            prons = {_refine_pron(pron) for pron_block in pron_blocks for pron in pron_block.split("|")
                     if ('.ogg' not in pron and len(pron) > 0)}
        return list(prons)
    except:
        return None

def build_corpus():
    # Create folder
    if not os.path.exists('data/refined'): os.mkdir('data/refined')
    
    # Start work
    results = []
    i = 1
    for _, elem in ET.iterparse("data/raw/{}".format(fname), tag=ns+"page"):
        hw = _get_hw(elem)
        prons = _get_prons(elem)
        if hw and prons:
            for pron in prons:
                results.append((hw, pron))
        
        elem.clear() # We need to save memory!
        if i % 1000 == 0: print(i)
        i += 1
    
    # Write to file    
    with codecs.open("data/refined/{}.csv".format(lcode), 'w', 'utf-8') as fout:
        fout.write("headword,pronunciation\n")
        results.sort(key=lambda x:x[0])
        for headword, pron in results:
            fout.write("{},{}\n".format(headword, pron))

if __name__ == "__main__":
    build_corpus()
    print("Done")
