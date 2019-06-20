#coding: utf-8

s_inicial = float(raw_input())
velocidade = float(raw_input())
t = float(raw_input())

s_final = s_inicial + velocidade*t

print "Posição final do móvel"
print "S(%.1f) = %.1f m" % (t, s_final)