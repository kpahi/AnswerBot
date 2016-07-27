import sys
import random
sInput = " "
sRespons = " "

from tokeninput import *
from wikisearch import *
from scraping import *
from selectresp imoprt *

while 1:
	print("> ", end = '')
	sInput = input()
	alltokens = tokenization(sInput)
	print(alltokens)

'''Here comes the wiki
	alltagged = tagging(alltokens)	
	print(alltagged)

	nouns = grouping(alltagged)
	print(nouns)

#get the wiki link for corresponding nouns
	link = getlink(nouns)
	
	
	content = getdes(link)
	nouns.clear()

'''
