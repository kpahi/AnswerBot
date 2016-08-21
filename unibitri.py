import nltk
import json
from nltk.corpus import gutenberg
from nltk.corpus import brown
import pickle


macbeth_sentences = gutenberg.sents('shakespeare-macbeth.txt')

#read the corpus text
file = open("/home/dragon/nltk_data/corpora/gutenberg/whitman-leaves.txt",'r')
fread = file.read()
news_text = brown.words(categories='news')
#initialize dictionary
total_unigram = {}
total_bigram = {}
total_trigram = {}


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

    #get only strings
    for word in words:
        if word.isalpha() or word==".":
            word_tokens.append(word)

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

#store the counted tokens
# with open('munigram.txt','r') as f:
#     data = json.load(f)
#
# data.update(total_unigram)
#
# with open('test.json', 'w') as f:
#     json.dump(data, f)
# print(total_unigram,total_bigram,total_trigram)
count=0
for totl in total_unigram:
    count+=1;
print(count)
unifile = open("munigram.txt", 'ab')
pickle.dump(total_unigram,unifile)
# unifile = open('munigram.txt', 'a')
# json.dump(total_unigram, unifile)

bifile =open("mbigram.txt",'ab')
pickle.dump(total_bigram,bifile)


trifile = open("mtrigram.txt", 'ab')
pickle.dump(total_trigram,trifile)

unifile.close()
bifile.close()
trifile.close()



#####################
