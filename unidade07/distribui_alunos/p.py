def distribui_alunos(turma1, turma2, capacidade):
    sala1 = []
    sala2 = []
    lab = [sala1, sala2]

    ultima_turma = -1
    sala_atual = 0
    i = -1
    while i < capacidade * 2:
        if sala_atual == len(lab):
            break
        i += 1
        if len(lab[sala_atual]) < capacidade:
            if ultima_turma != 1 and i < len(turma1) and len(lab[sala_atual]) < capacidade:
                lab[sala_atual].append(turma1[i])
            
            if ultima_turma != 2 and i < len(turma2) and len(lab[sala_atual]) < capacidade:
                lab[sala_atual].append(turma2[i])
        else:
            if len(sala2) < capacidade:
                if sala1[len(sala1)-1] != turma2[i-1]:
                    sala2.append(turma2[i-1])
            i -= 1  
            sala_atual +=1
    return lab
