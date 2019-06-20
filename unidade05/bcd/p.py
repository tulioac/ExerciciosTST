#coding: utf-8
string = ''

while (string != 'fim'):
    string = raw_input()

    if string != 'fim':
        if len(string) == 8:
            parte_1 = string[:4]
            parte_2 = string[4:]
            digito_1 = int(parte_1, 2)
            digito_2 = int(parte_2, 2)
            if digito_1 >= 10 or digito_2 >= 10:
                print "BCD inválido."
            else:
                print "%d%d" % (digito_1, digito_2)
        else:
            print "Tente novamente."
