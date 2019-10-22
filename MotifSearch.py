from collections import Counter

def main():
    long_motiv = 8 ##tamaño del motivo (cantidad de nucleotidos)
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
    #print(simpleMedianSearch(dna, cant_seq, n, long_motiv))
    print(bbMedianSearch(dna, cant_seq, n, long_motiv))
    #####

def bbMedianSearch(dna,t,n,l):
    s = [0] * t
    best_distance = 100
    i = -1
    best_word = ""
    while True:
        if i < (t - 1):
            prefix = to_nucleotides(s)
            optim_distance = total_distance(dna,prefix,l)
            if optim_distance > best_distance:
               s, i = bypass(s,i,l,4)
            else:
               s, i = nextvertex(s, i,t,4)
        else:
            word = to_nucleotides(s)
            if total_distance(dna,word,l)<best_distance:
               best_distance = total_distance(dna,word,l)
               best_word = word
            s,i=nextvertex(s, i,t, 4)
        if i == -1:
            break

    return best_word


def to_nucleotides(s):
    prefix = ""
    for i in s:
        if i==0:
           prefix += "A"
        elif i==1:
            prefix += "C"
        elif i==2:
            prefix += "G"
        elif i==3:
            prefix += "T"

    return prefix

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


def total_distance(dna,s,l):
    long_dna_seq = 40
    total_distance = 0

    for seq in dna:
        min_dist=l
        for i in range(long_dna_seq-(l-1)):
            distance = sum(c1 != c2 for c1, c2 in zip(s, seq[i:i+l]))
            if distance < min_dist:
               min_dist = distance
               distance = 0
        total_distance+=min_dist

    return total_distance


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

def consensusString(s, dna, k):
    """ Calculate consensus score where:
        s is a vector of positions
        dna is a matrix of same-length sequences
        k is the length of the consensus string
    """
    cons_string = ""

    for i in range(0, k):
        c = Counter(seq[offset+i] for seq, offset in zip(dna,s))
        [(base, freq)] = c.most_common(1)
        cons_string += base

    return cons_string


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
