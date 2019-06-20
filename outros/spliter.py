def spliter(string):
    var = ""
    lista_aux = []
    lista = []
    for i in range(len(string)):
        if string[i].isdigit() == True:
            var += string[i]
            print var
        else:
            lista_aux.append(var)
            var = ""
    lista.append(var)
    for k in lista_aux:
        
        if k != "":
            lista.append(k)
    return lista



print spliter(raw_input())