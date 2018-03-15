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

    fileOut = open(str(N) + '-weka_input.arff','w')

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


def main():
    N = int(sys.argv[1])

    # 1 - Obtenim N mes frequents
    mostFrequent = getMostFrequent(N)
    
    # 2 - Obtenim feature vectors
    getVector(N,mostFrequent)
    # 3 - Utilitzar WEKA o scikit-learn i calcular la precisio

    # 4 - Variar valors de N i analitzar




    """
    print "Most common female: ", fCount.most_common(N);
    print "Total female words: ", sum(fCount.values())
    print "Most common male: ", mCount.most_common(N);
    print "Total male words: ", sum(mCount.values())
    """














main();
