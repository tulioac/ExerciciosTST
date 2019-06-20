v_inicial = float(raw_input("Valor atual? "))
v_final = float(raw_input("Novo valor? "))

reajuste = (v_final * 100 / v_inicial) - 100

print "Reajuste de %.1f%%" % reajuste 