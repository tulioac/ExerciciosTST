def anula(lista):
    k = len(lista)
    while True:
        k -= 1
        if len(lista) > 1:
            if lista[k] + lista[k-1] == 0:
                lista.pop(k), lista.pop(k-1)
                k = len(lista) - 1
            if k == -1:
                break
        else:
            break
