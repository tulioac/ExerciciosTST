def split(palavra):
    letras = ''
    lista = []
    for i in range(len(palavra)):
        if palavra[i] != ':':
            letras += palavra[i]
        else:
            lista.append(letras)
            letras = ''
    if letras != '' or letras != ':':
        lista.append(letras)
    return lista 


def conta_palavras(k, palavras):
    separadas = split(palavras)

    contador = 0
    for i in separadas:
        if len(i) >= k:
            contador += 1

    return contador