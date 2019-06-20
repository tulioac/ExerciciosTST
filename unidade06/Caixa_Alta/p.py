def caixa_alta(frase):
    frase += ' '
    nova_frase = ''
    for i in range(len(frase)-1):
        if frase[i-1] == ' ' and frase[i+1] == ' ':
            nova_frase += frase[i].lower()
        elif frase[i-1] == ' ' and frase[i+1] != ' ':
            nova_frase += frase[i].upper()
        else:
            nova_frase += frase[i]
        
    return nova_frase
