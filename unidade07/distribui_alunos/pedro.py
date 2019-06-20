def distribui_alunos(turma1, turma2, capacidade):
    lab01 = []
    lab02 = []

    lista_labs = [lab01, lab02]

    turmas = [turma1, turma2]

    cont_turma = 0
    cont_lab = 0

    indice = 0

    for i in range(2):
        while True:
            operacao = False
            if len(lista_labs[cont_lab]) < capacidade and cont_turma == 0:
                lista_labs[cont_lab].append(turmas[cont_turma][indice])
                cont_turma = 1
                operacao = True
            if len(lista_labs[cont_lab]) < capacidade and cont_turma == 1:
                lista_labs[cont_lab].append(turmas[cont_turma][indice])
                cont_turma = 0
                operacao = True

            indice += 1
            if not operacao:
                break

    return lista_labs


t1 = [10, 38, 87, 22, 25]
t2 = [43, 21, 96, 33, 85, 17, 94]

x = distribui_alunos(t1, t2, 6)
print x
