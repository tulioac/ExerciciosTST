def ordena(lista):
    for j in range(len(lista)):
        for i in range(len(lista)-1):
            if lista[len(lista)-1 -i] < lista[len(lista)-2 -i]:
                lista[len(lista)-1 -i], lista[len(lista)-2 -i] = lista[len(lista)-2 -i], lista[len(lista)-1 -i]
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
    return lista

entrada = ''
agenda = []
while True:
    entrada = raw_input()
    if entrada == '####':
        break
    else:
        agenda.append(entrada)
        ordena(agenda)
        for i in agenda:
            if entrada == i:
                print "* %s" % i
            else:
                print i
        print 4*'-'
