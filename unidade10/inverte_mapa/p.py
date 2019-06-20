def cocktailSort(lista):
    for j in range(len(lista)):
        for i in range(len(lista)-1):
            if lista[len(lista)-1 - i] < lista[len(lista)-2 - i]:
                lista[len(lista)-1-i], lista[len(lista)-2 -i] = lista[len(lista)-2-i], lista[len(lista)-1-i]
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
    return lista


def inverte_dicionario(dic):
    inv_dic = {}
    for chave, valor in dic.iteritems():
        inv_dic[valor] = inv_dic.get(valor, [])
        inv_dic[valor].append(chave)

    for chave in inv_dic:
        inv_dic[chave] = cocktailSort(inv_dic[chave])
     
    return inv_dic


m = {"a": 2, "b": 3, "c": 2}
inverte_dicionario(m)