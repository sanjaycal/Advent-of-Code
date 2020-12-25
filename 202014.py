f = open("202014.txt","r")
f = f.read()
f = f.split("\n")
g = []

for i in f:
    g.append(i)

import math

a = []

mask = ""

values = {}
value = 0
key = 0
for i in g:
    k = ""
    value = 0
    key = 0
    if i[:2] == "ma":
        mask = i[7:]
    if i[:2] == "me":
        key = list(bin(int(i[4:i.find("]")])))
        key = key[2:]
        value = (int(i[i.find("=")+2:]))
        while len(key)<len(mask):
            key.insert(0,"0")
        xs = 0
        for i in range(len(key)):
            if mask[i] == "X":
                key[i] = "X"
                xs+=1
            if mask[i] == "1":
                key[i] = "1"
        for i in range(2**xs):
            p = list(bin(i))[2:]
            while len(p) < xs:
                p.insert(0,"0")
            key2 = key.copy()
            for j in range(len(key)):
                if key[j] == "X":
                    key2[j] = p[0]
                    p.pop(0)
            n = ""
            for j in key2:
                n+=j
            values[int(n,2)] = value
print(values)
klj = 0
for i in values.values():
    klj+=i

print(klj)
