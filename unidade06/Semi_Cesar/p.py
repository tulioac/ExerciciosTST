from string import ascii_lowercase

def cesar(msg, d):
    nova_palavra = ''
    for i in range(len(msg)):
        achou = False
        for j in range(len(ascii_lowercase)):
            if msg[i] == ascii_lowercase[j]:
                nova_palavra += ascii_lowercase[(j+d) % 26]
                achou = True
        if achou == False:
            nova_palavra += msg[i]
    return nova_palavra