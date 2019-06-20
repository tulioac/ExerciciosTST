def meuIn(elemento, lista):
    for i in lista:
        if i == elemento:
            return True
    return False

def meuSplit(string):
    lista = []
    caracteres = ''
    for i in string:
        if i != '/':
            caracteres += i
        else:
            lista.append(caracteres)
            caracteres = ''
    if caracteres != '':
        lista.append(caracteres)
    return lista

def eh_roteiro(iata, voos, roteiro):
    roteiro = meuSplit(roteiro)
    for i in range(len(roteiro)):
        roteiro[i] = iata[roteiro[i]]

    viagem_possivel = True
    for i in range(len(roteiro)-1):
        if not meuIn(roteiro[i+1], voos[roteiro[i]]):
            viagem_possivel = False
    
    return viagem_possivel





iata = {"Campina Grande": "CPV",
       "Recife": "REC",
       "Salvador": "SSA",
       "Brasilia": "BSB",
       "Sao Paulo": "GRU",
       "Rio de Janeiro": "GIG"}


voos = {"CPV": ["REC", "SSA"],
       "REC": ["CPV", "BSB", "GRU", "GIG"],
       "SSA": ["REC", "GRU", "GIG"],
       "BSB": ["CPV", "GIG", "GRU"],
       "GRU": ["GIG", "BSB"],
       "GIG": ["GRU", "REC"]}

print eh_roteiro(iata, voos, "Recife/Rio de Janeiro/Salvador/Recife")