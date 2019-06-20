def meuIn(elemento, lista):
    for i in lista:
        if i == elemento:
            return True
    return False

entrada = raw_input().lower()

letras = {}

for i in entrada:
    if meuIn(i, letras) and i != ' ':
        letras[i] += 1
    elif i != ' ':
        letras[i] = 1

resposta = ['', 0]
for caractere, quantidade in letras.iteritems():
    if quantidade > resposta[1]:
        resposta[1] = quantidade
        resposta[0] = caractere

print "%s %d" % (resposta[0], resposta[1]) 


