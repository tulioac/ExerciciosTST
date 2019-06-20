# coding: utf-8
# Cálculo de Campos de Futebol

area = [float(raw_input()), float(raw_input()), float(raw_input())]

campos = [area[0] / 4000, area[1] / 4000, area[2] / 4000]
media = (campos[0] + campos[1] + campos[2])/3

print "%.2f\n%.2f\n%.2f" % (campos[0], campos[1], campos[2])
print "%.2f" % media