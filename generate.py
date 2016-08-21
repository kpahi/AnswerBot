import pickle
import nltk
from nltk.corpus import stopwords

bifile = pickle.load(open("biprobability.txt",'rb'))
trifile = pickle.load(open("triprobability.txt",'rb'))
for i in range(1,3):
    getinput = input('YOU>>')
    input_tokens = nltk.word_tokenize(getinput)

    stop_words = set(stopwords.words("english"))
    nostop_word = []
    for word in input_tokens:
        if word not in stop_words:
            nostop_word.append(word)

    tagged_tokens = nltk.pos_tag(nostop_word)

    # choose first Noun for current state to start response
    for words in tagged_tokens:
        if words[1] == 'NN':
            choose = words[0]
            break


    # print(choose)

    # choose next best
    def next_best(current_state):
        bestprob = 0
        # print(bifile[current_state])
        bimarkov = bifile[current_state]
        # print(bimarkov)
        for data in bimarkov:
            if data[1] > bestprob:
                # print(data[1])
                bestprob = data[1]
                beststate = data[0]
                # print(beststate)
        return beststate


    def babble(amount, state=''):
        if not amount:
            return state

        next_word = next_best(state)
        # print(next_word)
        return state + ' ' + babble(amount - 1, next_word)


    # next_best("he")
    response = babble(3, choose)
    print("AnswerBot>>", response)
    # print(response)





