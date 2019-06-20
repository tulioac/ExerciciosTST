def troca(lista, i, j):
    lista[i], lista[j] = lista[j], lista[i]

def flip(lista, i, j):
    print lista, "inicio"
    for z in range(0, i-j, -1):
        for k in range(i, j+z):
                troca(lista, k, k+1)

    print lista

l1 = [1, 2, 3, 4, 5, 6, 7]
flip(l1, 2, 5)
print "[1, 2, 6, 5, 4, 3, 7]" + ' *'