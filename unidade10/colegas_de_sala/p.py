def colegas_de_sala(salasprofs, professor):
    sala_do_prof = salasprofs[professor]
    colegas = []

    for prof, sala in salasprofs.iteritems():
        if prof != professor and sala == sala_do_prof:
            colegas.append(prof)
    
    return colegas

    