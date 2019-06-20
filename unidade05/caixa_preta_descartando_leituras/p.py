#coding: utf-8
string = ''
valido = True
qnt_peso = 0
qnt_combustivel = 0
qnt_altitude = 0

while (valido == True):
    string = raw_input()
    informacoes = string.split()
    peso = int(informacoes[0])
    combustivel = int(informacoes[1])
    altitude = int(informacoes[2])

    if peso >= 0:
        qnt_peso += 1

        if combustivel >= 0:
            qnt_combustivel += 1

            if altitude >= 0:
                qnt_altitude += 1

            else:
                valido = False
                print "dado inconsistente. altitude negativa."  
        else:
            valido = False
            print "dado inconsistente. combustível negativo."
    else: 
        valido = False
        print "dado inconsistente. peso negativo."

print "peso: %d" % qnt_peso
print "combustível: %d" % qnt_combustivel
print "altitude: %d" % qnt_altitude