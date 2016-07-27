import nltk
class resfunctions:
    def __init__(self):
        return
    def word_tokenize(self,line):
        word_list=[]
        for word in line.split():
            word_list.append(word)
        return word_list
    def remove_stopwords(self,text):
        stopword = nltk.corpus.stopwords.words('english')
        content = [w for w in text if w.lower() not in stopword]
        return content


