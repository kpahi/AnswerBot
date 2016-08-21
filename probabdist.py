import json
import pickle
class probcalc:
    biprobdic={}
    triprobdic = {}

    def __init__(self,data1,data2):
        self.lowgram= data1
        self.highgram = data2

    def bigram_probability(self):
        count=0
        for data in self.highgram:
            #print(self.lowgram)
            #print(data)
            probability = self.highgram[data]/self.lowgram[data[0]]
            tuples = (data[1],probability)
            if data[0] not in self.biprobdic:
                self.biprobdic[data[0]] = []
            self.biprobdic[data[0]].append(tuples)
        for text in self.biprobdic:
            print(text,self.biprobdic[text])
            count+=1
        print(count)
        return self.biprobdic

    def trigram_probability(self):
        count=0
        for unidata, bidata, tridata in self.highgram:
            bipairs = (unidata, bidata)
            tripairs = (unidata, bidata, tridata)
            triprobab = self.highgram[tripairs] / self.lowgram[bipairs]
            trituple = (tridata, triprobab)
            if bipairs not in self.triprobdic:
                self.triprobdic[bipairs] = []
            self.triprobdic[bipairs].append(trituple)
        for text in self.triprobdic:
            print(text, self.triprobdic[text])
            count+=1
        print(count)
        return self.triprobdic

if __name__ == '__main__':
    #read files
    cout=0
    # with open('munigram.txt','r') as datafile:
    #     unitext = json.load(datafile)
    unitext = pickle.load(open("munigram.txt",'rb'))
    bifile =pickle .load(open("mbigram.txt",'rb'))
    trifile = pickle.load(open("mtrigram.txt",'rb'))

    #calculate bigram probability
    biprob = probcalc(unitext,bifile)
    bigramprob = biprob.bigram_probability()

    #calculate trigram probability
    triprob = probcalc(bifile,trifile)
    trigramprob = triprob.trigram_probability()
    for unigram in unitext:
        cout += 1
    print(cout)

    #store probability model in file
    storebi = open('mbiprobability.txt','wb')
    storetri = open('mtriprobability.txt','wb')

    pickle.dump(bigramprob,storebi)
    pickle.dump(trigramprob,storetri)

    storebi.close()
    storetri.close()





