import numpy as np
def main():
    ref = "GATTACA"
    seq = "GCAATCA"

    n = min(len(ref), len(seq))
    m = max(len(ref), len(seq)) +1

    ##Init 2 lists
    col1=[0 * i for i in range(m)]
    col2=[0 * i for i in range(m)]
    cont = 0
    for i in range(m):
        col1[i]=cont
        cont -= 1
    #print(col1,col2)
    ##
    while n >= 2:
        n = (n+1)//2
        contt=0
        m-=contt
        for i in range(n):
            for j in range(m):
                if j == 0 :
                    col2[j] = col1[j]  - 1
                else:
                    diag = col1[j-1]
                    izq = col1[j] - 1
                    sup = col2[j-1] - 1
                    #print(ref[j-1],seq[i])
                    if ref[j-1] == seq[i]:
                        col2[j] = max(diag + 1, sup, izq)
                    else:
                        col2[j] = max(diag - 1, sup, izq)
                # necesito el mayor de la segunda fila y la pos
            print([(x, y) for (x, y) in zip(col1, col2)])
            col1=col2
            print(col1)
            col2=[0 * i for i in range(m)]
            #maxi,pos=find_max_pos(matrix,m)
            #print("maximo: ",maxi," en la pos: ",pos)
            # inverse
       n=0


    # una vez que tengo el mayor divido prefix[] y sink[] y empiezo a buscar los mayores de cada mitad recursivamente
def find_max_pos(matrix,m):
    maxi = 0
    pos = 0
    for i in range(m):
        if matrix[i][1] > maxi:
            maxi = matrix[i][1]
            pos = i
    return (maxi, pos)

def max_score():



if __name__ == '__main__':
    main()
