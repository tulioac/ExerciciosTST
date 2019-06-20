#coding: utf-8

print "== Estágio 1 =="
peso1 = float(raw_input("Peso? "))
nota1 = float(raw_input("Nota? "))

print "== Estágio 2 =="
peso2 = float(raw_input("Peso? "))
nota2 = float(raw_input("Nota? "))

print "== Estágio 3 =="
peso3 = float(raw_input("Peso? "))
nota3 = float(raw_input("Nota? "))

media_parcial = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3)

media_cinco = (5.0 - media_parcial * 0.6) / 0.4
media_sete = (7.0 - media_parcial * 0.6) / 0.4

print "== Resultados =="
print "Média parcial: %.1f" % media_parcial
print "Nota na final, pra média 5.0 = %.1f" % media_cinco
print "Nota na final, pra média 7.0 = %.1f" % media_sete
