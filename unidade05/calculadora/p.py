#coding: utf-8

string = ''
valido = True

while (valido):
    string = raw_input()
    informacoes = string.split()

    operacao = int(informacoes[0])
    if operacao != 5:
        digito_1 = int(informacoes[1])
        digito_2 = int(informacoes[2])

        if operacao == 1:
            print "%d" % (digito_1 + digito_2)
        
        elif operacao == 2:  
            print "%d" % (digito_1 - digito_2)

        elif operacao == 3:
            print "%d" % (digito_1 * digito_2)

        elif operacao == 4 and digito_2 != 0:
            print "%d" % (digito_1 / digito_2)

        elif digito_2 == 0:
            print "Erro: Divisão por 0"
            valido = False
    else:
        valido = False

