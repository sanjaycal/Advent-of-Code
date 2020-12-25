f = open("202015.txt","r")
f = f.read()
f = f.split(",")
g = []

for i in f:
    g.append(i)

import math

a = []

for i in g:
    a.append(int(i))



nums = a.copy()
d={a:[i] for i,a in enumerate(nums)}
print(d)
lst=nums[-1]
for i in range(len(nums),2020):
    if len(d[lst])==1:
        spoken=0
    else:
        spoken=d[lst][-1]-d[lst][-2]
    if spoken in d:
        d[spoken].append(i)
    else:
        d[spoken]=[i]
    lst=spoken

print(spoken)
            
    
