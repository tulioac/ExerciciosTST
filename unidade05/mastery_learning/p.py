# coding: utf-8

print "Mastery Learning"
print "Cálculo da nota na unidade"
print

nota_1 = float(raw_input("Nota? "))
nota_2 = float(raw_input("Nota? "))
contador = 0
penalizacao = 0.0

media = (nota_1 + nota_2) / 2.0

while(True):
    contador += 1
    if contador > 1:
        penalizacao = (contador - 1) * 0.5


    if media < 6:
        print "Média: %.1f (cursando)" % media
        print "Penalização: %.1f" % penalizacao

        print

        nota = float(raw_input("Nota? "))

        if nota > nota_1 and nota_1 < nota_2:
            nota_1 = nota
        elif nota > nota_2 and nota_2 < nota_1:
            nota_2 = nota

        media = (nota_1 + nota_2) / 2.0
        
    else:
        print "Média: %.1f (aprovado)" % media
        print "Penalização: %.1f" % penalizacao

        break

print
print 3*'='
print "Notas válidas: %.1f e %.1f" % (nota_1, nota_2)
print "Média parcial na unidade: %.1f" % media
print "Penalizações: %.1f" % penalizacao
media -= penalizacao
print "Média final na unidade: %.1f" % media








