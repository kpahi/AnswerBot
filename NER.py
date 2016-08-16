from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree
import nltk
from function import *
def get_continuous_chunks(text):
    chunked = ne_chunk(pos_tag(word_tokenize(text)))
    #print(chunked)
    prev = None
    # print(chunked)
    continuous_chunk = []

    for i in chunked:
        # print(i)
        if type(i) == Tree:
            current_chunk = []
            concat  = ''
            #print(i.leaves)
            for token,pos in i.leaves():
                # current_chunk.append(token)
                # strings = str(current_chunk)
                concat +=" "+token
            ner =(i.label(),concat)
            # print(ner)
            continuous_chunk.append(ner)
    return continuous_chunk

def getNER(content):
    nerlist = []
    for text in content:
        obtainlist = get_continuous_chunks(str(text))
        for data in obtainlist:
            if data not in nerlist:
                nerlist.append(data)
    return nerlist
def getplacelist(content):
    places=[]
    for data in content:
        if data[0] =='GPE':
            places.append(data[1])
    return places


def getpersonlist(content):
    persons=[]
    for data in content:
        if data[0]=='PERSON':
            persons.append(data[1])
    return persons

def gethighcountner(nouns,wholist,all_con):
    getlist =[]
    personlist=[]
    wordslist=[]

    #file = open('paragraph.txt','r')
    #fread = file.read()
    #sentences = nltk.sent_tokenize(fread)
    sentences = nltk.sent_tokenize(all_con)
    for person in wholist:
        count =0
        for sentence in sentences:
            words = nltk.word_tokenize(sentence)
            lower_words = getlowerlist(words)
            persons = getlowerlist(nltk.word_tokenize(person))
            if set(persons) < set(lower_words) and set(nouns) <set(lower_words):
                count += 1
                print(count)
        getdata = (person,count)
        getlist.append(getdata)

    for get in getlist:
        print(get)
    getlist=sorted(getlist, key=lambda x: x[1],reverse = True)
    for get in getlist:
        print(get)
    getinfo = getlist[0]
#        print(getinfo[0])
    return getinfo[0]





