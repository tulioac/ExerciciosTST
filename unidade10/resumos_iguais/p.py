def meuIn(elemento, lista):
    for i in lista:
        if i == elemento:
            return True
    return False

def conta_soma(numero):
    soma = 0
    numero = str(numero)
    for i in numero:
        soma += int(i)
    return soma


def agrupa_resumos_iguais(lista):
    resumo = {}

    for i in lista:
        soma = conta_soma(i)
        if not meuIn(soma, resumo):
            resumo[soma] = [i]
        else:
            resumo[soma].append(i)
    return resumo

lista1 = [60, 343, 19, 1230, 51, 123]

print agrupa_resumos_iguais(lista1)