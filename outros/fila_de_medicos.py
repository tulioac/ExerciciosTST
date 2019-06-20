def fila_de_medicos(fila, numero_de_medicos):
    medicos = []
    for i in range(numero_de_medicos):
        lista = []
        for j in range(i, len(fila), numero_de_medicos):
            lista.append(fila[j])
        medicos.append(lista)
    print medicos


lista = ["Antonio", "Carlos", "Bianca", "Pedro", "Jose", "Patricia", "Alfredo"]
fila_de_medicos(lista, 3)
    