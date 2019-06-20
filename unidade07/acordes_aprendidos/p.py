def acordes(musica_1, musica_2):
    lista = []
    for i in musica_1:
        lista.append(i)


    for j in musica_2:
        igual = False
        for k in musica_1:
            if k == j:
                igual = True
        if igual == False:
            lista.append(j)

    return lista
