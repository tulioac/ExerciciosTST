precos = []
tamanho = []
conforto = []
hotel = []

while (True):
    entrada = raw_input()

    if entrada != '---':
        lista = entrada.split(',')
        precos.append(float(lista[0]))
        tamanho.append(int(lista[1]))
        conforto.append(int(lista[2]))
        hotel.append(lista[3])
    else:
        break

menor_preco = precos[0]
maior_tamanho = 0
maior_conforto = 0

for i in range(len(precos)):
    if precos[i] < menor_preco:
        menor_preco = precos[i]
        melhor = i

print "%s" % hotel[melhor]

for i in range(len(tamanho)):
    if tamanho[i] > maior_tamanho:
        maior_tamanho = tamanho[i]
        melhor = i

print "%s" % hotel[melhor]

for i in range(len(conforto)):
    if conforto[i] > maior_conforto:
        maior_conforto = conforto[i]
        melhor = i

print "%s" % hotel[melhor]
