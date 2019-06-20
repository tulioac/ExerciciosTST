def criaSenhaFraca(palavra):
    senha = '((' + palavra + '))'
    print senha

def criaSenhaForte(palavra):
    senha = ''
    for i in range(len(palavra)):
        if palavra[i].lower() == 'o':
            senha += '0'
        elif palavra[i].lower() == 'i' or palavra[i].lower() == 'l':
            senha += '1'
        elif palavra[i].lower() == 'e':
            senha += '3'
        elif palavra[i].lower() == 'a':
            senha += '4'
        elif palavra[i].lower() == 'b':
            senha += '6'
        elif palavra[i].lower() == 't':
            senha += '7'
        else:
            senha += palavra[i]
    senha = '((' + senha + '))'
    print senha

while True:
    entrada = raw_input().split()
    if entrada[0][0] == '*':
        break
    elif entrada[1] == 'fraco':
        criaSenhaFraca(entrada[0])
    elif entrada[1] == 'forte':
        criaSenhaForte(entrada[0])