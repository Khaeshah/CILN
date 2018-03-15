try:
    import Queue as Q
except ImportError:
    import queue as Q
import glob
from collections import Counter

def readData(fCount,mCount):

    path = './dataset/*'
    files = glob.glob(path)

    # Bucle que itera sobre tots els arxius
    for fileName in files:
        with open(fileName) as file:
            content = file.read()
            # Si es un fitxer escrit per una dona
            if fileName.endswith("_female"):
                fCount += Counter(content.strip().split())
            # Si es un fitxer escrit per un home
            if fileName.endswith("_male"):
                mCount += Counter(content.strip().split());


    print "Most common female: ", fCount.most_common(5);
    print "Total female words: ", sum(fCount.values())
    print "Most common male: ", mCount.most_common(5);
    print "Total male words: ", sum(mCount.values())

def main():
    # Creem un counter per guardar informacio de females i males
    countF = Counter()
    countM = Counter()
    # Llegim datasets
    readData(countF,countM)


main();
