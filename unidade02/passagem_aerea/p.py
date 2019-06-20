#coding: utf-8
milhas = float(raw_input())
aliquota = float(raw_input())

passagem = milhas * aliquota + 51.0

print "Valor da passagem: R$ %.2f" % passagem

print

a_vista = passagem * 0.75
seis_parcelas = passagem * 0.95

print "Pagamento:"
print "1. À vista. R$ %.2f" % a_vista
print "2. Em 6 parcelas. Total: R$ %.2f" % seis_parcelas
print "   6 x R$ %.2f" % (seis_parcelas/6)
print "3. Em 10 parcelas. Total: R$ %.2f" % passagem
print "   10 x R$ %.2f" % (passagem/10)
