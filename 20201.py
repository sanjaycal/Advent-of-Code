f = open("20201.txt","r")
f = f.read()
f = f.split("\n")
g = []
for i in f:
    g.append(int(i))

import math

for i in g:
   for j in g:
       for k in g:
           if (i+j+k)==2020:
               print(i*j*k)
