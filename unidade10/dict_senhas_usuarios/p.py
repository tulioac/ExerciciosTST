def quantidade_usuarios(cadastro):
    quantidade = 0
    for senha in cadastro:
        if senha != 9999:
            quantidade += len(cadastro[senha])
    return quantidade
