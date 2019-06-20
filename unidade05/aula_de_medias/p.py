# coding: utf-8
soma = 0
valores = []
menores = []
maiores = []

while(soma < 100):
    valor = float(raw_input())
    valores.append(valor)
    soma += valor

quant = len(valores)

media = soma / quant

print "Quantidade de números lidos: %d" % quant
print "Soma dos números lidos: %.2f" % soma
print "Média = %.2f" % media

for i in range(len(valores)):
    if valores[i] < media:
        menores.append(i)
    else:
        maiores.append(i)

if len(menores) > 0:
    print
    print "Abaixo da média"
    for i in range(len(menores)):
        print "%.2f (%do)" % (valores[menores[i]], menores[i]+1)
if len(maiores) > 0:

    print
    print "Acima da média"
    for i in range(len(maiores)):
        print "%.2f (%do)" % (valores[maiores[i]], maiores[i]+1)
