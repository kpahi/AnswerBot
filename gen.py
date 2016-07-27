from knowl import *
#from keywords import *
import math
from operator import itemgetter


tokenize = lambda doc: doc.upper().split(" ")
def search_keys(inps):
	inputs = inps
	keys = []
	resp_list = []

#inputs = "you can to"
#inputs= " i am bored"
#inputs= 'are you intelligent '







	temp_dict = {}

#how many keywords contains the tokenized word
	nd =1 

	inputs = tokenize(inputs)

	def get_all_key():
		for k in know.keys():
			keys.append(k)
#call the above function
	get_all_key()
#get all the responds
	for r in know.values():
		resp_list.append(r)

#resp_list becomes the list of lists

#get all keys


#find the tf
	def find_weight():
		for k in keys:
			count = 1.
			for i in inputs:
				if i in tokenize(k):
					count = count +1.0
					continue

					#temp_dict[k] = count
					#temp_dict[k] = 1 + math.log(count / len(k))
				#temp_dict[k] = 1+ math.log(len(k) / count)
				#temp_dict[k] = count
				#find the idf
				#if(count != 1.):
				#	nd +=1
				#idf = math.log(nd/len(k))
				#tf_idf = count * idf
			
				#temp_dict[k] = tf_idf
				temp_dict[k] = int(count)
			
		return temp_dict
#sort by the values of weight
#print(temp_dict)
#temp_dict = sorted(temp_dict.items(), key= itemgetter(1))
#print(temp_dict)
#print(temp_list)
	ten_resp =[]
#get last five response
	def top_ten_resp():
		print("Best 10 responses are:\n")
		for i in range(1,11):
			#print(i)
			ten_resp.append(temp_list[-i])
			#print(temp_list[-i])

	dictionary = {}
#get a dictionary with weight assigned to the keywords
	dictionary = find_weight()
#print(dictionary)
#sort the list of keyword with greatest weight
	temp_list = sorted(dictionary.items(), key=itemgetter(1))
	top_ten_resp()
	
	return ten_resp
