f = open("202025.txt","r")
f = f.read()
f = f.split("\n")
g = []

for i in f:
    g.append(int(i))


a = g[0]
b = g[1]

def root(a):
    for i in range(100000000):
        if pow(7, i, 20201227) == a:
            return i

print(pow(a, root(b), 20201227))
print(pow(b, root(a), 20201227))
