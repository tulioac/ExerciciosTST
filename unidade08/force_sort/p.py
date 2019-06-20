def force_sort(seq):
    diferencas = []
    if seq:
        diferencas.append(0)

        for i in range(len(seq)-1):
            if seq[i] > seq[i+1]:
                diferencas.append(abs(seq[i]-seq[i+1]))
                seq[i+1] = seq[i]
            else:
                diferencas.append(0)
    return diferencas
