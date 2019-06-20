def desloca(lista, origem, destino):
    for i in range(origem, destino):
        lista[i], lista[i+1] = lista[i+1], lista[i]