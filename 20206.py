f = open("20206.txt","r")
f = f.read()
f = f.split("\n\n")
g = []
for i in f:
    g.append(i)

import math

a = []

for i in g:
    a.append(i.split("\n"))


print(a)
jj=0
b = ""
d = "qwertyuiopasdfghjklzxcvbnm"
c =[]
for i in a:
    b = d
    for j in i:
        for k in b:
            if not k in j:
                b = b.replace(k,'')
    c.append(len(set(b)))


h = 0

for i in c:
    h+=i


print(h)
