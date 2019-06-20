def meuIn(elemento, estrutura):
    for elemento_atual in estrutura:
        if elemento == elemento_atual:
            return True
    return False

def inv_dic(dic):
    invertido = {}
    for chave, valor in dic.iteritems():
        if meuIn(valor, invertido):
            invertido[valor].append(chave)
        else:
            invertido[valor] = [chave]
    return invertido

dicionario = {'a': 2, 'b': 3, 'c': 2}

print inv_dic(dicionario)
