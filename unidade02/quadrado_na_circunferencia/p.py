#coding: utf-8
import math
lado = float(raw_input())

raio = math.sqrt(2) * lado / 2

areaC = math.pi * raio * raio
areaQ = lado * lado

dif = (areaC - areaQ) * 2

print "Área não comum: %.5f" % dif
