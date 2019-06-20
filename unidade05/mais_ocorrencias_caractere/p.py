def procura_letra(palavra, letra):
    contador = 0
    for i in palavra:
        if i == letra:
            contador += 1
    return contador


entrada = ''
palavras = []
impresso = False

while(True):
    entrada = raw_input()
    if entrada != 'fim':
        palavras.append(entrada)

    else:
        caractere = raw_input()
        numero = int(raw_input())

        for i in palavras:
            x = procura_letra(i, caractere)
            if x > numero:
                impresso = True
                print i

        if impresso == False:
            print "Nenhuma palavra encontrada."
            break
        
        break
