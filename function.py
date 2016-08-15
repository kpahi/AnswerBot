from wikisearch import *
from scraping import *

import nltk

def wiki_search(search_text):
#get the wiki link for corresponding nouns
	link = googleit(search_text)	
	# content = regetdes(link)
	content = getdes(link)
	return content
	# print(content)

def getnouns(content):
	noun_list=[]
	for data in content:
		if data[1] in ['NN','NNP','NNPS',"NNS"]:
			noun_list.append(data[0])
	return noun_list

def listtooutput(inputlist):
	str = " ".join(inputlist)
	return str

def getlowerlist(inputlist):
	outputlist=[]
	for inputs in inputlist:
		outputlist.append(inputs.lower())
	print(outputlist)
	return outputlist
