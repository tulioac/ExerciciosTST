def meu_slice(palavra, tam):
    nova_palavra = ''
    for i in range(tam):
        nova_palavra += palavra[i]
    return nova_palavra

def meu_in(palavra, dic):
    for i in dic:
        if i == palavra:
            return True
    return False

def agrupa_por_periodo(alunos):
    dic = {}
    for i in alunos:
        periodo = meu_slice(i, 3)
    
        if meu_in(periodo, dic):
            dic[periodo] += 1
        else:
            dic[periodo] = 1

    return dic

turma = [
    '0511114', '0521137', '0611001',
    '0611003', '0611004', '0621006',
    '0811007', '0811009', '0811502',
    '0811604', '0811605',
]

print agrupa_por_periodo(turma)