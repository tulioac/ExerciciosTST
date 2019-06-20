#coding: utf-8
n = int(raw_input())
lista = []
reprovados = 0
media_aprovados = 0
media_reprovados = 0

for i in range(n):
    valor = float(raw_input())
    lista.append(valor)
    
for i in range(n):
    if lista[i] < 7:
        reprovados += 1
        media_reprovados += lista[i]
    else:
        media_aprovados += lista[i]


aprovados = n - reprovados
media_aprovados /= aprovados
media_reprovados /= reprovados

print "Reprovados: %d " % reprovados
if reprovados > 0:
    print "Média: %.1f" % media_aprovados
print
print "Aprovados: %d" % aprovados
if aprovados > 0:
    print "Média: %.1f" % media_aprovados



