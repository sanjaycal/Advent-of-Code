f = open("202013.txt","r")
f = f.read()
f = f.split("\n")
g = []

for i in f:
    g.append(i)

import math

a = []

start = int(g[0])

busses = []

g = g[1].split(",")

for i in g:
    busses.append((i))

print(len(busses))

correct = []

print("use chinese remainder theorom, use https://comnuan.com/cmnn02/cmnn0200a/cmnn0200a.php")

for i in range(len(busses)):
    try:
        a = int(busses[i])
        b = -i
        while b<0:
            b = a+b
        print("1 " + str(b) + " " + str(a))
    except:
        g.append(i)
    
