matriz = [
    [2, 3, 5, 3, 1],
    [3, 2, 1, 5, 6],
    [3, 2, 3, 2, 1]
]

for coluna in range(len(matriz[0])):
    print
    for linha in range(len(matriz)):
        print matriz[linha][coluna]