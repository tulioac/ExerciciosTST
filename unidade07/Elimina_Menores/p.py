def elimina_menores(num, lista):
    contador = 0
    for i in range(len(lista)-1, -1, -1):
        if lista[i] < num:
            lista.pop(i)
            contador += 1
    return contador