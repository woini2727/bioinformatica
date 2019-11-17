
def main():
    list_alig = []
    ref = "GATTACA"
    seq = "GCAATCA"
    if len(ref) < len(seq):
       seq_sup=ref
       seq_inf=seq
    else:
        seq_sup = seq
        seq_inf = ref
    n = len(seq) # mas corto fila
    m = len(ref) +1 # mas largo columna
    ##Init 2 lists
    col1=[0 * i for i in range(m)]
    col2=[0 * i for i in range(m)]
    cont = 0
    for i in range(m):
        col1[i]=cont
        cont -= 1

    # prefix (si la secuencia mas chica es par ++1)
    n = (n // 2) + 1
    prefix = seq[:n]
    sufix =  seq[n-1:]
    list_palabras = []
    list_palabras.append(prefix)
    list_palabras.append(sufix)

    while (len(list_palabras) !=0):
        prefix = list_palabras[0]
        list_alig,pos=max_score(m, ref, prefix, col1, col2,list_alig)
        ref = ref[:pos+1]
        list_palabras.pop(0)
        if prefix//2 !=1:
           list_palabras.append(prefix[(len(prefix)//2) -1:])
           list_palabras.append(prefix[:len(prefix)//2])




    #sufix

def find_max_pos(col,m):
    maxi = -100000
    pos = 0
    for i in range(m):
        if col[i] >= maxi:
            maxi = col[i]
            pos = i
    return (maxi, pos)

def max_score(m,ref,prefix,col1,col2,list_alig):
        #n = (n + 1) // 2
        contt = 0
        m -= contt
        print(col1)
        for i in range(len(prefix)):
            for j in range(m):
                if j == 0:
                    col2[j] = col1[j] - 1
                else:
                    diag = col1[j - 1]
                    izq = col1[j] - 1
                    sup = col2[j - 1] - 1
                    if ref[j - 1] == prefix[i]:
                        col2[j] = max(diag + 1, sup, izq)
                    else:
                        col2[j] = max(diag - 1, sup, izq)
            col1 = col2
            col2 = [0 * i for i in range(m)]
            print(col1)
        maxi,pos = find_max_pos(col1,m)
        list_alig.append(maxi)
        return (maxi,pos)

if __name__ == '__main__':
    main()
