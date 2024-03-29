from wikisearch import *
from scraping import *
import generator
from main import prn_dict
import nltk

def wiki_search(search_text):
#get the wiki link for corresponding nouns
	link = googleit(search_text)	
	# content = regetdes(link)
	content = getdes(link)
#	print(content)
	
	return content

def static_search(sInput):
#search in the static keywords list
	search = generator.SelectResponse(sInput)
	response_list = search.top_ten_resp()
	# print(response_list)


#currently select the 1st keywords
	best = response_list[0][0]
	# print("Selected key word: ", best)
#Resonse of the 1st matched keywords
	best_resp = generator.give_resp(best)
	print("AnswerBot>>",best_resp)



def getnouns(content):
	noun_list=[]
	for data in content:
		if data[1] in ['JJ','NN','NNP','NNPS',"NNS"]:
			noun_list.append(data[0])
	return noun_list

def listtooutput(inputlist):
	str = " ".join(inputlist)
	return str

def getlowerlist(inputlist):
	outputlist=[]
	for inputs in inputlist:
		outputlist.append(inputs.lower())
	# print(outputlist)
	return outputlist
#check if there is any pronoun
def checkprn(t):
	#make a list of the tupple t which is after pos_tag
	l = list(t)
	for i in range(0,len(t)):
		if t[i][1] == 'PRP':
			l[i] = prn_dict[t[i][0]]
			continue
		l[i] = t[i][0]
		

	return l
