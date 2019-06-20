#coding: utf-8
import math
lado = float(raw_input())

raio = math.sqrt(2) * lado / 2

perimetro = 2 * math.pi * raio

area = math.pi * raio * raio

print "Perímetro: %.5f" % perimetro
print "Área: %.5f" % area
