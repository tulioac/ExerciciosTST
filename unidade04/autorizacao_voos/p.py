tempo_limite = int(raw_input())
avioes = int(raw_input())

tempo = []
tempo_gasto = 0
decolados = 0
for i in range(avioes):
    valor = int(raw_input())

    tempo.append(valor)

    if tempo_gasto + valor <= tempo_limite:
        decolados += 0
        tempo_gasto += valor

print "%d voo(s) autorizados." % decolados