#coding: utf-8
print "Análise da Turma"
print 3*'='

aprovados = int(raw_input('Número de aprovados? '))
reprovados = int(raw_input('Número de reprovados? '))

print 3*'-'

total = aprovados + reprovados

perc_aprovados = aprovados * 100.0 / total
perc_reprovados = reprovados * 100.0 / total

print 'Total de alunos na turma: ' + str(total)
print "Aprovados: " + str(aprovados) + " = %.1f%%" % perc_aprovados
print "Reprovados: " + str(reprovados) + " = %.1f%%" % perc_reprovados


