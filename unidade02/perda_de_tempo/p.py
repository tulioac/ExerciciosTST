#coding: utf-8
val1 = int(raw_input())
val2 = int(raw_input())
val3 = int(raw_input())
val4 = int(raw_input())
val5 = int(raw_input())

total = val1 + val2 + val3 + val4 + val5
media = total / 5.0
semana = 24 * 60 * 7.0
porcentagem = 100.0 * media * 7 / semana
episodio = total / 50

print "Você perdeu %d min na semana (média de %.1f min por dia)." % (total, media)
print "Isso significa %.2f%% da sua semana produtiva." % porcentagem
print "Daria para assistir %d episódio(s) de House." % episodio