f = open("202010.txt","r")
f = f.read()
f = f.split("\n")
g = []

for i in f:
    g.append(i)

import math

a = []

for i in g:
    a.append(int(i))

a.sort()

one = 0
three  = 0
b = []


def is_valid(lst):
    for i in range(len(lst)):
        if lst[0] >=4:
            return False
        if lst[i]-lst[i-1] >=4:
            return False
    return True

b = []
o = 0





def h(n,p,q):
    o = 0
    q = q
    if n!=0:
        for i in range(len(a)):
            q[p-n] = i
            o += h(n-1,p,q)
    if n==0:
        b = a.copy()
        for i in range(p):
            exec("del(b[q[i]])")
        if is_valid(b):
            o+=1
        return o
    return o
    

ha = 0
print(h(5,5,[0,0,0,0,0]))

print(ha)
