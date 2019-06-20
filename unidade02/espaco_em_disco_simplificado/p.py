#coding: utf-8

nome1 = raw_input()
espaco1 = float(raw_input())

nome2 = raw_input()
espaco2 = float(raw_input())

nome3 = raw_input()
espaco3 = float(raw_input())

print "SPLab - Espaço utilizado pelos usuários"
print '-'*45
print "Nr., Usuário, Espaço Utilizado"

print

tamanho1 = espaco1 / (1024 * 1024)
tamanho2 = espaco2 / (1024 * 1024)
tamanho3 = espaco3 / (1024 * 1024)

print "1, %s, %.2f MB" % (nome1, tamanho1)
print "2, %s, %.2f MB" % (nome2, tamanho2)
print "3, %s, %.2f MB" % (nome3, tamanho3)

print

print "Espaço total ocupado: %.2f MB" % (tamanho1 + tamanho2 + tamanho3)
print "Espaço médio ocupado: %.2f MB" % ((tamanho1 + tamanho2 + tamanho3)/3)



