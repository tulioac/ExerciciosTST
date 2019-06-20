media = float(raw_input())
media_lista = media / 2 + 1
string = ''
media_maior = media_lista
lista = ''

while (string != 'fim' and media_lista > (media/2)):
    string = raw_input()
    media_lista = 0

    if string != 'fim':
        lista = string.split()
        for i in range(len(lista)):
            media_lista += float(lista[i])
        
        media_lista /= len(lista)

        if media_lista > media:
            print string
