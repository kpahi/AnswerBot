import sys
import random
import nltk
sInput = " "
sRespons = " "

from tokeninput import *
from wikisearch import *
from scraping import *
from response import resfunctions

res = resfunctions()
while 1:
    print("> ", end = '')
    sInput = input()
    '''alltokens = tokenization(sInput)
    print(alltokens)
    nouns = grouping(alltokens)
    print(nouns)'''

    tokens = res.word_tokenize(sInput)
    nostop_words = res.remove_stopwords(tokens)
#get the wiki link for corresponding nouns
    link = getlink(nostop_words)


    content = regetdes(link)
    print(content)
    '''file = open("paragraph.txt",'r')
    readfile =file.read()
    print(readfile)
    sentences = nltk.sent_tokenize(readfile)
    print(sentences)'''

