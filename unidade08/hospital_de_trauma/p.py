# coding: utf-8
nomes_cores = ["vermelho", "laranja", "amarelo", "verde", "azul"]
prioridade_cores = {"vermelho": 4, "laranja": 3,
                    "amarelo": 2, "verde": 1,  "azul": 0}
cores = [0, 0, 0, 0, 0]


def resumo():
    print '-'*3
    for i in range(len(cores)):
        print "%s: %d" % (nomes_cores[i], cores[i])
    print '-'*3


def troca(lista, i, j):
    lista[i], lista[j] = lista[j], lista[i]


def cadastra(pessoas, nome, prioridade):
    pessoas.append([nome, prioridade])
    for i in range(len(pessoas)-1):
        for k in range(len(pessoas)-1):
            if prioridade_cores[pessoas[k][1]] < prioridade_cores[pessoas[k+1][1]]:
                troca(pessoas, k, k+1)


def exibe_ordem(lista):
    for i in range(len(lista)):
        print lista[i][0]


pacientes = []
while True:
    entrada = raw_input().split()
    if entrada[0] == 'fim':
        exibe_ordem(pacientes)
        resumo()
        break

    else:
        cadastra(pacientes, entrada[0], entrada[1])
        if entrada[1] == nomes_cores[0]:
            cores[0] += 1
        elif entrada[1] == nomes_cores[1]:
            cores[1] += 1
        elif entrada[1] == nomes_cores[2]:
            cores[2] += 1
        elif entrada[1] == nomes_cores[3]:
            cores[3] += 1
        elif entrada[1] == nomes_cores[4]:
            cores[4] += 1
