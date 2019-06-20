entrada = ''
coeficientes = []
while True:
    valor_da_funcao = 0
    entrada = raw_input()
    if entrada == 'fim':
        break
    else:
        valores = entrada.split()
        if len(valores) > 1:
            print "novo polinomio"
            coeficientes = []
            for i in range(1, len(valores)):
                coeficientes.append(int(valores[i]))
        else:
            for i in range(len(coeficientes)):
                valor_da_funcao += coeficientes[i]*int(valores[0])**i
            print valor_da_funcao