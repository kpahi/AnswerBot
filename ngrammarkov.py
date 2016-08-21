import nltk
import pickle



def check_for_trigram(bigram,trifile):
    reqtri =False
    for tri in trifile:
        if bigram==tri:
            sort = sorted(trifile[bigram], key=lambda x: x[1], reverse=True)
            reqtri = sort[0][0]            # print(trifile[bigram])
    return reqtri
def choose_bigram(unigram,bifile):
    sort = sorted(bifile[unigram], key=lambda x: x[1], reverse=True)
    reqbi = sort[0][0]
    return reqbi

def markovresponse():
    uinput = input("YOUm>>")
    # uinput ="tell me about crime"
    input_tokens = nltk.word_tokenize(uinput)
    # search after removing the stop words

    nouns_tags = ['NN', 'NNP', 'NNPS', 'NNS', 'JJ', 'PRP']
    input_tagged = nltk.pos_tag(input_tokens)
    trifile = pickle.load(open("mtriprobability.txt", 'rb'))
    bifile = pickle.load(open("mbiprobability.txt", 'rb'))
    sentence = []

    for data in input_tagged:
        # print(data)
        if data[1] in nouns_tags:
            choose = data[0]
            break
    index = input_tokens.index(choose)
    input_bigram = (input_tokens[index], input_tokens[index + 1])
    # print(input_bigram)
    sentence = []
    start_bigram = input_bigram
    tri_check = check_for_trigram(start_bigram,trifile)
    if tri_check == False:
        sentence = [start_bigram[0]]
    else:
        sentence = list(start_bigram)
    count = 1
    func_bigram = start_bigram[0]
    while (sentence[-1] != "."):
        tri_check = check_for_trigram(start_bigram,trifile)
        if tri_check == ".":
            break
        if tri_check == False:
            temp_bigram = choose_bigram(func_bigram,bifile)
            sentence.append(temp_bigram)
        else:
            sentence.append(tri_check)
        start_bigram = (sentence[-2], sentence[-1])
        func_bigram = sentence[-1]
        # print(sentence)
        return sentence







