import nltk
import json
from nltk.corpus import gutenberg
from nltk.corpus import brown
import pickle
import os


macbeth_sentences = gutenberg.sents('shakespeare-macbeth.txt')

#read the corpus text
file = open("/home/dragon/nltk_data/corpora/gutenberg/chesterton-ball.txt",'r')
fread = file.read()
# news_text = brown.words(categories='news')
#initialize dictionary
total_unigram = {}
total_bigram = {}
total_trigram = {}

ucheck = os.stat("munigram.txt").st_size
bcheck = os.stat("mbigram.txt").st_size
tcheck = os.stat("mtrigram.txt").st_size
print(ucheck)
if ucheck and bcheck and tcheck:
    unitext = pickle.load(open("munigram.txt", 'rb'))
    bitext = pickle.load(open("mbigram.txt", 'rb'))
    tritext = pickle.load(open("mtrigram.txt", 'rb'))
    total_unigram = unitext
    total_bigram = bitext
    total_trigram = tritext

count1=0
for totl in total_bigram:
    count1+=1;
print(count1)
#count the tokens
def count_tokens(token,dictionary):
    if token not in dictionary:
        dictionary[token] = 1
    else:
        dictionary[token] += 1

#tokenizing sentences and words
sentence_tokens = nltk.sent_tokenize(fread)
for sentence in sentence_tokens:
    word_tokens = []
    #get unigrams
    words = nltk.word_tokenize(sentence)
    # words = wordh.lower()

    #get only strings
    for word in words:
        if word.isalpha() or word==".":
            word_tokens.append(word.lower())

    #get bigrams
    bigrams = nltk.bigrams(word_tokens)

    #get trigrams
    trigrams = nltk.trigrams(word_tokens)

    #count unigrams
    for word in word_tokens:
        count_tokens(word,total_unigram)

    for bigram in bigrams:
        count_tokens(bigram,total_bigram)

    for trigram in trigrams:
        count_tokens(trigram,total_trigram)


count=0
for totl in total_bigram:
    count+=1;
print(count)
unifile = open("munigram.txt", 'wb')
pickle.dump(total_unigram,unifile)

bifile =open("mbigram.txt",'wb')
pickle.dump(total_bigram,bifile)


trifile = open("mtrigram.txt", 'wb')
pickle.dump(total_trigram,trifile)

unifile.close()
bifile.close()
trifile.close()



#####################
