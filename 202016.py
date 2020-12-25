f = open("202016.txt","r")
f = f.read()
f = f.split("\n")
g = []

for i in f[25:]:
    g.append(i)


valid = {}

for i in f[:20]:
    valid[i[:i.find(":")]] = [[int(i[i.find(":")+2:i.find("-",i.find(":")+2)]),
                               int(i[i.find("-",i.find(":")+2)+1:i.find("o",i.find(":")+2)-1])],
                              [int(i[i.find("o",i.find(":")+2)+3:i.find("-",i.find("o",i.find(":")+2)+3)]),
                               int(i[i.find("-",i.find("or",i.find(":")+2)+2)+1:])]]



import math

j = []

for i in g:
    j.append(i.split(","))

tickets = []

for i in j:
    a = []
    for k in i:
        a.append(int(k))
    tickets.append(a)
def find(lst):
    count = 0
    pqwe = []
    required = len(valid.keys())
    for i in lst:
        count = required
        for j in valid.keys():
            if (i>=valid[j][0][0] and i<=valid[j][0][1]) or (i>=valid[j][1][0] and i<=valid[j][1][1]):
                count -= 1
        if count >= required:
            pqwe.append(i)
    if len(pqwe) == 0:
        return False
    else:
        return True



               
            
v = []
for i in tickets:
    if not find(i):
        v.append(i)

tickets = v
print((list(valid.keys())[0:6]))
vf = (list(valid.keys()))
print(vf)
for j in vf:
    for tt in range(0,20):
        count = len(tickets)
        for k in range(len(tickets)):
            i = tickets[k][tt]
            if ((i>=valid[j][0][0] and i<=valid[j][0][1]) or (i>=valid[j][1][0] and i<=valid[j][1][1])):
                count -= 1
        if count ==0:
            print(tt, end = ",")
    print("\n")



    
