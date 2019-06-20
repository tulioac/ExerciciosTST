#coding: utf-8

def split(palavra):
    var = ''
    lista = []
    for i in range(len(palavra)):
        if palavra[i] != ",":
            var += palavra[i]
        else:
            lista.append(var)
            var = ''
    if var != '':
        lista.append(var)
    return lista

def conta_votos(votacoes, id_votacao):
    qnt_sim = 0
    qnt_nao = 0
    voto = ''
    for i in range(len(votacoes)):
        informacoes = split(votacoes[i])
        voto = informacoes[1] 
        id_voto = informacoes[2]
        if informacoes[1] == 'sim' and int(id_voto) == int(id_votacao):
            qnt_sim += 1
        elif informacoes[1] == 'nao' and int(id_voto) == int(id_votacao):
            qnt_nao += 1

    resposta = [qnt_sim, qnt_nao]
    return resposta    

votacao = []
votacao.append('greve geral,sim,543,joao,servidor')
votacao.append('greve geral,nao,543,marina,servidor')
votacao.append('indicativo de greve,sim,5,joao,professor')
votacao.append('paralisação,nao,543,julio,professor')
votacao.append('paralisação,sim,543,carlos,professor')
votacao.append('paralisação,sim,543,juliana,professor')
votacao.append('lei 1329,sim,99,joao,servidor')

print conta_votos(votacao, 543)