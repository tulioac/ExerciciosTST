entrada = raw_input()
info = entrada.split()

nome = info[0]
saldo_inicial = float(info[1])

while (True):
    entrada = raw_input()
    info = entrada.split()

    operacao = int(info[0])

    if operacao == 1:
        valor = float(info[1])
        saldo_inicial -= valor
    elif operacao == 2:
        valor = float(info[1])
        saldo_inicial += valor
    elif operacao == 3:
        print "Saldo de R$ %.2f na conta de %s" % (saldo_inicial, nome)
        break
