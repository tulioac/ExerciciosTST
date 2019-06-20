def quicksort(lista):
    def quicksort(lista, ini, fim):
        if fim == ini:
            return

        i_pivot = pivot(lista, ini, fim)
        quicksort(lista, ini, i_pivot - 1)
        quicksort(lista, i_pivot + 1, fim)

    quicksort(lista, 0, len(lista) - 1)

def pivot(seq, ini, fim):
    pivot = seq[0]
    i_vaga = ini

    for i in range(ini + 1, fim + 1):
        if seq[i] <= pivot:
            seq[i_vaga] = seq[i]
            i_vaga += 1
            if i_vaga < i:
                seq[i] = seq[i_vaga]

    seq[i_vaga] = pivot
    return i_vaga

    