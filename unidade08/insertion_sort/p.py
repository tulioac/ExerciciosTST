def insertion_sort(lista):
    for i in range(1, len(lista)):
        atual = lista[i]
        k = i
        while k > 0 and atual < lista[k - 1]:
            lista[k] = lista[k-1]
            k -= 1
        lista[k] = atual