from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree
import nltk
def get_continuous_chunks(text):
    chunked = ne_chunk(pos_tag(word_tokenize(text)))
    #print(chunked)
    prev = None
    # print(chunked)
    continuous_chunk = []
    current_chunk = []
    for i in chunked:
        if type(i) == Tree:
            for token,pos in i.leaves():
                ner =(i.label(),token)
                # print(ner)
                continuous_chunk.append(ner)
    return continuous_chunk
# test = "President of America is Barak Obama but the New York city is tidy."
# get =get_continuous_chunks(test)
# print(get)



