# coding: utf-8
# Calculando o consumo de energia em Joules

potencia = int(raw_input())
tempo = int(raw_input())
tempo /= 60.0


print str(potencia * tempo/1000) , "kWh"