f = open("202021.txt","r")
f = f.read()
f = f.split("\n\n")
g = []

for i in f:
    a = []
    j = i.split("\n")
    g.append(j)

import math


def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list

allergens = []

for i in g:
    for j in i:
        allergens.append(j[j.find("(contains ")+10:-1].split(", "))

alle = allergens.copy()
allergens = []
for i in alle:
    for j in i:
        allergens.append(j)

allergens = Remove(allergens)

ingredients = []

for i in g:
    for j in i:
        ingredients.append(j[:j.find("(contains ")-1].split(" "))


ain = []

for i in ingredients:
    for j in i:
        ain.append(j)

ain = Remove(ain)


possibilities = {}



for i in allergens:
    possibilities[i] = ain
    

for i in range(len(alle)):
    for j in alle[i]:
        possibilities[j] = list(set(possibilities[j]).intersection(set(ingredients[i])))



a = possibilities.values()
bb = possibilities.keys()
sbb = sorted(list(bb))
print(sbb)
al = []

for i in a:
    for j in i:
        al.append(j)

al = Remove(al)




count = 0
a = []
for i in ingredients:
    for j in i:
        a.append(j)


for i in a:
    if not i in al:
        count+=1

print(count)
