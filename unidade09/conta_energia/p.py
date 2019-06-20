def calcula_conta(tabela):
    conta = 0
    
    for linha in range(1, len(tabela)):
        conta += int(tabela[linha][1]) * int(tabela[linha][2]) * int(tabela[linha][3]) * 0.28 / 1000

    msg = "R$ %.2f" % conta
    return msg

tabela = [["Equipamento", "Quantidade", "Tempo de Uso (horas)", "Potencia (Watts)"],
          ["AR-CONDICIONADO",    1,              240,               2000],
          ["COMPUTADOR",         2,              150,               180],
          ["TV",                 3,              150,               110]]

print calcula_conta(tabela)
