#coding: utf-8
lado1 = float(raw_input())
lado2 = float(raw_input())

casa = float(raw_input())

area = lado1 * lado2

qnt = int(area / casa)

print "%d casa(s) pode(m) ser construída(s) no terreno." % qnt
