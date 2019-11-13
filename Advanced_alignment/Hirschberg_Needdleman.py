
def main():
    ref = "GATTACA"
    seq = "GCAATCA"

    n = min(len(ref), len(seq))
    m = max(len(ref), len(seq))

    ##Init Matrix
    matrix = [[0] * 2 for i in range(m)]
    cont = 0
    for i in range(m):
        matrix[i][0] = cont
        matrix[i][1] = 0
        cont -= 1

    while n >= 2:
        # recorro la matriz de a 2 columnas hasta la mitad y me paro en el mayor de dicha columna mitad
        n = n//2
        contt=0
        m-=contt
        for j in range(m):
            if j == 0 :
                matrix[j][1] = matrix[j][0] - 1
            else:
                diag = matrix[j-1][0]
                izq = matrix[j][0] - 1
                sup = matrix[j-1][1] - 1
                    #matrix[j][1] = max(diag,izq,sup)
                print(ref[0] ,seq[j-1])
                if ref[0] == seq[j-1]:
                    matrix[j][1] = max(diag + 1, sup, izq)
                else:
                    matrix[j][1] = max(diag - 1, sup, izq)
        print(matrix)
        n=0
        # inverse

    # una vez que tengo el mayor divido prefix[] y sink[] y empiezo a buscar los mayores de cada mitad recursivamente


if __name__ == '__main__':
    main()
