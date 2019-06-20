#coding: utf-8
import math

x1 = int(raw_input())
y1 = int(raw_input())
x2 = int(raw_input())
y2 = int(raw_input())
x3 = int(raw_input())
y3 = int(raw_input())

ponto1 = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
ponto2 = math.sqrt((x1 - x3)**2 + (y1 - y3)**2)
ponto3 = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)

perimetro = ponto1 + ponto2 + ponto3

print "O perímetro é de %.2f" % perimetro