#coding: utf-8
def num_creditos(bd_ufcg, matricula):
    creditos = 0
    for departamento in bd_ufcg:
        for info_disciplina in bd_ufcg[departamento]:
            for codigo_disciplina in bd_ufcg[departamento][info_disciplina]:
                if codigo_disciplina == matricula:
                    creditos += info_disciplina[1]
    return creditos

bd_ufcg = {"UASC": {("Programação I", 4): ["11624100", "11624400"], ("Programação II", 4): ["11624200"], ("Teoria dos Grafos", 2): ["11624200"]},
           "UAF": {("Física Clássica", 4): ["11624200"], ("Física Moderna", 4): ["11624300", "11624500", "11624600"]},
           "UAM": {("Cálculo I", 4): ["11624100", "11624300"], ("Álgebra Linear", 4): ["11624300"]}
           }

print num_creditos(bd_ufcg, "11624100")