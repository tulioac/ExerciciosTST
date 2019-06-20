#coding: utf-8

s0 = float(raw_input("Posição inicial? "))
v0 = float(raw_input("Velocidade inicial? "))
tempo = float(raw_input("Tempo? "))
acerelacao = float(raw_input("Aceleração? "))

print

print "Dados da questão"
print '=' * 16

vf = v0 + acerelacao * tempo
sf = s0 + v0*tempo + acerelacao*tempo*tempo/2
vm = (v0 + vf)/2

print "   Posição inicial: %.2f m" % s0
print "Velocidade inicial: %.2f m/s" % v0
print "        Aceleração: %.2f m/s2" % acerelacao
print "             Tempo: %.2f s" % tempo
print "  Velocidade final: %.2f m/s" % vf
print "  Velocidade média: %.2f m/s" % vm
print "     Posição final: %.2f m" % sf
