import sys
import random
sInput = " "
sRespons = " "

from tokeninput import *
from wikisearch import *

while 1:
	print("> ", end = '')
	sInput = input()
	alltokens = tokenization(sInput)
	print(alltokens)
	nouns = grouping(alltokens)
	print(nouns)

#get the wiki link for corresponding nouns
	link=getlink(nouns)
	content = getdes(link)
	nouns.clear()


