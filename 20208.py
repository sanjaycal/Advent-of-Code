f = open("20208.txt","r")
f = f.read()
f = f.split("\n")
g = []

for i in f:
    g.append(i)

import math

head = 0
accumulator = 0

print(g[0])


def run_command(a,q):
    global accumulator
    global head
    if q[a][:3] == "acc":
        accumulator += int(q[a][4:])
    if q[a][:3] == "jmp":
        head-=1
        head += int(q[a][4:])
    return q

def do(q):
    global p
    global head
    global accumulator
    p = []
    while True:
        try:
            if head not in p:
                p.append(head)
            else:
                #print(max(p))
                break
            run_command(head,q)
            head+=1
        except:
            print(accumulator)
p = []

m = g


for i in range(len(m)):
    head = 0
    accumulator = 0
    if m[i][:3] == "jmp":
        m[i] = m[i].replace("jmp","nop")
    else:
        m[i] = m[i].replace("nop","jmp")
    do(m)
    if m[i][:3] == "jmp":
        m[i] = m[i].replace("jmp","nop")
    else:
        m[i] = m[i].replace("nop","jmp")
    

