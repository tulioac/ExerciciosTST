#coding: utf-8

media = 0
valor = 0 
contador = 0
soma = 0

while (valor >= media):
    contador += 1
    valor = float(raw_input())
    if valor >= media:
        soma += valor
        media = soma / contador

print "Saldo total do FIS: R$%.2f." % soma
print "Média das contribuições: R$%.2f." % media
        