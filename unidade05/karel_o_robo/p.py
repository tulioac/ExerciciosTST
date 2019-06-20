#coding: utf-8

# C - acima
# B - abaixo
# E - esquerda
# D - direita

def meu_absoluto(numero):
    if numero < 0:
        return numero*(-1)
    else:
        return numero

x = 0
y = 0
fim = False
abs_x = 0
abs_y = 0

while (fim == False):
    entrada = raw_input()
    direcao = entrada[0]
    valor = int(entrada[2])

    if valor != 0:
        if direcao == 'C':
            y += + valor

        elif direcao == 'B':
            y -= valor
        
        elif direcao == 'D':
            x += valor

        elif direcao == 'E':
            x -= valor

        abs_x = meu_absoluto(x)
        abs_y = meu_absoluto(y)

        if abs_y == abs_x * 2 and x !=0 and y !=0:
            print "Parabéns, conquista do portal (%d, %d)" % (x, y)
            fim = True

    else:
        fim = True
        print "Fim de jogo"