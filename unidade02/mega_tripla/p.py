num1 = int(raw_input())
num2 = int(raw_input())
num3 = int(raw_input())

dig1 = num1 % 11
dig2 = num2 % 11
dig3 = num3 % 11

print "%02d-%02d-%02d" % (dig1, dig2, dig3)