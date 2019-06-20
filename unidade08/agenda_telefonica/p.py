def exibeDados(lista, indice):
    print "Nome: %s" % lista[i][0]
    print "Fone: %d" % lista[i][1]
    print 10*'-'

def ordena(lista):
    for j in range(len(lista)):
        for i in range(len(lista)-1):
            if lista[len(lista)-1-i][0] < lista[len(lista)-2-i][0]:
                lista[len(lista)-1-i], lista[len(lista)-2-i] = lista[len(lista)-2-i], lista[len(lista)-1-i]
            if lista[i][0] > lista[i+1][0]:
                lista[i], lista[i+1] = lista[i+1], lista[i]

operacao = ''
agenda = []
while True:
    operacao = raw_input()
    if operacao == 'finalizar':
        break
    elif operacao == 'inserir':
        quantidade = int(raw_input())
        for i in range(quantidade):
            nome = raw_input()
            telefone = int(raw_input())
            agenda.append([nome, telefone])
    elif operacao == 'buscar':
        procurado = raw_input()
        achou = False
        for i in range(len(agenda)):
            if agenda[i][0] == procurado:
                exibeDados(agenda, i)
                achou = True
        if achou == False:
            print "Nome inexistente"
            print 10*'-'
    elif operacao == 'imprimir':
        ordena(agenda)
        for i in range(len(agenda)):
            exibeDados(agenda, i)
        