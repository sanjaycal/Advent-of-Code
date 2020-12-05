f = open("20203.txt","r")
f = f.read()
f = f.split("\n")
g = []
for i in f:
    g.append(i)

import math

nt = 0
def is_tree(x,y):
    if g[y][x%len(g[0])] == "#":
        return True
    else:
        return False

def num_trees(cx,cy):
    x = 0
    y = 0
    nt = 0
    for i in g:
        try:
            if is_tree(x,y):
                nt+=1
            x+=cx
            y+=cy
        except:
            print("a")
    return nt



nt1 = num_trees(1,1)
nt2 = num_trees(3,1)
nt3 = num_trees(5,1)
nt4 = num_trees(7,1)
nt5 = num_trees(1,2)



print(nt1)
print(nt2)
print(nt3)
print(nt4)
print(nt5)
print(nt1*nt2*nt3*nt4*nt5)
