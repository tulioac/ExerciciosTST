peso = float(raw_input())
altura = float(raw_input())

imc = peso / altura ** 2
peso_necessario = (24.9 - imc) * altura ** 2



print "IMC atual = %.2f" % imc
print "Peso a ser ganho/perdido = %.2f" % peso_necessario