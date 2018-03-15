try:
    import Queue as Q
except ImportError:
    import queue as Q
import glob,sys
from collections import Counter

def nFrequents(fCount,mCount):

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

def main():
    N = int(sys.argv[1])
    # Creem un counter per guardar informacio de females i males
    fCount = Counter()
    mCount = Counter()
    # Obtenim N mes frequents
    nFrequents(fCount,mCount)

    print "Most common female: ", fCount.most_common(N);
    print "Total female words: ", sum(fCount.values())
    print "Most common male: ", mCount.most_common(N);
    print "Total male words: ", sum(mCount.values())

    # Obtencio de feature vector
    # primera posicio: [#, #Mayusculas, # NP]

main();
