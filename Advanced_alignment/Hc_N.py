import operator

def main(seq,ref):
    #ref = "AGTACGCA"
    #seq = "TATGC"
    z = ""
    w = ""
    print(hirschberg(seq,ref,z,w))


def score(seq,ref):
    m = len(ref)
    col1 = [0 * i for i in range(m)]
    col2 = [0 * i for i in range(m)]
    cont = 0
    for i in range(m):
        col1[i] = cont
        cont -= 1
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
        return col1

def hirschberg(seq,ref,z,w):
    if len(ref) == 0:
      for i in range(len(seq)):
        z = z + "-"
        w = w + seq[i]
    elif len(seq) == 0:
        for i in range(len(ref)):
            z += ref[i]
            w += "-"
    elif len(ref) == 1 or len(seq) == 1:
        l = list(needlemanWunsch(ref,seq))
        print(l)
    else:
        refmid = len(ref) // 2
        rev = ref[::-1]
        scoreizq = score(seq, ref[:refmid])
        scoreder = score(seq[::-1],rev[refmid:])
        seqmid = find_max_pos(scoreizq,reversed(scoreder))
        z,w= hirschberg(ref[: refmid],seq[ :seqmid+1],z,w), hirschberg(ref[refmid:],seq[seqmid:],z,w)
    return (z,w)

def find_max_pos(score1,score2):
    pts = [s1 + s2 for s1, s2 in zip(score1, score2)]
    maximo = max(pts)
    pos = pts.index(maximo)
    return pos

def needlemanWunsch(ref,seq):
    dp_table = [[0] * (len(seq)+1)  for i in range(len(ref)+1)]
    for i in range(1, len(ref)+1):
        for j in range(1, len(seq)+1):
            similarity = 1 if ref[i-1] == seq[j-1] else -1
            gap_penalty = -1
            dp_table[i][j] = max(
                    dp_table[i-1][j-1] + similarity,
                    dp_table[i-1][j] + gap_penalty,
                    dp_table[i][j-1] + gap_penalty
                    )
    i, j = len(ref), len(seq)
    while i != 0 and j != 0:
        yield (i,j)
        #print(ref[i-1],seq[j-1])
        similarity = 1 if ref[i-1] == seq[j-1] else -1
        gap_penalty = -1
        a, b, c = dp_table[i-1][j-1] + similarity, dp_table[i-1][j] + gap_penalty, dp_table[i][j-1] + gap_penalty
        m = min(a,b,c)
        if m == a:
            i -= 1
            j -= 1
        elif m == b:
            i -= 1
        elif m == c:
            j -= 1
    yield (i,j)

if __name__ == '__main__':
    ref = "GATTACA"
    seq = "GATTACA"
    #for nums in needlemanWunsch(ref,seq):
       #i,j=nums
       #print(nums)

    main(seq,ref)

