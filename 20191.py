f = open("20191.txt","r")
f = f.read()
f = f.split("\n")
g = []
for i in f:
    g.append(int(i))

import math

def fuel_a(n):
    if math.floor(n/3)-2>0:
        return math.floor(n/3)-2
    else:
        return 0

def fuel(n):
    y = 0
    j = fuel_a(n)
    for i in range(100):
        y+= j
        j = fuel_a(j)
    return y

h = []
for i in g:
    h.append(fuel(i))

l = 0

for i in h:
    l+=i

f = open("20191 - Answer.txt","a")
f.write(str(l))
f.close()
print(l)
