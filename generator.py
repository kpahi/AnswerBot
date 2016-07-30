from knowl import *
#from keywords import *

import math
#import random
import random
from operator import itemgetter

#function to tokenize the inputs
tokenize = lambda doc: doc.upper().split(" ")

#already given responses

class SelectResponse(object):
	keys = []
	resp_list = []
	temp_dict = {}
	temp_resp = []
	ten_resp = []
	temp_list = []
	number_of_keys = 0

	def __init__(self, inps):
		self.inputs = inps
		#tokenize the inputs
		self.inputs = tokenize(self.inputs)
		
#get all the keys
	def get_all_keys(self):
		for k in know.keys():
			self.keys.append(k)

		self.number_of_keys = len(self.keys)
		return self.keys


#get weight of all the KEYWORDS
	def find_weight(self):
		all_keys = self.get_all_keys()
		for k in all_keys:
			count = 1.
			for i in self.inputs:
				if i in tokenize(k):
					count = count + 1.0
					continue

				self.temp_dict[k] = int(count)


		return self.temp_dict
	
#get top 10 matched keywords:
	def top_ten_resp(self):
		dictionary = self.find_weight()
		temp_list = sorted(dictionary.items(), key=itemgetter(1))
		print("Best 10 matched keywords are:\n")
		for i in range(1,5):
			self.ten_resp.append(temp_list[-i])
		return self.ten_resp



#try
#response = SelectResponse(" you intelligent  ")

#k = response.top_ten_resp()
#k = response.give_resp()
#print(k)
#print(k[0][0])
#best = k[0][0]
#print(response.number_of_keys)
#print(response.give_resp)

#get response
def give_resp(matched_k):
	resp_list = []
	i = 0
	for r in know.keys():
		if matched_k == r:
			#print(know.get(r))
			resp_list = know.get(matched_k)
			pos_res = len(resp_list)
			j = random.randint(0,pos_res-1)
			return know[matched_k][j]

		i +=1
			

#list_resp = give_resp(best)

#print(list_resp)

