# coding: utf-8
#!/usr/bin/python2
from __future__ import print_function
import argparse
import codecs
import os
import sys
import re
import lxml.etree as ET
import unicodedata

ns = "{http://www.mediawiki.org/xml/export-0.10/}" # namespace

# arguments setting 
lcode = sys.argv[1]
fname = "{}wiktionary-20161201-pages-articles-multistream.xml".format(lcode)    

def _refine_hw(hw):
    global lcode
    
    if lcode in ['de']:
        return hw
    
def _refine_pron(pron):
    global lcode
    
    if lcode in ['de']:
        # remove punctuations
        pron = re.sub(u"[.,·/#!$%\^&*;:{}=–\-_`~()<>]", "", pron)
        
        # unicode normalization
        pron = unicodedata.normalize('NFD', pron)
        
        # digraph normalization
        dict = {u"ʣ":u"dz", u"ʤ":u"dʒ", u"ʦ":u"ts", u"ʧ":u"tʃ"}
        for k, v in dict.items():
            pron = pron.replace(k, v)
        
        # split into phonemes
        ## proness
        pron = re.sub(ur"([ˈˌ])", ur" \1", pron).strip()
        ## diacritics 
        pron = re.sub(ur"([^\U00000300-\U0000036F\U000002B0-\U000002FF])", ur' \1', pron).strip()
        
        # squeeze spaces
        pron = re.sub("[ ]+", " ", pron)
        return pron

def _get_hws(elem):
    '''Given elem, returns list of headwords'''
    global ns, lcode
    if lcode in ['de']: # There's only one form of headword.
        try:
            hw = elem.find('./{}title'.format(ns)).text
            
            # validity check
            if " " in hw or "," in hw: 
                return None
            else:
                return [_refine_hw(hw)]
        except:
            return None

def _get_prons(elem):
    '''Given elem, returns list of pronunciations'''
    global ns, lcode
    if lcode in ['de']:
        try:
            text = elem.find('./{0}revision/{0}text'.format(ns)).text
            if re.search(ur"^==[^=]+Sprache\|Deutsch", text) is None: # In german wiktionary, languages other than german are included.
                return None
            pron = re.search(ur"{{IPA}}[^\n]+Lautschrift\|([^}]+)", text).group(1)
            
            # validity check
            if u"..." in pron or u"…" in pron:
                return None
            else:
                return [_refine_pron(pron)]
        except:
            return None
    
def build_corpus():
    global lcode, fname, ns
    
    # Create folder
    if not os.path.exists('data/refined'): os.mkdir('data/refined')
    
    # Start work
    results = []
    i = 1
    for _, elem in ET.iterparse("data/raw/{}".format(fname), tag=ns+"page"):
        hws = _get_hws(elem)
        prons = _get_prons(elem)
        if hws and prons:
            for hw in hws:
                for pron in prons:
                    results.append((hw, pron))
        
        elem.clear() # We need to save memory!
        if i % 1000 == 0: print(i, end="===")
        i += 1
    
    # Write to file    
    with codecs.open("data/refined/{}.csv".format(lcode), 'w', 'utf-8') as fout:
        fout.write("headword,pronunciation\n")
        results.sort(key=lambda x:x[0])
        for headword, pron in results:
            fout.write(u"{},{}\n".format(headword, pron))

if __name__ == "__main__":
    build_corpus()
    print("Done")
