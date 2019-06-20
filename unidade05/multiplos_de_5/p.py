limite = int(raw_input())
contador = 0
valor = 0

while(True):
    contador += 1
    valor = contador * 10
    if valor >= limite:
        break
    print valor

