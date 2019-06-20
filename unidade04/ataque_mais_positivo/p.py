#coding: utf-8

def maior(lista):
    i_max = 0
    for i in range(len(lista)):
        if lista[i_max] < lista[i]:
            i_max = i
    maximo = lista[i_max]
    return maximo

n_times = int(raw_input())

times = []
gols = []

for i in range(n_times*2):
    entrada = raw_input()
    if i % 2 == 0:
        times.append(entrada)
    else:
        gols.append(int(entrada))

mais_gols = maior(gols)

print "Time(s) com melhor ataque (%d gol(s)):" % mais_gols
for i in range(len(times)):
    if gols[i] == mais_gols:
        print times[i]

media_gols = 0
for g in gols:
    media_gols += g

media_gols /= len(gols)*1.0

print 
print "Média de gols marcados: %.1f" % media_gols
