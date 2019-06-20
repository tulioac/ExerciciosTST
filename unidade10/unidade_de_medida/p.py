while True:
    entrada = raw_input().split()
    entrada[0] = float(entrada[0])
    entrada[2] = float(entrada[2])


    if entrada[0] == 0 and entrada[2] == 0:
        break
    else:
        if entrada[1] == 'km':
            entrada[0] *= 1000.0
        elif entrada[1] == 'hm':
            entrada[0] *= 100.0
        elif entrada[1] == 'dam':
            entrada[0] *= 10.0
        elif entrada[1] == 'dm':
            entrada[0] /= 10.0
        elif entrada[1] == 'cm':
            entrada[0] /= 100.0
        elif entrada[1] == 'mm':
            entrada[0] /= 1000.0

        if entrada[3] == 'km':
            entrada[2] *= 1000.0
        elif entrada[3] == 'hm':
            entrada[2] *= 100.0
        elif entrada[3] == 'dam':
            entrada[2] *= 10.0
        elif entrada[3] == 'dm':
            entrada[2] /= 10.0
        elif entrada[3] == 'cm':
            entrada[2] /= 100.0
        elif entrada[3] == 'mm':
            entrada[2] /= 1000.0

        print "%.2f m" % (entrada[0] + entrada[2])