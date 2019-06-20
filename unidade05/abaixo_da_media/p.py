lista = []
media = 0
valor = ''

while(valor != 'fim'):
    valor = raw_input()
    if valor != 'fim':
        lista.append(float(valor))
        media += float(valor)

media /= len(lista)

print "%.2f" % media

for i in range(len(lista)):
    if lista[i] < media:
        print "%d %d" % (i+1, lista[i])