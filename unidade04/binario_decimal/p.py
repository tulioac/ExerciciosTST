binario = raw_input()

msg = ''
saida = []
decimal = 0
for i in range(len(binario)-1, -1, -1):
    potencia = 2**(len(binario)-i-1)
    valor = int(binario[i]) * potencia
    msg = "%s * %d = %d" % (binario[i], potencia, valor)
    saida.append(msg)
    if valor != 0:
        decimal += valor

for i in range(len(saida)-1, -1, -1):
    print saida[i]

print "%s(2) = %d(10)" % (binario, decimal)
    