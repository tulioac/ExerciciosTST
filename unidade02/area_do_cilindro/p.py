#coding: utf-8 
import math

print 'Cálculo da Superfície de um Cilindro'
print 3*'-'

diametro = float(raw_input('Medida do diâmetro? '))
altura = float(raw_input('Medida da altura? '))

raio = diametro / 2
print 3*'-'

area = (math.pi * raio ** 2) * 2 + 2 * math.pi * raio * altura
print 'Área calculada: %.2f' % area