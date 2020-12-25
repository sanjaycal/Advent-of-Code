f = open("202012.txt","r")
f = f.read()
f = f.split("\n")
g = []

for i in f:
    g.append(i)

import math

c = []

for i in g:
    c.append([i[0],i[1:]])


ns = 1
ew = 10
angle = 0
nsn = 0
sew = 0

for a in c:
    if a[0] == "N":
        ns+=int(a[1])
    elif a[0] == "S":
        ns -= int(a[1])
    elif a[0] == "E":
        ew +=int(a[1])
    elif a[0] == "W":
        ew -= int(a[1])
    elif a[0] == "F":
        for i in range(int(a[1])):
            nsn += ns
            sew += ew
    elif a[0] == "L":
        for i in range(int(int(a[1])/90)):
            e = ew
            ew = -ns
            ns = e
    elif a[0] == "R":
        for i in range(int(int(a[1])/90)):
            e = ew
            ew = ns
            ns = -e
print(nsn)
print(sew)
print(abs(nsn) + abs(sew))
print(angle)
