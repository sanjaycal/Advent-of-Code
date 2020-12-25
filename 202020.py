f = open("202020.txt","r")
f = f.read()
f = f.split("\n\n")
g = []

for i in f:
    a = []
    j = i.split("\n")
    g.append(j)

import math


class image:
    def __init__(self, pct, iid):
        self.pct = pct
        self.spct = pct
        self.iid = iid
        self.siid = iid
    def __repr__(self):
        a = ""
        for i in self.pct:
            b = ""
            for j in i:
                b+=j
            a+=b+"\n"
        return str(self.iid) + ": \n" + a
    def flip_v(self):
        a = self.pct
        a.reverse()
        self.pct = a
    def flip_h(self):
        a = []
        for i in self.pct:
            a.append(i[::-1])
        self.pct = a
    def is_ad(self, oimage):
        for i in range(4):
            if self.is_adj(oimage, i):
                return i
        return -1
    def is_adj(self, oimage, side):
        if side%2 == 0:
            return self.is_adj_v(oimage, side)
        else:
            return self.is_adj_h(oimage, side)
    def is_adj_v(self, oimage, side):
        if side == 0:
            if oimage.pct[-1] == self.pct[0]:
                return True
            else:
                return False
        if side == 2:
            if oimage.pct[0] == self.pct[-1]:
                return True
            else:
                return False
    def is_adj_h(self, oimage, side):
        if side == 1:
            count = 0
            needed = len(self.pct[0])
            for i in range(needed):
                if oimage.pct[i][0] == self.pct[i][-1]:
                    count+=1
            if count == needed:
                return True
            return False
        if side == 3:
            count = 0
            needed = len(self.pct[0])
            for i in range(needed):
                if oimage.pct[i][-1] == self.pct[i][0]:
                    count+=1
            if count == needed:
                return True
            return False
    def reset(self):
        self.iid = self.siid
        self.pct = self.spct
    def rotate(self):
        self.pct = list(zip(*self.pct[::-1]))
        
        
        
            


images = []

for i in g:
    images.append(image(i[1:],int(i[0][5:-1])))


side_len = math.sqrt(len(images))

a = image(['..........','..........','..........','..........','..........','..........','..........','..........','..........','..........'],0)

fimage = []

for i in range(int(side_len)):
    b = []
    for j in range(int(side_len)):
        b.append(a)
    fimage.append(b)

cimage = []
for i in images:
    count = 0
    for j in images:
        if i!=j:
            if i.iid == 2311:
                print("2-3-1-1")
            for jfdashna in range(0,4):
                if i.iid == 2311:
                    print(count)
                j.rotate()
                j.flip_v()
                if i.is_ad(j)!=-1:
                    count+=1
                j.flip_h()
                if i.is_ad(j)!=-1:
                    count+=1
                j.flip_v()
                if i.is_ad(j)!=-1:
                    count+=1
                j.flip_h()
                if i.is_ad(j)!=-1:
                    count+=1
    print(count)
    if count == 4:
        cimage.append(i)

for i in cimage:
    print(i.iid)




