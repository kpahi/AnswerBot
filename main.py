import sys
import random
import nltk
sInput = " "
sRespons = " "

from tokeninput import *
from wikisearch import *
from scraping import *
from response import resfunctions

#static working
from gen import *
matched_keys = []
res = resfunctions()
while 1:
    print("> ", end = '')
    sInput = input()
	#search in the static keywords list
    matched_keys = search_keys(sInput)
    print(matched_keys)

    #alltokens = tokenization(sInput)
    #print(alltokens)
    #nouns = grouping(alltokens)
    #print(nouns)

    #tokens = res.word_tokenize(sInput)
    #nostop_words = res.remove_stopwords(tokens)
#get the wiki link for corresponding nouns
    #link = getlink(nostop_words)
    #content = regetdes(link)
    #print(content)
    
