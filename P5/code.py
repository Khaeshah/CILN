import glob,re,sys


def getMostFrequent(N):
    path = './dataset/*'
    files = glob.glob(path)
    # Creem un dict per guardar informacio de females i males
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

        # Contem el nombre d'aparicions de les paraules que ens interessen
        with open(fileName) as file:
            for line in file:
                for word in line.split():
                    totalWords += 1
                    if word in frequents:
                        dic[word] += 1

        # Tractem el output al fitxer
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
    forbidden = ("?" , "!",'"', ",", ".", ";", ":")

    info = "% 1. Title: Gender classification\r\n" + \
    "%\n" + \
    "%2. Sources:\r\n" + \
    "%\t(a) Creator: Roman Rey, Sergi Sorigue\r\n" + \
    "%\t(b) Date: March, 2018 \r\n" + \
    "%\r\n\r\n" + \
    "@RELATION gender\r\n"

    for w in frequent:
        #word = re.sub('[^A-Za-z0-9 ]+', '', w)
        nWord = re.sub(r"[?|$|.|!|'|,|]",r'_',w)
        info += "@ATTRIBUTE freq_" + nWord + " NUMERIC\r\n"
    info += "@ATTRIBUTE class {female,male}\r\n"
    info += "@DATA\r\n"
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


# Mirar diferents precisions amb / sense signes de puntuacio, amb / sense majuscules, i amb / sense una combinacio de les dues
# simple logistic, smo. a la pestanya select attributes
# podem veure information gain. aqui sortiran les n paraules, podem treure conclusions. elem.lower()
