"""
    P4 CILN -Tagging basado en unigramas-

    Autors:
            Roman Rey Pedrero   : 183694
            Sergi Sorigue Arnau : 184753
"""



corpus = "corpus.txt";

EOF = "\r\n"

"""
    Funcio readCorpus: llegeix un corpus i el carrega a un diccionari, comptant
    el nombre d'ocurrences de cada tipus de paraula.
    Aquesta funcio crea l'arxiu lexic.txt
"""
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
"""
    Funcio crearLexic: Guarda al fitxer lexic.txt el diccionari seguint el format
"""
def crearLexic(diccionari):
    # Ara guardar el output en un fichero lexic con el formato:
    # Cantar    V   440
    # Perro     N   330
    # Perro     Adj 30

    file = open("lexic.txt","w");

    for paraula in diccionari:
        for tipus in diccionari[paraula]:
            #print paraula, "\t" ,tipus, "\t", diccionari[paraula][tipus]
            file.write(paraula + "\t" + tipus + "\t" + str(diccionari[paraula][tipus]) + EOF )
    file.close()


"""
    Funcio readTest: donat un fitxer de paraules, generem un fitxer amb les mateixes
    i el tipus de paraula mes frequent al diccionari.
"""
def readTest(filename_in, filename_out, diccionari):

    file_out = open(filename_out,"w")

    with open(filename_in) as file:
        for line in file:
            # El tipus mes comu es NP
            etiqueta = "NP"
            # rstrip per ,\r\n
            paraula = line.decode("latin_1").encode("UTF-8").rstrip()
            # Posem tipus mes frequent
            if paraula in diccionari:
                maxocurrences = 0
                for tipus in diccionari[paraula]:
                    if maxocurrences < diccionari[paraula][tipus]:
                        maxocurrences = diccionari[paraula][tipus]
                        etiqueta = tipus
            # Write al file
            file_out.write(paraula + "\t" + etiqueta + EOF)

    file.close()
    file_out.close()
"""
    Funcio evaluate: compara el fitxer generat i el fitxer amb les paraules ja etiquetades
    i calcula la precisio  prediccions_correctes / total_prediccions
"""
def evaluate(filename_generated, filename_gold):
    # Obrim fitxers
    file_gold = open(filename_gold,"r")
    file_generated = open(filename_generated,"r").read() #read() perque iterarem

    correct = 0.0
    total = 0.0

    # Per cada linia del fitxer golden
    for dirtyLine in file_gold:
        line = dirtyLine.decode("latin_1").encode("UTF-8")
        # Si existeix al que hem generat --> +1
        if line in file_generated:
            correct +=1
        total += 1
    print "corr", correct, "tot", total
    return correct/total;


"""
    MAIN del programa, s'executen les funcions anteriors sequencialent.
    Creem el diccionari, realitzaem els tests, i els avaluem
"""
def main():
    diccionari = dict();
    # Llegir fitxer corpus.txt i guardarlo a lexic.txt
    readCorpus(diccionari);
    # generar els fitxer test_x_out
    readTest("test_1.txt", "test_1_out.txt", diccionari);
    readTest("test_2.txt", "test_2_out.txt", diccionari);
    # comparar gold_standard_1 amb test_1
    avaluacio1 = evaluate("test_1_out.txt", "gold_standard_1.txt")
    # comparar gold_standard_2 amb test_2
    avaluacio2 = evaluate("test_2_out.txt", "gold_standard_2.txt")

    print "test_1", avaluacio1;
    print "test_2", avaluacio2


main();
