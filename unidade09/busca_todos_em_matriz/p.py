def busca_matriz(m, e): 
    posicoes = []

    for coluna in range(len(m[0])):
        for linha in range(len(m)):
            if m[linha][coluna] == e:
                posicoes.append((linha, coluna))
    return posicoes
