def insere_ordenado_primeiro(lista):
    for j in range(len(lista)):
        for i in range(len(lista)-1):
            if lista[len(lista)-1 - i] < lista[len(lista)-2 - i]:
                lista[len(lista)-1-i], lista[len(lista)-2 -i] = lista[len(lista)-2-i], lista[len(lista)-1-i]
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]