import sys


def main(argv):
    sust=False
    if len(argv)>1:
        if argv=="-s":
            sust = True
    referencia = str(input())
    secuencia = str(input())
    reflen = len(referencia) + 1
    seclen = len(secuencia) + 1
    a = [[0] * reflen for i in range(seclen)]

    for i in range(1, len(secuencia) + 1):
        for j in range(1, len(referencia) + 1):
            diag = a[i - 1][j - 1]
            izq = a[i][j - 1] - 1
            sup = a[i - 1][j] - 1

            if sust:
                value = sustitiution(referencia, secuencia, j - 1, i - 1)
                a[i][j] = max(diag + value, sup, izq,0)
            else:
                if referencia[j - 1] == secuencia[i - 1]:
                    a[i][j] = max(diag + 1, sup, izq,0)
                else:
                    a[i][j] = max(diag - 1, sup, izq,0)
    print(a)
    print(alignment(a, reflen, seclen, referencia, secuencia))
    print("score: ",a[-1][-1])

def sustitiution(referencia, secuencia, posref, possec):
    sub_list = ["a", "c", "g", "t"]
    indexref = sub_list.index(referencia[posref])
    indexsec = sub_list.index(secuencia[possec])

    matrix_sust = [[1, -1, -1, -1], [-1, 1, -1, -1], [-1, -1, 1, -1], [-1, -1, -1, 1]]
    value = matrix_sust[indexref][indexsec]
    return value


def alignment(matrix, n, n2, referencia, secuencia):
    ##----------- get better score --------------------------###
    may=0
    lastj = 0
    lasti = 0
    for i in range(len(secuencia) + 1):
        for j in range(len(referencia) + 1):
            if matrix[i][j]>may:
               may=matrix[i][j]
               lasti=i
               lastj=j
    ##
    print("Result: ",may)
    listaAlig = [matrix[lasti][lastj]]
    listaAligcoord = [(lasti, lastj)]
    ##-------------------------------------------------------####

    zero=False
    while(not zero):
        diag = matrix[lasti - 1][lastj - 1]
        izq = matrix[lasti][lastj - 1]
        arr = matrix[lasti - 1][lastj]
        maximo = diag
        if diag==0:
            zero=True
        listaAlig.append(maximo)
        if maximo == diag:
            lasti = lasti - 1
            lastj = lastj - 1
        elif maximo == izq:
            lasti = lasti
            lastj = lastj - 1
        else:
            lasti = lasti - 1
            lastj = lastj

        listaAligcoord.append((lasti, lastj))
    l = listaAligcoord[::-1]
    l.pop(0)
    print(l)

    ##---------------escribimos la secuencia--------------######
    ant = -1
    newstring = ""
    for t in l:
        i, j = t
        if i - 1 == ant:
            print("-", end="")
            newstring += "-"
        else:
            ant = i - 1
            print(secuencia[i - 1].upper(), end="")
            newstring += secuencia[i - 1]
    print("")
    for i in range(len(newstring)):
        if referencia[len(referencia)-i-1:] == newstring[len(newstring)-i-1]:
            print("|", end="|")
        else:
            print(" ", end="")
    print("")
    ##---------escribimos coincidencias------------------#########
    for t in l:
        i, j = t
        print(referencia[j-1].upper(),end="")
    print("")
    return l


if __name__ == '__main__':
    main(sys.argv)
