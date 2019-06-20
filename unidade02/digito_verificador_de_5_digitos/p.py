numero = raw_input()

valor = 0

valor += int(numero[0])
valor += int(numero[1])
valor += int(numero[2])
valor += int(numero[3])
valor += int(numero[4])

digito = valor % 11

print "%s-%02d" % (numero, digito)