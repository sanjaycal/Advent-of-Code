f = open("20182.txt","r")
f = f.read()
f = f.split("\n")
g = []
for i in f:
    g.append(i)

import math

for i in g:
    for j in g:
        a = 0
        for k in range(len("fonbsmjyqugrapsczckghtvdxl")):
            if i[k]!=j[k]:
                a+=1
        if a ==1:
            print([i,j])
            
        
    
