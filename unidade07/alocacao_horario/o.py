def achar_na_lista(lista, procurado):
    for i in lista:
        if i == procurado:
            return True
    return False

def get_choque_horario(disciplinas):
    choques = []
    for i in range(len(disciplinas)):
        for j in range(i+1, len(disciplinas)):
            if disciplinas[i][len(disciplinas[i])-1] == disciplinas[j][len(disciplinas[j])-1]:
                if not achar_na_lista(choques, disciplinas[i]):
                    choques.append(disciplinas[i])  
                if not achar_na_lista(choques, disciplinas[j]):
                    choques.append(disciplinas[j])

    return choques