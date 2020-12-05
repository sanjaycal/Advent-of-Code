f = open("20202.txt","r")
f = f.read()
f = f.split("\n")
g = []
for i in f:
    g.append(i)

import math

list_of_characters = "qwertyuiopasdfghjklzxcvbnm"


def find_first_letter(string):
    for i in string:
        for j in list_of_characters:
            if i==j:
                return i

def num_of_char(string,char):
    a = 0
    for i in string:
        if i == char:
            a+=1
    return a



g.remove("")

low = []
for i in g:
    if i[1] == "-":
        low.append(int(i[0]))
    else:
        low.append(int(i[0:2]))
high = []
for i in g:
    if i[1] == "-":
        if i[4] == " ":
            high.append(int(i[2:4]))
        else:
            high.append(int(i[2]))
    else:
        if i[4] == " ":
            high.append(int(i[3]))
        else:
            high.append(int(i[3:5]))

char_to_find = []

for i in g:
    char_to_find.append(find_first_letter(i))

password = []
for i in g:
    password.append(i.split(" ")[2])


total = 0


for i in range(len(low)):
    if (password[i][low[i]-1]==char_to_find[i] or password[i][high[i]-1]==char_to_find[i]) and not(password[i][low[i]-1]==char_to_find[i] and password[i][high[i]-1]==char_to_find[i]):
        total+=1

print(total)
    
