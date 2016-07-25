import sys
import random
sInput = " "
sRespons = " "

from tokeninput import *


while 1:
	print("> ", end = '')
	sInput = input()
	alltokens = tokenization(sInput)
	print(alltokens)
	nouns = grouping(alltokens)
	print(nouns)
	nouns = ""

