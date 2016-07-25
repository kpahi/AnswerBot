#from decimal import *
#import _pydecimal

import nltk

#from wikisearch import *

#stemming
from nltk.stem.porter import PorterStemmer
from nltk.stem.lancaster import LancasterStemmer

#which one to use
#stem_this = PorterStemmer()
stem_this = LancasterStemmer()
s = ("Hello there")

checknoun = ['NN','NNP','NNS']
#group the separated nouns (two)
nouns = ['Nepal']

#tokenize  and tag the input sentence 
def tokenization(sentence):
	text = nltk.word_tokenize(sentence)
	tagged = nltk.pos_tag(text)
	return tagged

def grouping(tagged):
	i=0
	length = len(tagged)
	for i in range(0,length):
		word = tagged[i][0]
		tag = tagged[i][1]
		#print(tagged[i][0])
		print(word,tag)
		if( tagged[i][1] in ['VBG', 'RB']):
			stemmed = stem_this.stem(word)
			print("Stemmed word: ", stemmed)


		#check if two noun are together
		if( i < length-1):
			if( tag in checknoun and tagged[i+1][1] in checknoun ):
				noun = tagged[i][0] + " " + tagged[i+1][0]
				nouns.append(noun)
			elif(tagged[i][1] in checknoun ):
				check = nltk.word_tokenize(str(nouns))
				if(tagged[i][0] in check):
					continue
				nouns.append(tagged[i][0])
			else:
				continue

		i+=1
	return nouns
'''
t = tokenization(s)
n = grouping(t)
print(t)
print(n)
'''

