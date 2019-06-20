parte1 = int(raw_input())
parte2 = int(raw_input())
parte3 = int(raw_input())

parte4 = parte3 / 100 + parte3 / 10 % 10 + parte3 % 10

print "%03d.%03d.%03d-%02d" % (parte1, parte2, parte3, parte4)
