f = open("20183.txt","r")
f = f.read()
f = f.split("\n")
g = []
for i in f:
    g.append(i)

import math

h= []
j = []
for i in g:
    j = i.split(",")


print(len(g))
