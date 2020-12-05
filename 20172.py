f = open("20172.txt","r")
f = f.read()
f = f.split("\n")
g = []
for i in f:
    g.append(i)

h = []
for i in g:
    h.append(i.split("\t"))

lst = []
a = []
for i in h:
    for j in i:
        try:
            a.append(float(j))
        except:
            print("\n")
    lst.append(a)
    a = []

print(lst)

a = []
for i in lst:
    l = 0
    s = 0
    for j in i:
        for k in i:
            print(j/k)
            if (j/k)%1 == 0.0 and j!=k:
                print([j/k])
                l = j
                s = k
    a.append(l-s)

print(a)

sum = 0

for i in range(len(a)-1):
    sum+= a[i]
    print(sum)

print(sum)
            
        
    
