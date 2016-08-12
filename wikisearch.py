import wikipedia
#from tokeninput import *
#from main import *
import requests
from bs4 import BeautifulSoup


def getlink(n):
	mypage = wikipedia.page(str(n))
	print(mypage.url)
	return mypage.url

#google search here
def googleit(research):
	research += (' wiki')
	goog_search = "https://www.google.co.uk/search?sclient=psy-ab&client=ubuntu&    hs=k5b&channel=fs&biw=1366&bih=648&noj=1&q=" + research
	
	r = requests.get(goog_search)

	soup = BeautifulSoup(r.text, "html.parser")

	wiki_link = soup.find('cite').text
	print(wiki_link)

	return wiki_link

	


