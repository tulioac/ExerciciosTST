contador = 0
while True:
    contador += 1
    vogais = 0
    consoantes = 0
    palavra = raw_input()
    for i in range(len(palavra)):
        if palavra[i] in 'aeiouAEIOU':
            vogais += 1
    consoantes = len(palavra) - vogais
    if consoantes > vogais:
        break

print contador
