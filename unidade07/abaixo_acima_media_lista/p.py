def organiza_por_media(lista):  
    media = 0
    for i in lista:
        media += i
    if len(lista) > 0:
        media /= len(lista)

    for j in range(len(lista)):
        for i in range(0 ,len(lista) - 1, 1):
            while(lista[i] > media and not (lista[i+1] > media)):
                lista[i], lista[i+1] = lista[i+1], lista[i]           

    return lista


p1 = [1, 2, 4, 1, 3, 4, 56, 7, 7, 4, 3, 67]

x = organiza_por_media(p1)

print x

