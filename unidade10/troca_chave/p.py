def troca_chave(dic):
    novo = {}
    
    for chave, valor in dic.iteritems():
        novo[valor] = chave
    return novo
