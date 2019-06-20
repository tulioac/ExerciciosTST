#coding: utf-8
import math

velocidade_de_vazao = float(raw_input())
diametro = float(raw_input())
tempo = int(raw_input())

seccao = (math.pi * diametro**2) / 4
vazao = velocidade_de_vazao * seccao * 1000                                       #em segundos
quantidade_de_agua = tempo * vazao
print "Quantidade de água =", quantidade_de_agua, "litros."
