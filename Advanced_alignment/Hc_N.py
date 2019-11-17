import operator

def main():
    ref = "AGTACGCA"
    seq = "TATGC"
    print(hirschberg(seq,ref))


def score(seq,ref):
    m = len(ref)
    col1 = [0 * i for i in range(m)]
    col2 = [0 * i for i in range(m)]
    cont = 0
    for i in range(m):
        col1[i] = cont
        cont -= 1
    print(col1)
    for i in range(len(seq)):
        for j in range(m):
            if j == 0:
                col2[j] = col1[j] - 1
            else:
                diag = col1[j - 1]
                izq = col1[j] - 1
                sup = col2[j - 1] - 1
                if ref[j - 1] == seq[i]:
                    col2[j] = max(diag + 1, sup, izq)
                else:
                    col2[j] = max(diag - 1, sup, izq)
        col1 = col2
        col2 = [0 * i for i in range(m)]
        print(col1)
        return col1

def hirschberg(seq,ref):
    z = ""
    w = ""
    if len(ref) == 0:
      for i in range(len(seq)):
        z = z + "-"
        w = w + seq[i]
    elif len(seq) == 0:
        for i in range(len(ref)):
            z += ref[i]
            w += "-"
    elif len(ref) == 1 or len(seq) == 1:
        z,w = needlemanWunsch(ref,seq)
    else:
        refmid = len(ref) // 2
        rev = ref[::-1]
        scoreizq = score(seq, ref[:refmid])
        scoreder = score(seq[::-1],rev[refmid:])
        seqmid = find_max_pos(scoreizq,scoreder)
        print(seqmid)
        z,w= str(hirschberg(ref[: refmid],seq[ :seqmid+1])),str( hirschberg(ref[refmid:],seq[seqmid+1:]))

    return (z,w)

def find_max_pos(score1,score2):
    pts = []
    for s1,s2 in zip(score1,score2):
        pts.append(s1+s2)
        print(s1+s2)
    maximo = max(pts)
    pos = pts.index(maximo)
    return pos

def needlemanWunsch(ref,seq):
    print(0)
    return "",""

if __name__ == '__main__':
    main()
