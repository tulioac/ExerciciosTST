def troca(lista, i, j):
    lista[i], lista[j] = lista[j], lista[i]

def exibe(lista):
    msg = ''
    for i in range(len(lista) - 1):
        msg += lista[i] + ' '
    msg += lista[len(lista)-1]
    print msg

def GE(lista):
    for i in range(len(lista) - 2, -1, -1):
        troca(lista, i, i-1)
    exibe(lista)

def GD(lista):
    for i in range(len(lista)-1):
        troca(lista, i, i+1)
    exibe(lista)

def I(lista):
    for i in range(0, len(lista)-1, 2):
        troca(lista, i, i+1)
    exibe(lista)

cartas = raw_input().split()

while True:
    entrada = raw_input()
    if entrada == 'fim':
        break
    else:
        if entrada.upper() == 'GE':
            GE(cartas)
        elif entrada.upper() == "GD":
            GD(cartas)
        elif entrada.upper() == "I":
            I(cartas)    