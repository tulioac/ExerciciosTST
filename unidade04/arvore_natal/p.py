h = int(raw_input())

espacos = h
os = -1

for i in range(h):
    espacos -= 1
    os +=  2
    print ' '*espacos + 'o'*os
print ' '*(h-1) + 'o'