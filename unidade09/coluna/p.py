def coluna(matriz, i):
    lista = []

    for coluna in range(len(matriz[0])):
        for linha in range(len(matriz)):
            if coluna == i:
                lista.append(matriz[linha][coluna])

    return lista