corpus = "corpus.txt";

def readCorpus(diccionari):
    file = open("corpus.txt", "r");
    with open(corpus) as file:
        for line in file:
            lineAux = line.decode("latin_1").encode("UTF-8")
            (paraula, tipus) = lineAux.split()[0], lineAux.split()[1]
            if paraula not in diccionari:
                entrades = dict()
                entrades[tipus] = 1
                diccionari[paraula] = entrades
            else:
                # Quan no existeix la prep la creem
                if tipus not in diccionari[paraula]:
                    diccionari[paraula][tipus] = 1
                    #diccionari[paraula] = entrades
                # Quan ja existeix la prep, incrementem en 1 el nombre d'aparicions
                else:
                    diccionari[paraula][tipus] += 1;
                    #print paraula, ":", diccionari[paraula]

        # Creem l'arxiu de lexic
        crearLexic(diccionari)



def crearLexic(diccionari):
    # Ara guardar el output en un fichero lexic con el formato:
    # Cantar    V   440
    # Perro     N   330
    # Perro     Adj 30
    for paraula in diccionari:
        print paraula, " " ,diccionari[paraula]
        #for tipus in paraula:
        #    print paraula, " ", tipus, " "#, diccionari[paraula][tipus]



    """
    (paraula, prep) = line.split()


    entrades = dict();
    entrades[prep] = 1;
    diccionari[paraula] = entrades;


    print diccionari;
    """



def main():
    diccionari = dict();
    # Llegir fitxer corpus.txt i guardarlo
    readCorpus(diccionari);
    # llegir fitxer test_1 i compararlo amb el diccionari

    # escriure en el fitxer test_1 el que es (nom, adv...)

    # comparar gold_standard_1 amb test_1

    # repetir amb test_2

main();
