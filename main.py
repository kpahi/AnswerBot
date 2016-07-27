import sys
import random
import nltk
sInput = " "
sRespons = " "

from tokeninput import *
from wikisearch import *
from scraping import *
<<<<<<< HEAD
from selectresp imoprt *
=======
from response import resfunctions
>>>>>>> f5199b7cc4bb0777d315c04ca4a30c13627fe855

res = resfunctions()
while 1:
<<<<<<< HEAD
	print("> ", end = '')
	sInput = input()
	alltokens = tokenization(sInput)
	print(alltokens)

'''Here comes the wiki
	alltagged = tagging(alltokens)	
	print(alltagged)

	nouns = grouping(alltagged)
	print(nouns)
=======
    print("> ", end = '')
    sInput = input()
    '''alltokens = tokenization(sInput)
    print(alltokens)
    nouns = grouping(alltokens)
    print(nouns)'''
>>>>>>> f5199b7cc4bb0777d315c04ca4a30c13627fe855

    tokens = res.word_tokenize(sInput)
    nostop_words = res.remove_stopwords(tokens)
#get the wiki link for corresponding nouns
    link = getlink(nostop_words)

<<<<<<< HEAD
'''
=======

    content = regetdes(link)
    print(content)
    '''file = open("paragraph.txt",'r')
    readfile =file.read()
    print(readfile)
    sentences = nltk.sent_tokenize(readfile)
    print(sentences)'''

>>>>>>> f5199b7cc4bb0777d315c04ca4a30c13627fe855
