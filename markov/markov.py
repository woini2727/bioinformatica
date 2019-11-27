from math import log, inf, exp

def markov(symbols, states, matrizA, matrizE, I, output_list):
    # settings
    trelli_1 = {}
    trelli_2 = {}

    # init trelli_1 and trelli_2
    for indexj, state in enumerate(states):
        indexi = symbols.index(output_list[0])
        trelli_1[state] = [0.0] * len(output_list)
        trelli_1[state][0] = log(I[state]) + log(matrizE[indexi][indexj])
        trelli_2[state] = ['0'] * len(output_list)

    # complete trellis
    for i in range(1,len(output_list)):
        for st_index, st in enumerate(states):
            max_previous = -inf # maxima probabilidad anterior hallada (excluye P. de emision)
            st_previous  = ""   # estado que genero max_previous

            # buscar el mejor estado anterior
            for state_index, state in enumerate(states):
                val1 = trelli_1[state][i-1] + log(matrizA[state_index][st_index])
                if val1 > max_previous:
                    max_previous = val1
                    st_previous = state

            # guardar probabilidad de transicionar a este estado y emitir el simbolo
            trelli_1[st][i] = max_previous + log(matrizE[symbols.index(output_list[i])][st_index])

            # guardar el estado anterior para backtracking
            trelli_2[st][i] = st_previous

    # backtracking hasta llegar al sentinela
    s = max(states, key=lambda st: trelli_1[st][-1])
    result = []
    while s != '0':
        result.append(s)
        s = trelli_2[s][-len(result)-1]
    result.reverse()

    print('Trellis 1')
    for state in states:
        print(state, *map(exp, trelli_1[state]))
    print('Trellis 2')
    for state in states:
        print(state, *trelli_2[state])
    print('Best Path')
    print(*result)


if __name__ == '__main__':
    symbols = ["H", "T"]
    states = ["F", "B"]
    matrizE = [[0.50, 0.75], [0.5, 0.25]]
    matrizA = [[0.7, 0.3], [0.3, 0.7]]
    I = {'F': 0.5, 'B': 0.5} # probabilidades iniciales

    markov(symbols,states,matrizA,matrizE,I, "THHHHHH")
    print()
    markov(symbols,states,matrizA,matrizE,I, "TTHHHHT")
