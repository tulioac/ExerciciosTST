def agrupa_proximos(lista, valor, criterio):
    retorno = []
    for i in range(len(lista)):
        if abs(lista[i] - valor) < criterio:
            retorno.append(lista[i])
    return retorno