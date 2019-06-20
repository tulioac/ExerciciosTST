def filtra_lista(num, lista):
    nova_lista = []
    for i in range(len(lista)):
        if i % num == 0:
            nova_lista.append(lista[i])
    return nova_lista

lista1 = [0,1,2,3,4,5,6]
print filtra_lista(2, lista1)