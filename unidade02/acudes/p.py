#coding: utf-8

capacidade = int(raw_input("capacidade? "))
percentual = float(raw_input("percentual hoje? "))
gasto = int(raw_input("gasto diário? "))

volume = capacidade * percentual / 100.0
dias = volume / gasto

print "volume: %.2f" % volume
print "dias restantes: %d" % dias