from wikisearch import *
from scraping import *


def wiki_search(search_text):
#get the wiki link for corresponding nouns
	link = googleit(search_text)	
	#content = regetdes(link)
	content = getdes(link)
	print(content)
