#coding: utf-8

a = int(raw_input())
b = int(raw_input())

print "===== Operadores ====="

adicao = a + b
subtracao = a - b
multi = a * b
div = a / b
resto = a % b
exp = a ** b
neg_a = a * (-1)
igualdade = a == b
dif = a != b
maior1 = a > b
maior2 = b > a
menor_igual = a <= b

print "A = " + str(a)
print "B = " + str(b)

print "Adição = " + str(adicao)
print "Subtração = " + str(subtracao)
print "Multiplicação = " + str(multi)
print "Divisão = " + str(div)
print "Resto = " + str(resto)
print "Exponenciação = " + str(exp)
print "Negação de A = " + str(neg_a)
print "A é igual a B? %s" % str(igualdade)
print "A é diferente de B? %s" % str(dif)
print "A é maior que B? %s" % str(maior1)
print "B é maior que A? %s" % str(maior2)
print "A é menor ou igual a B? %s" % str(menor_igual)

