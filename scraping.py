#import the library used to query website
import urllib.request
from urllib.request import HTTPError,URLError
import re

#import Beautiful Soup to parse data from the website
from bs4 import BeautifulSoup
#filename = paragraph.txt
target = open('paragraph.txt','w')


def getdes(l):
	page = urllib.request.urlopen(l)
	soup = BeautifulSoup(page)
	all_paragraph = soup.find_all('p',limit = 5)
	for par in all_paragraph:
		paragraph = par.getText()
		print(paragraph)
		target.write(paragraph)
		target.write("\n")




