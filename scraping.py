# -*- coding: utf8 -*-
import sys
#import the library used to query website
import urllib.request
from urllib.request import HTTPError,URLError
import re
import nltk
import wikipedia


#import Beautiful Soup to parse data from the website
from bs4 import BeautifulSoup
#filename = paragraph.txt
target = open('paragraph.txt','w')

def getdes(l):
    all = ''
    try:
        page = urllib.request.urlopen(l)
        soup = BeautifulSoup(page,"lxml")
        all_paragraph = soup.find_all('p',limit = 5)
        target.seek(0)
        target.truncate()
        target.seek(0)
       # print(all_paragraph)
        for par in all_paragraph:
            paragraph = (par.getText()).encode('utf-8')
            #print(paragraph)
            all += str(paragraph)
            #target.write(str(paragraph))
            #target.write("\n")
        #print(all)
        target.write(all)
        print(all)
    except URLError as e:
        print('Reason ', e.reason)
        print("Error wiriting file")

    return all

def regetdes(l):
    #print(l)
    sentences_list=[]
    try:
        page = urllib.request.urlopen(l)
        soup = BeautifulSoup(page, "lxml")
        all_paragraph = soup.find_all('p', limit=5)
        for par in all_paragraph:
            paragraph = (par.getText()).encode('utf-8')
            print(paragraph)
            decodedpara =paragraph.decode('utf-8')
            sentences = nltk.sent_tokenize(decodedpara)
            sentences_list.append(sentences)

    except URLError as e:
        print('Reason ', e.reason)
        print("Error wiriting file")


    return sentences_list




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
