f = open("202024.txt","r")
f = f.read()
f = f.split("\n")
g = []

for i in f:
    a = []
    count = 0
    prev = ""
    for j in i:
        if j =="n" or j=="s":
            count+=1
            prev = j
        else:
            if count == 0:
                a.append(j)
                count = 0
            elif count == 1:
                a.append(prev+j)
                count = 0
    g.append(a)

print(g[0])


coords = []


for i in g:
    ns = 0.0
    ew = 0.0
    for j in i:
        if j=="e":
            ew+=1.0
        if j=="w":
            ew-=1.0
        if j=="ne":
            ew+=0.5
            ns+=0.5
        if j=="nw":
            ew-=0.5
            ns+=0.5
        if j=="se":
            ew+=0.5
            ns-=0.5
        if j=="sw":
            ew-=0.5
            ns-=0.5
    if not [ew,ns] in coords:
        coords.append([ew,ns])
    else:
        coords.remove([ew,ns])

print(len(coords))



for i in range(100):
    cn = coords
    
