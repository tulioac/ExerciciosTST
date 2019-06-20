quant = float(raw_input())

atacado = int(raw_input())
varejo = int(raw_input())

qnt_a = quant / atacado
qnt_v = float(quant % atacado / varejo)

print "Clientes no atacado = %dkg cada." % qnt_a
print "Clientes no varejo = %.2fkg cada." % qnt_v