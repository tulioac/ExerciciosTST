def complemento1(numero):
    s_binario = bin(numero)
    binario = ''
    if numero >= 0:
        for i in range(2, len(s_binario)):
            binario += s_binario[i]
    else:
        for i in range(2, len(s_binario)):
            if s_binario[i] == '1':
                binario += '0'
            else:
                binario += '1'
    print "%08d" % int(binario)

def excesso_127(numero):
    numero += 127
    s_binario = bin(numero)
    binario = ''
    for i in range(2, len(s_binario)):
        binario += s_binario[i]
    print "%08d" % int(binario)

while True:
    entrada = raw_input()
    
    if entrada[0] == '*':
        break
    
    else:
        entrada = entrada.split()
        if entrada[0] == 'C1':
            complemento1(int(entrada[1]))
        elif entrada[0] == 'E127':
            excesso_127(int(entrada[1]))