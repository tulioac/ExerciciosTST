entrada = ''
quantidade_de_elementos = 0
indices = []
posicao = 0

while(entrada != 'fim'):
    entrada = raw_input()
    if entrada != 'fim':
        if int(entrada) >= 0:
            quantidade_de_elementos += 1
        else:
            indices.append(quantidade_de_elementos)
            quantidade_de_elementos = 0

if len(indices) > 0:
    tamanho_maximo = 0
    for i in range(len(indices)):
        if indices[i] > tamanho_maximo:
            tamanho_maximo = indices[i]
            posicao = i

    print "Conjunto %d - %d elemento(s)" % (posicao + 1, tamanho_maximo)