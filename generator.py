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
	temp_dict = {}
	temp_resp = []
	ten_resp = []
	temp_list = []
	number_of_keys = 0
	count = 0

	def __init__(self, inps):
		self.inputs = inps
		#tokenize the inputs
		self.inputs = tokenize(self.inputs)
		print(self.inputs)
		
#get all the keys
	def get_all_keys(self):
		for k in know.keys():
			self.keys.append(k)

		self.number_of_keys = len(self.keys)
		return self.keys


#get weight of all the KEYWORDS
	def find_weight(self):
		self.temp_dict = {}
		all_keys = self.get_all_keys()
		for k in all_keys:
			count = 1.
			for i in self.inputs:
				if i in tokenize(k):
					count = count + 1.0
					continue

				self.temp_dict[k] = int(count)

		del all_keys
	#	print(self.temp_dict)
		return self.temp_dict
	
#get top 10 matched keywords:
	def top_ten_resp(self):
		dictionary = self.find_weight()
		self.temp_list = sorted(dictionary.items(), key=itemgetter(1))
		self.ten_resp = []
		print("Best 10 matched keywords are:\n")
		for i in range(1,5):
			self.ten_resp.append(self.temp_list[-i])
		del dictionary
		del self.temp_list
		return self.ten_resp
	
#delete everything
	def __del__(self):
		del self.inputs
		del self.temp_dict
		del self.ten_resp



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

