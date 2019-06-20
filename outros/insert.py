def troca(lista, i, j):
    lista[i], lista[j] = lista[j], lista[i]

def meu_insert(lista, elemento):
    lista.append(elemento)

    for i in range(len(lista)-1, 0, -1):
        if lista[i][1] < lista[i-1][1]:
            troca(lista, i, i-1)
    print lista

fila = [("maria", 1.05), ("joao", 1.09), ("ana", 1.16)]

meu_insert(fila, ("jose", 1.12))
