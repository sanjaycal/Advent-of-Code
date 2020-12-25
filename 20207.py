f = open("20207.txt","r")
f = f.read()
f = f.split("\n")
g = []

for i in f:
    g.append(i)

import math

a = {}
b = ""
for i in g:
    b = i.split(" contain")
    a[b[0].replace(" ","").replace("s","").replace("0","").replace("9","").replace("8","").replace("7","").replace("6","").replace("5","").replace("4","").replace("3","").replace("2","").replace("1","").replace(".","")] = b[1].replace(" ","").replace("s","").replace("0","").replace("9","").replace("8","").replace("7","").replace("6","").replace("5","").replace("4","").replace("3","").replace("2","").replace("1","").replace(".","").split(",")

def lst(l1,l2):
    for i in l1:
        if i in l2:
                return True
    return False
h = []

def bn(s):
    h = []
    for i in a[s]:
        if i == "hinygoldbag":
            return True
        elif i in a.keys():
            if s not in h:
                h.append(s)
                bn(s)
            else:
                return False
        else:
            return False
    else:
        return False
        

b = 0

for i in a.keys():
    if bn(i):
        b+=1


print(b)
