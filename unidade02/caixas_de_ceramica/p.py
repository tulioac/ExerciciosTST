#coding: utf-8

capacidade = float(raw_input("Capacidade de revestimento? "))

print

print "== Dados do vão a revestir =="
comprimento = float(raw_input("Comprimento? "))
largura = float(raw_input("Largura? "))
altura = float(raw_input("Altura? "))

print

print "== Resultados =="

area = comprimento * largura + largura * altura * 2 + comprimento * altura * 2
caixas = area / capacidade

print "Área total a revestir: %.1f m2" % area
print "Número de caixas: %d" % caixas