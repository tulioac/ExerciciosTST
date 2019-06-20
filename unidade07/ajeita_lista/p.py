def minimo_impar(lista, posicao):
    minimo = 10000000
    posicao_min = -1
    for i in range (posicao, len(lista)):
        if lista[i] < minimo and lista[i] % 2 != 0:
            minimo = lista[i]
            posicao_min = i

    return posicao_min

def maximo_par(lista, posicao):
    maximo = -10000000
    posicao_max = -1
    for i in range (posicao, len(lista)):
        if lista[i] > maximo and lista[i] % 2 == 0:
            maximo = lista[i]
            posicao_max = i

    return posicao_max

def troca_posicao(lista, atual, desejada):
    if atual > desejada:
        lista.insert(desejada, lista[atual])
        lista.pop(atual+1)
    else:
        lista.insert(desejada+1, lista[atual])
        lista.pop(atual)
    return lista

def ajeita_lista(lista):
    for i in range(len(lista)):
        posicao_minimo_impar = minimo_impar(lista, i)
        troca_posicao(lista, posicao_minimo_impar, i)
        posicao_maximo_par =  maximo_par(lista, i)
        troca_posicao(lista, posicao_maximo_par, i)