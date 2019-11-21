from math import log,log10
import math

def markov(symbols,states,matrizA,matrizE,output_list):
    # settings
    trelli_1 = {}
    trelli_2 = {}
    trelli_aux = {}

    # end settings
    for state in states:
        trelli_1[state] = []
        trelli_2[state] = []
        trelli_aux[state] = []
    # init trelli_1 and trelli_2
    for state in states:
        indexi = symbols.index(output_list[0])
        indexj = states.index(state)
        trelli_1[state].append(matrizA[indexi][indexj]/len(symbols))
        trelli_2[state].append("0")
    # complete trellis
    maxm = -1
    for i in range(1,len(output_list)):
        for st in states:
            maxm = -10
            st_m=""
            for state in states:
                #val1 =  trelli_1[state][-1] * (matrizA[symbols.index(output_list[i])][states.index(state)]) * (matrizE[states.index(st)][states.index(state)])
                val1 =  math.exp(log10(trelli_1[state][-1]) + log10(matrizA[symbols.index(output_list[i])][states.index(state)]) + log10(matrizE[states.index(st)][states.index(state)]))
                if val1>maxm:
                    st_m=state
                    maxm = val1
                maxm = max(val1,maxm)
                print(maxm)
                #maxm =
            trelli_2[st].append(st_m)
            trelli_aux[st].append(maxm)

        #print(trelli_aux)
        for st in states:
            trelli_1[st].append(trelli_aux[st][-1])
    #print(matrizA[symbols.index("T")][states.index("F")])
    n = -1
    st_b=""
    for st in states:
        if trelli_1[st][-1]>n:
            st_b=st
            n = trelli_1[st][-1]


    print(trelli_1)
    print(trelli_2)
    print(trelli_2[st_b])


if __name__ == '__main__':

    symbols = ["H", "T"]
    states = ["F", "B"]
    matrizA = [[0.50, 0.75], [0.5, 0.25]]
    matrizE = [[0.7, 0.3], [0.3, 0.7]]
    output_list = ["T", "H", "H", "H", "H", "H", "H"]

    markov(symbols,states,matrizA,matrizE,output_list)