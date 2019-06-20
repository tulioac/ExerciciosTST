alvo = int(raw_input())
entrada = ''
valores = []
contador = 0
qnt_maiores = 0

while (entrada != 'fim'):
    entrada = raw_input()
    qnt_maiores = 0
    contador += 1
    if entrada != 'fim':
        lista = entrada.split()

        for i in range(len(lista)):
            if int(lista[i]) > alvo:
                qnt_maiores += 1
                
        if qnt_maiores > len(lista)/2:
            print "sequencia %d: %s" % (contador, entrada)

    
