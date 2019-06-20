#coding:    utf-8
qnt_tweets = int(raw_input())

paginas = qnt_tweets / 400

perdidos = qnt_tweets - paginas * 400
perc_perdidos = perdidos * 100.0 / qnt_tweets

print "Serão necessárias %d página(s) para visualizar os tweets." % paginas
print "%.1f%% dos tweets serão perdidos." % perc_perdidos