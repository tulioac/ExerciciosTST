def filtra_altera_lista(num, lista):
    for i in range(len(lista) - 1, -1, -1):
        if i % num != 0:
            lista.pop(i)