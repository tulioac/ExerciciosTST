#coding: utf-8

def MA(valores):
    soma = 0
    for i in range(len(valores)):
        soma += float(valores[i])
    media = soma / len(valores)
    print "Média Aritmética: %.4f" % media

def MG(valores):
    produto = 1.0
    for i in range(len(valores)):
        produto *= float(valores[i])
    media = produto ** (1.0/len(valores))
    print "Média Geométrica: %.4f" % media

def MH(valores):
    soma_dos_inversos = 0
    for i in range(len(valores)):
        soma_dos_inversos += 1/(float(valores[i]))
    media = len(valores)/soma_dos_inversos
    print "Média Harmônica: %.4f" % media

entrada = ''
while True:
    entrada = raw_input()

    if entrada == 'Q':
        break
    else:
        entrada = entrada.split()
        valores = raw_input().split()
        for i in entrada:
            if i == 'MG':
                MG(valores)
            elif i == 'MA':
                MA(valores)
            elif i == 'MH':
                MH(valores)
        print '-'*4