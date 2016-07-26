# -*- coding: utf8 -*-
import sys
#import the library used to query website
import urllib.request
from urllib.request import HTTPError,URLError
import re
import wikipedia


#import Beautiful Soup to parse data from the website
from bs4 import BeautifulSoup
#filename = paragraph.txt
target = open('paragraph.txt','w')

def getdes(l):
	print(l)
	try:
		page = urllib.request.urlopen(l)
		soup = BeautifulSoup(page,"lxml")
		all_paragraph = soup.find_all('p',limit = 5)
		for par in all_paragraph:
			paragraph = (par.getText()).encode('utf-8')
			print(paragraph)
			target.write(str(paragraph))
			target.write("\n")
	except URLError as e:
		print('Reason ', e.reason)




#with wikipedia

'''
def getdes(searchfor):
	p = wikipedia.page(searchfor)
	print(p.url)
	fulltext = (p.content).encode('utf-8')
	print((fulltext))
	target.write((fulltext))
	target.write("\n")
'''	
