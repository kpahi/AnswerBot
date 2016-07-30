import sys
import random
import nltk
sInput = " "


from tokeninput import *
from wikisearch import *
from scraping import *
from response import resfunctions

import generator

#static working
from gen import *
matched_keys = []
res = resfunctions()

if __name__ == '__main__':
	while 1:
		print("> ", end = '')
		sInput = input()
		sInput += str(' ')


#search in the static keywords list
		search = generator.SelectResponse(sInput) 
		response_list = search.top_ten_resp()
		print(response_list)


#currently select the 1st keywords
		best = response_list[0][0]
		print("Selected key word: ", best)
#Resonse of the 1st matched keywords
		best_resp = generator.give_resp(best)
		print(best_resp)



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
		del sInput
		del search
		del response_list
		del best_resp
		#r = search.top_ten_resp()
		#print(response_list)
