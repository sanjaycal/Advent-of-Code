f = open("20209.txt","r")
f = f.read()
f = f.split("\n")
g = []

for i in f:
    g.append(i)

import math

a = []

for i in g:
    a.append(int(i))



def in25(p):
    for i in a[p-25:p]:
        if a[p]-i in a[p-25:p]:
            return True
    return False

h = 0


def y(p):
    global h
    b = 0
    h = 0
    while b<85848519:
        b+=a[p+h]
        h+=1
    return b

for i in range(len(a)):
    if y(i) == 85848519:
        print(i)
        print(h)
        j = 0
        for k in range(h):
            j+=a[i+k]
        print(max(a[i:i+h])+min(a[i:i+h]))
