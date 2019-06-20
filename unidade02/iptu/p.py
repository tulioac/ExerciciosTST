#coding: utf-8
area = float(raw_input("Área construída? "))
aliquota = float(raw_input("Alíquota? "))

iptu = area * aliquota + 35.0
print "IPTU: R$ %.2f" % iptu

cota_unica = iptu * 0.75
seis_parcelas = iptu * 0.95

print

print "Pagamento:"
print "1. Quota única. R$ %.2f" % cota_unica
print "2. Em 6 parcelas. Total: R$ %.2f" % seis_parcelas
print "   6 x R$ %.2f" % (seis_parcelas / 6)
print "3. Em 10 parcelas. Total: R$ %.2f" % iptu
print "   10 x R$ %.2f" % (iptu / 10)