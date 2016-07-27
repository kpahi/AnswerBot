from knowl import *
#from keywords import *
import math
from operator import itemgetter
keys = []
resp_list = []

#input = "you can to"
#input = " i am bored"
input = "What do you like. "
#input = "you can speak."
count = 1.

tokenize = lambda doc: doc.upper().split(" ")

temp_dict = {}

#how many keywords contains the tokenized word
nd =1 

input = tokenize(input)

for k in know.keys():
	keys.append(k)

#get all the responds
for r in know.values():
	resp_list.append(r)

#resp_list becomes the list of lists

#find the tf
for k in keys:
	for i in input:
		if i in tokenize(k):
			count = count +1.
			continue
			#temp_dict[k] = count
			#temp_dict[k] = 1 + math.log(count / len(k))
		#temp_dict[k] = 1+ math.log(len(k) / count)
		#temp_dict[k] = count

		#find the idf
		if(count != 1.):
			nd +=1
		idf = math.log(nd/len(k))
		tf_idf = count * idf

		temp_dict[k] = tf_idf



		
	count = 1.
#sort by the values of weight
temp_dict = sorted(temp_dict.items(), key=itemgetter(1))

#find the idf
#total number of keys:


print(temp_dict)
