letras_vogais = ['a', 'A', 'e', 'E', 
          'i', 'I', 'o', 'O', 
          'u', 'U']

def conta_vogais(palavra):
    contador = 0
    for i in palavra:
        for j in letras_vogais:
            if i == j:
                contador += 1
    return contador
        

contador = 0

while(True):
    contador += 1
    entrada = raw_input()
    vogais = conta_vogais(entrada)
    consoantes = len(entrada) - vogais
    if consoantes > vogais:
        break

print contador