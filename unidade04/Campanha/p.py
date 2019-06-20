vitorias = 0
derrotas = 0
empates = 0

saldo = 0
gols_pro = 0
gols_contra = 0

pontos = 0
pontos_casa = 0
pontos_fora = 0

for i in range(10):
    entrada = raw_input()
    if entrada[len(entrada)-2] == 'c':
        gols_pro += int(entrada[0])
        gols_contra += int(entrada[2])
        if int(entrada[0]) > int(entrada[2]):
            vitorias += 1
            pontos_casa += 3
        elif int(entrada[0]) < int(entrada[2]):
            derrotas += 1
        else:
            empates += 1
            pontos_casa += 1
    else:
        gols_pro += int(entrada[2])
        gols_contra += int(entrada[0])
        if int(entrada[2]) > int(entrada[0]):
            vitorias += 1
            pontos_fora += 3
        elif int(entrada[2]) < int(entrada[0]):
            derrotas += 1
        else:
            empates += 1
            pontos_fora += 1

saldo = gols_pro - gols_contra
pontos = pontos_casa + pontos_fora

print "%dv, %de, %dd" % (vitorias, empates, derrotas)
print "pontos: %d" % pontos
print "saldo: %d (%d pro, %d contra)" % (saldo, gols_pro, gols_contra)
print "pontos em casa: %d" % pontos_casa
print "pontos fora: %d" % pontos_fora