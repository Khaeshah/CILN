corpus = "corpus.txt";

def readCorpus(diccionari):

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

        file.close()

def crearLexic(diccionari):
    # Ara guardar el output en un fichero lexic con el formato:
    # Cantar    V   440
    # Perro     N   330
    # Perro     Adj 30

    file = open("lexic.txt","w");


    for paraula in diccionari:
        for tipus in diccionari[paraula]:
            #print paraula, "\t" ,tipus, "\t", diccionari[paraula][tipus]
            file.write(paraula + "\t" + tipus + "\t" + str(diccionari[paraula][tipus]) + "\r\n" )
    file.close()

def readTest(filename_in, filename_out, diccionari):


    file_out = open(filename_out,"w")


    with open(filename_in) as file:
        for line in file:
            etiqueta = "NP"
            # rstrip per ,\r\n
            paraula = line.decode("latin_1").encode("UTF-8").rstrip()
            if paraula in diccionari:
                maxocurrences = 0
                for tipus in diccionari[paraula]:
                    if maxocurrences < diccionari[paraula][tipus]:
                        maxocurrences = diccionari[paraula][tipus]
                        etiqueta = tipus
            file_out.write(paraula + "\t" + etiqueta + "\r\n")

    #llegim test1

    file.close()
    file_out.close()

def evaluate(filename_generated, filename_gold):
    correctes = 0.0;
    total = 0.0;

    file_gold = open(filename_gold, "r")

    with open(filename_generated) as file_generated:
        for line in file_generated:
            (paraula, tipus) = line.split("\t")

            

            if paraula+"\t"+tipus in file_gold:
                correctes += 1
            total += 1
    print "correctes", correctes, "total", total
    return correctes/total;

def main():
    diccionari = dict();
    # Llegir fitxer corpus.txt i guardarlo
    readCorpus(diccionari);
    # escriure en el fitxer test_1 el que es (nom, adv...)
    readTest("test_1.txt", "test_1_out.txt", diccionari);
    # comparar gold_standard_1 amb test_1
    print evaluate("test_1_out.txt", "gold_standard_1.txt")

    # repetir amb test_2

main();
