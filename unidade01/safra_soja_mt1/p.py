soja = int(raw_input())

atacado = int(raw_input())
varejo = int(raw_input())

qnt_atacado = float(soja / atacado)
qnt_varejo = float((soja - qnt_atacado*atacado) / varejo)

print "Clientes no atacado = %dkg cada." % qnt_atacado
print "Clientes no varejo = %.2fkg cada." % qnt_varejo