# coding: utf-8
# Aluno: Túlio Araújo Cunha
# Matrícula: 118210965
# UFCG - Programação 1 - 2018.2
# Questão: Dieta e2
# 10/09/2018

peso = float(raw_input())
horas = float(raw_input())
calorias = float(raw_input())

dias = (peso * 7700) / ((horas * 900) + (2000 - calorias))

print "Você precisará de %.2f dias de dieta" % dias

