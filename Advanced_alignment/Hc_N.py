import operator

def main(seq,ref):
    z = ""
    w = ""
    print(hirschberg(seq,ref,z,w))


def score(seq,ref):
    score = [[0] * (len(seq)+1) for i in range(2)]
    for j in range(1,len(seq)+1):
        score[0][j] = score[0][j-1] -1
    for i in range(0,2):
        score[i][0] = score[i-1][0] -1
        for j in range(1,len(seq)+1):
            similarity = 1 if ref[i - 1] == seq[j - 1] else -1
            diag = score[i-1][j-1] + similarity
            izq = score[i][j-1] -1
            der = score[i-1][j] -1
            score[i][j] = max(diag,izq,der)
        score[0][:] = score[1][:]
    lastline = []
    for j in range(len(seq)+1):
        lastline.append(score[1][j])
    return lastline

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
        #print(ref, seq)
        l =list(needlemanWunsch(ref,seq))
        print(l)
    else:
        refmid = len(ref) // 2  ##siempre a la mitad
        rev = ref[::-1]
        scoreizq = score(seq, ref[:refmid+1])
        scoreder = score(seq[::-1],rev[refmid:])
        seqmid = find_max_pos(scoreizq,reversed(scoreder))
        z,w= hirschberg(seq[ :seqmid],ref[:refmid],z,w), hirschberg(seq[seqmid:],ref[refmid:],z,w)
        # seqmidiz = (len(seq) + 1) // 2
        # seqmidder = len(seq) // 2
        #z,w= hirschberg(seq[ :seqmidder],ref[:refmid],z,w), hirschberg(seq[seqmidiz-1:],ref[refmid:],z,w)
    return (z,w)

def find_max_pos(score1,score2):
    pts = [s1 + s2 for s1, s2 in zip(score1, score2)]
    maximo = max(pts[::-1])
    pos = pts.index(maximo)
    return pos

def needlemanWunsch(ref,seq):
    dp_table = [[0] * (len(seq)+1) for i in range(len(ref)+1)]
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
        m = max(a,b,c)
        if m == a:
            i -= 1
            j -= 1
        elif m == b:
            i -= 1
        elif m == c:
            j -= 1
    yield (i,j)

if __name__ == '__main__':
    ref = "AGTACGCA"
    seq = "TATGC"
    """for nums in needlemanWunsch(ref,seq):
       i,j=nums
       print(nums)"""

    main(seq,ref)

