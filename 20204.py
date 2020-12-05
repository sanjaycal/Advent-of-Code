f = open("20204.txt","r")
f = f.read()
f = f.split("\n\n")
g = []
for i in f:
    g.append(i)

import math


class passport():
    def __init__(self,byr,iyr,eyr,hgt,hcl,ecl,pid):
        a = byr[0]
        a = iyr[0]
        a = eyr[0]
        a = hgt[0]
        a = hcl[0]
        a = ecl[0]
        a = pid[0]
        self.byr = byr
        self.iyr =iyr
        self.eyr =eyr
        self.hgt =hgt
        self.hcl = hcl
        self.ecl =ecl
        self.pid = pid


passports = []
byr,iyr,eyr,hgt,hcl,ecl,pid = 0,0,0,0,0,0,0
jj = 0

#g = g[:5]

for i in range(len(g)):
    g[i] = (g[i].replace("\n"," "))+" "

print(len(g))
for i in g:
    for j in range(len(i)):
        if i[j] == ":":
            exec(i[j-3:j] + "=" +"'"+ i[j+1:(i.find(" ",j))]+"'")
    try:
        passports.append(passport(byr,iyr,eyr,hgt,hcl,ecl,pid))
    except:
        jj=0
    byr,iyr,eyr,hgt,hcl,ecl,pid = 0,0,0,0,0,0,0

print(len(passports))

g_p = []
a=0
eyr = 0
for i in passports:
    try:
        if int(i.byr)>=1920 and int(i.byr)<=2002:
            if int(i.iyr)>=2010 and int(i.iyr)<=2020:
                if int(i.eyr)>=2020 and int(i.eyr)<=2030:
                    if len(i.pid)==9 and int(i.pid) == int(i.pid):
                        g_p.append(i)
    except:
        jj = 0
print(len(g_p))

h_p = []
a =0 
for i in g_p:
    #try:
    if i.hgt[-2:] == "cm":
        if int(i.hgt[:-2])<=193 and int(i.hgt[:-2])>=150:
            h_p.append(i)
    if i.hgt[-2:] == "in":
        if int(i.hgt[:-2])<=76 and int(i.hgt[:-2])>=59:
            h_p.append(i)
    #except:
        #a+=1
        #jj=0

print("a:"+str(a))
        
                
print(len(h_p))

hc_p = []
a = 0
b = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
for i in h_p:
    try:
        if i.hcl[0] == "#":
            for j in i.hcl[1:]:
                for k in b:
                    if j==k:
                        a+=1
        if a==6:
            hc_p.append(i)
    except:
        jj = 0
    a = 0

print(len(hc_p))


e_p = []

b= ["amb","blu","brn","gry","grn","hzl","oth"]

for i in hc_p:
    try:
        for j in b:
            if i.ecl == j:
                e_p.append(i)
    except:
        jj = 0

print(len(e_p))
    
