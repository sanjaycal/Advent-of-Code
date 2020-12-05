f = open("20205.txt","r")
f = f.read()
f = f.split("\n")
g = []
for i in f:
    g.append(i)

import math


def get_row(s):
    a = s[:7]
    c = [0,127]
    for i in a:
        if i=="F":
            c[1] = c[1]-(c[1]+1-c[0])/2
        if i=="B":
            c[0] = c[0]+(c[1]+1-c[0])/2
    return int(c[1])


def get_col(s):
    a = s[7:]
    c = [0,7]
    for i in a:
        if i=="L":
            c[1] = c[1]-(c[1]+1-c[0])/2
        if i=="R":
            c[0] = c[0]+(c[1]+1-c[0])/2
    return int(c[1])



def get_id(s):
    return get_row(s) * 8 + get_col(s)

a = []
for i in g:
    a.append(get_id(i))


a.sort()
b = []
for i in range(1024):
    if not i in a:
        b.append(i)

print(b)
