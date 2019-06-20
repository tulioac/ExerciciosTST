#coding: utf-8

total = 0

for i in range (7):
    valor = int(raw_input())
    total += valor

print "Total: %d" % total
media = total / 7.0

print "Média: %.2f" % media