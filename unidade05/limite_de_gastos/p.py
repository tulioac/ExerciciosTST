media_da_secretaria = float(raw_input())

while (True):
    media = 0
    saida = ''
    entrada = raw_input()
    if entrada != 'fim':
        informacoes = entrada.split()
        for i in informacoes:
            media += float(i)
        media /= len(informacoes)
        tamanho = len(informacoes)
        if media > media_da_secretaria:
            for i in range(len(informacoes) - 1):
                saida += '%.1f ' % float(informacoes[i])
            saida += '%.1f' % float(informacoes[tamanho - 1])
            print saida
        elif media <= media_da_secretaria/2:
            break
    else:
        break