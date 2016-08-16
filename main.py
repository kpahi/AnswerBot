import sys
import random
import nltk
import NER
sInput = " "


from tokeninput import *
from response import resfunctions
from function import *

# from nltk.corpus import stopwords

stopwords = ['what', 'why', 'when', 'how', 'a', 'is', 'an', 'the', 'are', 'was', 'were', 'am']


# static working
from gen import *

matched_keys = []
res = resfunctions()
if __name__ == '__main__':
	while 1:
		count =1
		nerlist = []
		print("> ", end='')
		sInput = input().lower()
# sInput = "who is the president of america"

		inputstring = sInput
		sInput += str(' ')
# Remove stop words
# can be done with nltk->stopwords
# sInput = ' '.join([word for word in sInput.split() if word not in stopwords.words("english")])
		for word in stopwords:
			if word in sInput.split():
				sInput = sInput.replace(word, "")
# wikilist = wiki_search(sInput)


        # nerlist = getNER(wikilist)
#tokenize input words
		input_tokens = nltk.word_tokenize(inputstring)
		wikiflag = False
		wiki_tokens = ['what', 'who', 'where']
#check if input tokens contains wh question
		for tokens in input_tokens:
			if tokens in wiki_tokens:
				wikiflag = True
				break
#wiki search true
		if wikiflag:
			wiki_search(sInput)
			file = open('paragraph.txt', 'r')
			fread = file.read()
			sentences = nltk.sent_tokenize(fread)
#get ner list
			nerlist = NER.getNER(sentences)
			print(nerlist)
			tagged_input = nltk.pos_tag(input_tokens)
			get_input_nouns = getnouns(tagged_input)
			start_output = " ".join(input_tokens[2:])
			verbused = input_tokens[1]
#for who  questions
			if 'who' in input_tokens:
				person = NER.getpersonlist(nerlist)
				print(person)
				if len(person) == 1:
					print(start_output,verbused, ''.join(person))
				else:
					reqper = NER.gethighcountner(get_input_nouns, person)
					print(start_output,verbused,reqper)
			elif 'where' in input_tokens:
				place = NER.getplacelist(nerlist)
				print(place)
				if len(place) ==1:
					print(start_output,"at","".join(place))
				else:
					reqplace = NER.gethighcountner(get_input_nouns,place)
					print(start_output,"at",reqplace)
		if count ==1:
			break


