#coding: utf-8
import math

tipo = raw_input()

if tipo == 'círculo' or tipo == 'quadrado':
    raio_lado = float(raw_input())
    area = raio_lado * raio_lado    
    if tipo == 'círculo':
        area *= math.pi
        print "Área do círculo: %.2f (cm2)" % area
    else:
        print "Área do quadrado: %.2f (cm2)" % area


else:
    base = float(raw_input())
    altura = float(raw_input())
    area = base * altura
    if tipo == 'retângulo':    
        print "Área do retângulo: %.2f (cm2)" % area
    else:
        area /= 2
        print "Área do triângulo: %.2f (cm2)" % area




