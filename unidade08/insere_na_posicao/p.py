def troca(lista, i, j):
    lista[i], lista[j] = lista[j], lista[i]

def meu_insert(lista, num, pos):
    lista.append(num)
    for i in range(len(lista) - 1, pos, -1):
        troca(lista, i, i-1)

def na_posicao(lista, a_inserir):
    for i in range(len(a_inserir)):
        meu_insert(lista, a_inserir[i][0], a_inserir[i][1])
    print lista

l = [10, 20, 30]
a_inserir = [(5, 1), (-2, 4), (0, 0)]

na_posicao(l, a_inserir)