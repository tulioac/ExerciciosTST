def meu_in(lista, elemento):
    for i in lista:
        if i == elemento:
            return True
    return False

def disciplinas(alocacao, professor):
    aulas = []
    creditos = 0

    for disciplina in alocacao:
        for professores in alocacao[disciplina]:
            if professores == professor:
                if not meu_in(aulas, disciplina[0]):
                    aulas.append(disciplina[0])
                creditos += disciplina[1]

    return [aulas, creditos]   



alocacao = {("P1", 4): ['Jorge', 'Dalton','Wilkerson'],
    ("LP1", 4): ['Jorge', 'Dalton', 'Eliane', 'Wilkerson'],
    ("EVOL", 2): ['Dalton'],
    ("IC", 4): ['Eliane', 'Joseana'],
    ("P2", 4): ['Livia', 'Raquel', 'Nazareno'],
    ("GRAFOS", 2): ['Patricia', 'Patricia']}


print disciplinas(alocacao, "Dalton")
print
print disciplinas(alocacao, "Patricia")