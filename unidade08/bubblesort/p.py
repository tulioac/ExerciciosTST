def troca(dados, i, j):
    dados[i], dados[j] = dados[j], dados[i]

def bubblesort(dados):
    while True:
        trocou = False
        for i in range(len(dados)-1):
            if dados[i] > dados[i+1]:
                troca(dados, i, i+1)
                trocou = True
        if not trocou:
            break
    print dados
