def meuIn(lista, elemento):
    for i in lista:
        if i == elemento:
            return True
    return False

def numero_disciplinas(grade, horarios, pagas):
    provaveis = []
    horarios_provaveis = []
    for disciplina, requisitos in grade.iteritems():
        if len(requisitos) == 0:
            if not meuIn(pagas, disciplina) and not meuIn(horarios_provaveis, horarios[disciplina]):
                provaveis.append(disciplina)
                horarios_provaveis.append(horarios[disciplina])
        else:
            valido = True
            for cada_requisitos in requisitos:
                if not meuIn(pagas, cada_requisitos):
                    valido = False
            if valido and not meuIn(horarios_provaveis, horarios[disciplina]):
                provaveis.append(disciplina)
                horarios_provaveis.append(horarios[disciplina])
    return len(provaveis)


grade = {"p1": [], "lp1": [], "ic": [],"calc1": [], "p2": ["ic", "p1", "lp1"],
"lp2": ["ic", "p1", "lp1"], "grafos": ["ic", "p1", "lp1"], "calc2"  : ["calc1"], 
"edados": ["ic", "p1", "lp1", "p2", "lp2", "grafos"],
"leda": ["ic", "p1", "lp1", "p2", "lp2", "grafos"]}

horarios= {"p1": "s082", "lp1": "x082", "ic": "i142", "calc1": "q082", "p2": "t162",
"lp2": "s082", "grafos": "q082", "calc2": "x162", "edados": "x162", "leda": "t102"}

numero_disciplinas(grade, horarios, [])
numero_disciplinas(grade, horarios, ["ic", "p1", "lp1"]) # p2, lp2, grafos