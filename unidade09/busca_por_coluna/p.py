def busca_todos_por_coluna_em_matriz(m, e): 
    posicoes = []

    for coluna in range(len(matriz[0])):
        for linha in range(len(matriz)):
            if matriz[linha][coluna] == e:
                posicoes.append((linha, coluna))
    return posicoes


matriz = [
    [2, 3, 5, 3, 1],
    [3, 2, 1, 5, 6],
    [3, 2, 3, 2, 1],
]

busca_todos_por_coluna_em_matriz(matriz, 4)