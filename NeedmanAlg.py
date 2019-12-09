import sys
from math import log,inf
import argparse


def main(sust,afin,penalty):
    referencia = str(input())
    secuencia = str(input())
    reflen = len(referencia) + 1
    seclen = len(secuencia) + 1

    delta = -1
    rho = 0
    a = [[0] * reflen for i in range(seclen)]
    ##inicializamos matrices de la f afín
    a_inf = [[0] * reflen for i in range(seclen)]
    a_der = [[0] * reflen for i in range(seclen)]

    a_der[0][1] = rho+delta
    for i in range(2,len(referencia)+1):
        a_der[0][i] = a_der[0][i-1] + delta
    for j in range(1,len(secuencia)+1):
        a_der[j][0] = -inf

    a_inf[1][0] = rho+delta
    for j in range (2,len(secuencia)+1):
        a_inf[j][0] = a_inf[j-1][0] + delta
    for i in range (1,len(referencia)+1):
        a_inf[0][i] = -inf

    for i in range(1,len(referencia)+1):
        a[0][i] = a_der[0][i]
    for j in  range (1,len(secuencia)+1):
        a[j][0] = a_inf[j][0]

    for i in range(1, len(secuencia) + 1):
        for j in range(1, len(referencia) + 1):
            similaridad = sustitiution(referencia[j-1],secuencia[i-1])
            a_der[i][j] = max(a_der[i][j-1] + delta,a[i][j-1] + delta+rho)
            a_inf[i][j] = max(a_inf[i-1][j] + delta, a[i-1][j] + delta +rho)
            a[i][j] = max(a[i-1][j-1]+similaridad, a_der[i][j], a_inf[i][j])

    print(alignment(a,a_der,a_inf,referencia,secuencia))


def sustitiution(a, b):
    sub_list=["a","c","g","t"]
    indexref=sub_list.index(a)
    indexsec = sub_list.index(b)

    matrix_sust = [[1,-1,-1,-1], [-1,1,-1,-1], [-1,-1,1,-1], [-1,-1,-1,1]]
    value =matrix_sust[indexref][indexsec]
    return value

def alignment(a,a_der,a_inf,referencia,secuencia):
    i,j =  len(secuencia),len(referencia)
    string_a = ""
    string_b = ""
    while i != 0 or j != 0:
        similitud = sustitiution(referencia[j-1],secuencia[i-1])
        if i > 0 and j > 0  and (a[i][j] == similitud + a[i-1][j-1]):
           i -= 1
           j -= 1
           string_a += referencia[j]
           string_b += secuencia[i]
        elif a[i][j] == a_inf[i][j] and i > 0 :
           i -= 1
           string_a += "-"
           string_b += secuencia[i]
        elif a[i][j] == a_der[i][j] and j > 0:
           j -= 1
           string_a += referencia[j]
           string_b += "-"

    return string_a[::-1],string_b[::-1]

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Alineamiento global')
    parser.add_argument("--s", action='store_true',default=False)
    parser.add_argument("--a",action='store_true',default=False)
    parser.add_argument("--ac",action='store_true',default=False)
    args = parser.parse_args()
    main(args.s, args.a, args.ac)
