def troca(lista, i, j):
    lista[i], lista[j] = lista[j], lista[i]

def insere_ordenado_impostor(lista):
    for i in range(len(lista)-1):
        for k in range(len(lista)-1):
            if lista[k] > lista[k+1]:
                troca(lista, k, k+1)
