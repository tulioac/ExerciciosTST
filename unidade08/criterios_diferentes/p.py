def ordena(lista1, lista2):
    nova_lista = []
    i = 0
    j = len(lista2) - 1

    while True:
        if j == -1 and i <= len(lista1) - 1:
            nova_lista.append(lista1[i])
            if i < len(lista1):
                i += 1
        if i == len(lista1) and j >= 0:
            nova_lista.append(lista2[j])
            if j > -1:
                j -= 1
        if i <= len(lista1) -1 and j >= 0:
            if lista1[i] <= lista2[j]:
                nova_lista.append(lista1[i])
                if i < len(lista1):
                    i += 1
            elif lista1[i] > lista2[j]:
                nova_lista.append(lista2[j])
                if j > -1:
                    j -= 1

        if len(nova_lista) == len(lista1) + len(lista2):
            break

    return nova_lista

l1 = [3.9, 4.0]
l2 = [1.9]

print ordena(l1, l2)
