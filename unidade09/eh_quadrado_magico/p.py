def eh_quadrado_magico(quadrado):
    soma_linhas = [0] * len(quadrado)
    soma_colunas = [0] * len(quadrado[0])
    soma_diagonais = [0, 0]

    for linha in range(len(quadrado)):
        for coluna in range(len(quadrado[0])):
            soma_linhas[linha] += quadrado[linha][coluna]

    for coluna in range(len(quadrado[0])):
        for linha in range(len(quadrado)):
            soma_colunas[coluna] += quadrado[linha][coluna]

    for i in range(len(quadrado)):
        print quadrado[i][i]
        soma_diagonais[0] += quadrado[i][i]

    k = len(quadrado)
    for i in range(len(quadrado)):
        k -= 1
        soma_diagonais[1] += quadrado[i][k]

    print soma_colunas
    print soma_linhas
    print soma_diagonais    

    condicao_linhas = True
    for i in range(len(soma_linhas) - 1):
        if soma_linhas[i] != soma_linhas[i+1]:
            condicao_linhas = False

    condicao_colunas = True
    for i in range(len(soma_colunas) - 1):
        if soma_colunas[i] != soma_colunas[i+1]:
            condicao_colunas = False

    condicao_diagonais = True
    for i in range(len(soma_diagonais) - 1):
        if soma_diagonais[i] != soma_diagonais[i+1]:
            condicao_diagonais = False

    return condicao_linhas and condicao_colunas and condicao_diagonais

quadrado1 = [[2,7,6],[9,5,1],[1,3,8]]
quadrado2 = [[1,2,3],[4,5,6]]

print eh_quadrado_magico(quadrado1)
print eh_quadrado_magico(quadrado2)