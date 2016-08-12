
import nltk
#from generator import *
import main

#check for the name of user
#make personal profile dictionary save
#next time same person comes up, load the corresponding dictionary

likes = ['like','love', 'adore', 'mad about', 'crazy about', 'enjoy', 'keen on']

dislikes = ["don't like", 'dislike', 'hate', 'adore', "can't bear", "can't stand", "can't stand", 'detest', 'loathe']

checknoun = ['NN','NNP','NNS']
checkverb = ['VBG', 'VBP','RB']

#function to tokenize:
tokenize = lambda doc: doc.lower().split(" ")


name_entity = 'user'
d = {'he':'Kritish'}

class Profile(object):
	def __init__(self, inps):
		self.inputs= inps
	#tokenize and remove the stop words
		for w in main.stopwords:
			if w in (self.inputs).split():
				self.inputs = (self.inputs).replace(w,"")
#tokenize the inputs
		self.inputs = nltk.word_tokenize(self.inputs)
		print(self.inputs)
	
		#tag the tokenize words.
		tag = nltk.pos_tag(self.inputs)
		print(tag)
		
		#check if there is words likes or dislikes
		for i in range(0,len(self.inputs)):
			if (tag[i][1] in checkverb):
#get the nouns after it
				for j in range(0,len(self.inputs)):
					if( tag[j][1] in checknoun):
						d[tag[i][0]] = tag[j][0]

#check if any prep function
def checkPrep(t):
#here t is the list of tupple after pos_tag
#make a list of the tupple to mutate
	l = list(t)
	for i in range(0,len(t)):
		#Pronoun is detected
		if t[i][1] == 'PRP':
#here d is the dictionary where he:'name' is stored 
			l[i] = d[t[i][0]]
			continue
		l[i] = t[i][0]

	#new list omiting pronoun is in l
	print(l)



#
text1 = "i love basketball."
text2 = "i adore the smell of the chicken"
text3 = "i like color of the sky."

s = Profile(text1)
s = Profile(text2)
s = Profile(text3)

print(d)
	

