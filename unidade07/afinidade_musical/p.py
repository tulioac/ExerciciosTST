def tem_afinidade(l1, l2):
    contador = 0

    for i in l1:
        for j in l2:
            if j == i:
                contador += 1

    if contador > 2:
        return True
    else:
        return False