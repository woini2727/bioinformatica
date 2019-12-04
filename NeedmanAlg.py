import sys
from math import log


def main(argv):
    afin = False
    sust = False
    penalty = False
    if len(argv)>1:
        if argv[1]=="-s":
            sust = True
        elif argv[1]=="-a":
            afin = True
        elif argv[1]=="-ac":
            penalty = True
    referencia = str(input())
    secuencia = str(input())
    reflen = len(referencia) + 1
    seclen = len(secuencia) + 1

    a = [[0] * reflen for i in range(seclen)]

    ##inicializamos matrices de la f afín
    a_inf = [[0] * reflen for i in range(seclen)]
    a_der = [[0] * reflen for i in range(seclen)]

    # inicializamos
    if not penalty:
        lmb = 1
        for i in range(len(referencia) + 1):
            lmb -= 1
            a[0][i] = lmb
            a_inf[0][i] = lmb
            a_der[0][i] = lmb
        lmb = 1
        rho = 2
        for i in range(len(secuencia) + 1):
            lmb -= 1
            a[i][0] = lmb
            a_inf[i][0] = lmb
            a_der[i][0] = lmb
            # print(a)
        for i in range(1, len(secuencia) + 1):
            for j in range(1, len(referencia) + 1):
                diag = a[i - 1][j - 1]
                izq = a[i][j - 1] - 1
                sup = a[i - 1][j] - 1

                if sust:
                    value = sustitiution(referencia, secuencia, j - 1, i - 1)
                    a[i][j] = max(diag + value, sup, izq)
                elif afin:
                    a_inf[i][j] = max(a_inf[i - 1][j] - 1, a[i - 1][j] - rho)
                    a_der[i][j] = max(a_der[i][j - 1] - 1, a[i][j - 1] - rho)
                    if referencia[j - 1] == secuencia[i - 1]:
                        a[i][j] = max(diag + 1, a_der[i][j], a_inf[i][j])
                    else:
                        a[i][j] = max(diag - 1, a_der[i][j], a_inf[i][j])
                else:
                    if referencia[j - 1] == secuencia[i - 1]:
                        a[i][j] = max(diag + 1, sup, izq)
                    else:
                        a[i][j] = max(diag - 1, sup, izq)

    else:
        lmb = 1
        rho = -2
        for i in range(len(referencia) + 1):
            a[0][i] = lmb
            a_inf[0][i] = lmb
            a_der[0][i] = lmb
        for i in range(len(secuencia) + 1):
            a[i][0] = lmb
            a_inf[i][0] = lmb
            a_der[i][0] = lmb
        lmb = -1
        print(a_inf)
        for i in range(1, len(secuencia) + 1):
            for j in range(1, len(referencia) + 1):
                if referencia[j - 1] != secuencia[i - 1]:
                    a_inf[i][j] = a_inf[i - 1][j] + 1
                    a_der[i][j] = a_der[i][j - 1] + 1
                    print(a_inf[i][j],a_der[i][j])
                    a[i][j] = lmb*(log(min(a_der[i][j],a_inf[i][j]))) + rho  ##penalty
                else:
                    a_inf[i][j] = 0
                    a_der[i][j] = 0
                    a[i][j] = 0

    print(a)
    print(alignment(a, reflen, seclen, referencia, secuencia))
    print("score: ", a[-1][-1])

def sustitiution(referencia, secuencia,posref,possec):
    sub_list=["a","c","g","t"]
    indexref=sub_list.index(referencia[posref])
    indexsec = sub_list.index(secuencia[possec])

    matrix_sust = [[1,-1,-1,-1], [-1,1,-1,-1], [-1,-1,1,-1], [-1,-1,-1,1]]
    value =matrix_sust[indexref][indexsec]
    return value

def alignment(matrix, n, n2, referencia, secuencia):
    lastj = int(n - 1)
    lasti = int(n2 - 1)
    listaAlig = [matrix[lasti][lastj]]
    listaAligcoord = [(lasti, lastj)]
    for i in range(1, n):
        diag = matrix[lasti - 1][lastj - 1]
        izq = matrix[lasti][lastj - 1]
        arr = matrix[lasti - 1][lastj]
        maximo = max(diag, arr, izq)
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
    for i in range(len(referencia)):
        if referencia[i] == newstring[i]:
            print("|", end="")
        else:
            print(" ", end="")
    print("")
    ##---------escribimos coincidencias------------------#########

    print(referencia.upper())
    return l



if __name__ == '__main__':
    main(sys.argv)
