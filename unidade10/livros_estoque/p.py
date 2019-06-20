def ausentes(estoque):
    zerados = 0

    for livros in estoque:
        if estoque[livros] == 0:
            zerados += 1
    return zerados
    