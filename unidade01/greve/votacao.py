# coding: utf-8
# Eleição na ADUF

abstencao = float(raw_input())
a_favor = float(raw_input())
contra = float(raw_input())

total = abstencao + a_favor + contra
per_abstencao = abstencao / total * 100.0
per_favor = a_favor / total * 100.0
per_contra = contra / total * 100.0

print "Resultado da Votação"
print
print "%d abstenções (%.2f%%)" % (abstencao, per_abstencao) 
print "%d a favor (%.2f%%)" % (a_favor, per_favor) 
print "%d contra (%.2f%%)" % (contra, per_contra) 
