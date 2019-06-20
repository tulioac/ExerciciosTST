#coding: utf-8

def time_campeao(dados):
    maior = 0
    for info in dados.values():
        if info[0] > maior:
            maior = info[0]
    campeoes = []
    for times in dados:
        if dados[times][0] == maior:
            campeoes.append(times)
    return campeoes


dados = {"Botafogo": [59, 43, 39],
    "São Paulo": [52, 44, 36],
    "Palmeiras": [80, 62, 32],
    "Santos": [72, 59, 35]}

print time_campeao(dados)