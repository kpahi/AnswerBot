from nltk.corpus import brown
import nltk
from nested_dict import nested_dict
from nltk.probability import LidstoneProbDist

testcorpus = " hellow its me sam. sam is a me. sam can be good. I am sam. sam is good"

unigram = {}
bigram = {}
probab = {}
trigram = {}
triprobab ={}

file = open("corpus.txt", 'r')
fread = file.read()
sentences = nltk.sent_tokenize(fread)
for sentence in sentences:
    words = nltk.word_tokenize(sentence)

    bigra = nltk.bigrams(words)

    trigra = nltk.trigrams(words)

    for word in words:
        if word in unigram:
            unigram[word] += 1
        else:
            unigram[word] = 1
            # for text in unigram:
            # print(text, ":", unigram[text])

    for data in bigra:
        if data in bigram:
            bigram[data] += 1
        else:
            bigram[data] = 1
            # for text in bigram:
            # print(text, ":", bigram[text])


    for data in trigra:
        if data not in trigram:
            trigram[data] = 1
        else:
            trigram[data] += 1

for datas in bigram:
    # probab[datas[0]] = []
    temp = bigram[datas] / unigram[datas[0]]
    tup = (datas[1], temp)
    # test = probab[data[0]]
    # print(test)
    if datas[0] not in probab:
        probab[datas[0]] = []

    probab[datas[0]].append(tup)

for data1,data2,data3 in trigram:
    bipairs =(data1,data2)
    triparis = (data1,data2,data3)
    triprobab[bipairs] = []
    tritemp = trigram[triparis]/bigram[bipairs]
    tritup = (data3,tritemp)
    if bipairs not in triprobab:
        triprobab[bipairs] = []
    triprobab[bipairs].append(tritup)

for data in probab:
    print(data,probab[data])

for data in triprobab:
    print(data,triprobab[data])