def swap(lista, i, j):
    lista[i], lista[j] = lista[j], lista[i]

def ajeita_lista(lista):
    def impar(i): return lista[i] % 2 == 1
    def par(i): return lista[i] % 2 == 0

    for i in range(len(lista)):
        for j in range(len(lista) - 1, 0, -1):
            if par(j) and impar(j - 1) or \
               par(j) and par(j - 1) and lista[j] > lista[j - 1] or \
               impar(j) and impar(j - 1) and lista[j] < lista[j - 1]:
                swap(lista, j, j - 1)