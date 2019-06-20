def agrupa_negativos(lista):
    dic = {"nao-negativos":[], "negativos":[]}

    for i in lista:
        if i < 0:
            dic["negativos"].append(i)
        else:
            dic["nao-negativos"].append(i)
    return dic

print agrupa_negativos([10, -2, -7, 8])
