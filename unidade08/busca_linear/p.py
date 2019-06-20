def busca(seq, valor):
    for i in range(len(seq)):
        if seq[i] == valor:
            return i
    return -1