try:
    import Queue as Q
except ImportError:
    import queue as Q
import glob,sys
from collections import Counter



def getMostFrequent(N):
    path = './dataset/*'
    files = glob.glob(path)
    # Creem un counter per guardar informacio de females i males
    dictionary = {}

    # Bucle que itera sobre tots els arxius
    for fileName in files:
        with open(fileName) as file:
            for line in file:
                for word in line.split():
                    if not dictionary.has_key(word):
                        dictionary[word] = 1
                    else:
                        dictionary[word] += 1

    sortedDic = sorted(dictionary, key=dictionary.get, reverse=True)
    ret = [];
    for i in range(0,N):
        ret.append(sortedDic[i])
    return ret

def getVector(N, frequents):

    path = './dataset/*'
    files = glob.glob(path)
    # Creem un counter per guardar informacio de females i males
    count = Counter()

    fileOut = open(str(N) + '-weka_input.arff','a')

    # Bucle que itera sobre tots els arxius
    for fileName in files:
        dic = {}
        totalWords = 0
        # Creem el vector de tamany N per el WEKA
        for w in frequents:
            dic[w] = 0

        # Asignem un gender. Si no es male ni female, no tindra gender
        gender = ""
        if fileName.endswith("_female"):
            gender = "female"
        elif fileName.endswith("_male"):
            gender = "male"

        with open(fileName) as file:
            for line in file:
                for word in line.split():
                    totalWords += 1
                    if word in frequents:
                        dic[word] += 1

        isFirst = 1
        for w in frequents:
            value = str(float(dic[w])/totalWords)
            if isFirst:
                fileOut.write(value);
                isFirst = 0
            else:
                fileOut.write(',' + value)
        # Afegim el genere de la persona
        if(gender != ""):
             fileOut.write(',' + gender)
        fileOut.write('\r\n')

def generateWeka(N,frequent):
    fileOut = open(str(N) + '-weka_input.arff','w')

    info = "% 1. Title: Gender classification\r\n" + \
    "%2. Sources:\r\n" + \
    "% (a) CILN - Roman Rey, Sergi Sorigue\r\n\r\n" + \
    "@RELATION gender\r\n"

    for w in frequent:
        info += "@ATTRIBUTE freq_" + w + " NUMERIC\r\n"
    info += "@ATTRIBUTE class {female,male}\r\n"
    fileOut.write(info)
    fileOut.close()

def main():
    N = int(sys.argv[1])

    # 1 - Obtenim N mes frequents
    mostFrequent = getMostFrequent(N)

    # 2 - Generem el weka header
    generateWeka(N,mostFrequent)

    # 3 - Obtenim feature vectors
    getVector(N,mostFrequent)


    # 4 - Variar valors de N i analitzar




main();
