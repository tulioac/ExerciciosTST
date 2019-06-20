def cria_login(nome):
    dividido = nome.split()
    login = dividido[0].lower()
    for i in range(1, len(dividido)):
        if dividido[i] == 'da' or dividido[i] == 'de' or dividido[i] == 'do':
            continue
        else:
            login += dividido[i][0].lower()
    print "%s: %s" % (nome, login)



while True:
    entrada = raw_input()

    if entrada == 'fim':
        break
    else:
        cria_login(entrada)