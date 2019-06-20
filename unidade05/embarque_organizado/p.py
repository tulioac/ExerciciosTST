def ordena_lista(lista):
    valores = lista
    for i in range(len(valores)):
        for j in range (len(valores) - i - 1):
            if valores[j] < valores[j + 1]:
                valores[j], valores[j+1] = valores[j+1], valores[j] 
    return valores

entrada = raw_input()
posicoes = entrada.split()
lista = []
ordenada = []

for i in posicoes:
    if int(i) % 2 == 0:
        lista.append('0') # par
        ordenada.append('0') # par

    else:
        lista.append('1') # impar
        ordenada.append('1') # impar

ordenada = ordena_lista(ordenada)

if lista == ordenada:
    print "ok"
else:
    print "erro"
    