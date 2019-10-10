from collections import Counter

def main():
    long_motiv = 8  ##tamaño del motivo (cantidad de nucleotidos)
    base = 4  ##base 4
    dna = ["CGGGGCTATGCAACTGGGTCGTCACATTCCCCTTTCGATA",
           "TTTGAGGGTGCCCAATAAATGCAACTCCAAAGCGGACAAA",
           "GGATGCAACTGATGCCGTTTGACGACCTAAATCAACGGCC",
           "AAGGATGCAACTCCAGGAGCGCCTTTGCTGGTTCTACCTG",
           "AATTTTCTAAAAAGATTATAATGTCGGTCCATGCAACTTC",
           "CTGCTGTACAACTGAGATCATGCTGCATGCAACTTTCAAC",
           "TACATGATCTTTTGATGCAACTTGGATGAGGGAATGATGC"]
    cant_seq = len(dna) # cant de secuencias en la matriz
    n = len(dna[0]) # cant de nucleotidos x sec
    #print("bestcore", bfMotifSearch(dna, t, n, long_motiv))
    print(simpleMedianSearch(dna, cant_seq, n, long_motiv))
    #####

def simpleMedianSearch(dna,t,n,l):
    punteros = [0] * t
    best_score = 0  ##random high number
    best_motif = []
    i = -1
    while True:
        if i < (t-1):
            #print("i ", i)
            punteros, i = nextvertex(punteros, i,t, n-l+1)
        else:
            score_calculado = consensusScore(punteros, dna, l)
            if score_calculado > best_score:
               print(score_calculado)
               best_score = score_calculado
               best_motif = punteros[:]
            punteros, i = nextvertex(punteros,i, t, n-l+1)
        if i == -1:
            break

    return best_motif

def consensusScore(s, dna, k):
    """ Calculate consensus score where:
        s is a vector of positions
        dna is a matrix of same-length sequences
        k is the length of the consensus string
    """
    score = 0
    for i in range(0, k):
        c = Counter(seq[offset+i] for seq, offset in zip(dna,s))
        [(base, freq)] = c.most_common(1)
        score += freq
    return score

#L ALTURA DEL ARBOL =cant de secuencias
#k es el grado= long de la sec
def nextvertex(punteros, i, l, k):
    if i < (l-1):
        punteros[i+1] = 0
        tupla = (punteros, i + 1)
        return tupla
    else:
        for j in range(l-1, -1, -1):
            if punteros[j] < k-1:
                punteros[j] += 1
                tupla = (punteros, j)
                return tupla

    return punteros, -1

def bfMotifSearch(dna, t, n, l):
    s = [0, 0, 0, 0, 0, 0, 0]
    bestScore = score(s, dna)  ##comparo s vs matriz de DNA
    bestMotif = s
    motif = False
    while not motif:
        s = nextLeaf(s, t, n)
        scr = score(s, dna)
        # print(scr)
        if scr > bestScore:
            bestScore = scr
            bestMotif = s  ##hacer funcion que devuelva las posiciones
            print(bestScore)
        if bestMotif == [0, 0, 0, 0, 0, 0, 0]:
            motif = True
    return bestScore


def score(s, dna):
    l = 8
    t = 7
    baseA = []
    baseC = []
    baseG = []
    baseT = []
    for i in range(t):
        baseA.append(0)
        baseC.append(0)
        baseG.append(0)
        baseT.append(0)
    dicc = {"A": baseA, "C": baseC, "G": baseG, "T": baseT}
    # print(s)
    i = 0
    for secuencia in dna:
        cadena = secuencia[s[i]:s[i] + l]
        dicc = contarbases(cadena, dicc)
        i += 1

    ##sumo las bases y obtengo el score
    listamax = []
    for i in range(t):
        basea = dicc["A"]
        basec = dicc["C"]
        baseg = dicc["G"]
        baset = dicc["T"]
        maxi = max(basea[i], basec[i], baseg[i], baset[i])
        listamax.append(maxi)
    return sum(listamax)


def contarbases(cadena, dicc):
    for base in dicc.keys():
        lista = dicc[base]
        for i in range(len(cadena) - 1):
            if cadena[i] == base:
                lista[i] += 1
    return dicc


def nextLeaf(punteros, t, k):
    for i in range(t - 1, -1, -1):
        if punteros[i] < k-1:
            punteros[i] += 1
            return punteros
        punteros[i] = 0
    return punteros


def bypass(punteros,i,l,base):
    for j in range(i, -1, -1):
        if punteros[j] < base:
            punteros[j] += 1
            tupla = (punteros,j)
            return tupla
    tupla = (punteros, -1)
    return tupla

if __name__ == '__main__':
    main()
