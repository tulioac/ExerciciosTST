def distribui_alunos(turma1, turma2, capacidade):
    sala_1 = []
    sala_2 = []
    laboratorio = [sala_1, sala_2]
    indice = 0
    if len(turma1) > 0 or len(turma2) > 0:
        maior_turma = 0
        if len(turma1) >= len(turma2):
            maior_turma = len(turma1)
        else:
            maior_turma = len(turma2)
        for i in range(capacidade):
            if i < len(turma1):
                sala_1.append(turma1[i])
            if i < len(turma2):
                sala_1.append(turma2[i])
            if len(sala_1) == capacidade or i == maior_turma:
                indice = i + 1
                break

        if len(turma1) + len(turma2) > capacidade:
            for i in range(indice, maior_turma):
                if i < len(turma1):
                    sala_2.append(turma1[i])
                if i < len(turma2):
                    sala_2.append(turma2[i])
    return laboratorio


t1 = [1, 2, 3, 4, 5, 7]
t2 = [17, 23, 32]

x = distribui_alunos(t1, t2, 5)



print x