# coding: utf-8
valores = []
while (True):
    valor = raw_input()
    if valor != '-':
        valores.append(float(valor))
    else:
        break

media_limite = float(raw_input())
soma = 0
media = 0
achou = False

for i in range(len(valores)):
    if achou == False:
        soma += valores[i]
        media = soma / (i+1)
        if media > media_limite:
            print "media = %.1f" % media
            print "num = %d" % (i + 1)
            achou = True

if achou == False:
    print "limite não alcançado"
