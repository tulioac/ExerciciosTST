#coding: utf-8

limite_superior = float(raw_input())
nivel_atual = float(raw_input())

while (True):
    if nivel_atual >= limite_superior:
        print "Açude passou a liberar água."
        print "Nível: %.2f" % nivel_atual
        break
    else:
        entrada = raw_input()
        informacoes = entrada.split()
        acao = informacoes[0]
        quantidade = float(informacoes[1])

        if acao == 'chuva' or acao == 'afluente':
            nivel_atual += quantidade

        elif acao == 'demanda' and (nivel_atual - quantidade) >= 0:
            nivel_atual -= quantidade

        

    