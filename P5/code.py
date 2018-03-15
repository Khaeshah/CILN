try:
    import Queue as Q
except ImportError:
    import queue as Q
import glob,sys
from collections import Counter

def getFrequentsAndVector(N):

    path = './dataset/*'
    files = glob.glob(path)
    # Creem un counter per guardar informacio de females i males
    count = Counter()

    fileOut = open('weka_input.arff','w')

    # Bucle que itera sobre tots els arxius
    for fileName in files:
        with open(fileName) as file:
            content = file.read()
            # Asignem un gender. Si no es male ni female, no tindra gender
            gender = ""
            if fileName.endswith("_female"):
                gender = "female"
            elif fileName.endswith("_male"):
                gender = "male"

            # Contem el nombre d aparicions utilitzant un counter
            count = Counter(content.strip().split())
            totalWords = sum(count.values())
            temp = count.most_common(N);
            aux = []

            # Asignem el array amb la informacio que ens interessa
            isFirst = 1
            for common in temp:
                if(common[1] != 0):
                    value = str(float(common[1])/totalWords)
                    if isFirst:
                        fileOut.write(value);
                        isFirst = 0
                    else:
                        fileOut.write(',' + value)

            # Quan el text te menys paraules que la N, ho arreglem per igualar el vector
            dif = N - len(temp)
            while(dif):
                fileOut.write(',0')
                dif = dif-1;

            # Afegim el genere de la persona
            if(gender != ""):
                 fileOut.write(',' + gender)
            fileOut.write('\r\n')



def main():
    N = int(sys.argv[1])
    vec = []

    # Obtenim N mes frequents i feature vectors
    getFrequentsAndVector(N)




    """
    print "Most common female: ", fCount.most_common(N);
    print "Total female words: ", sum(fCount.values())
    print "Most common male: ", mCount.most_common(N);
    print "Total male words: ", sum(mCount.values())
    """














main();
