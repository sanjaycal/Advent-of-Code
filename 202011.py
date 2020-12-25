f = open("202011.txt","r")
f = f.read()
f = f.split("\n")
g = []

for i in f:
    g.append(i)

import math

a = []

for i in g:
    a.append(list(i))

g = a


tt = g
print(g)
def get_state(x,y):
    if x>=0 and y>=0:
        try:
            return tt[y][x]
        except:
            return "."
    else:
        return "."


def next_turn(grid):
    r, c = len(grid), len(grid[0])
    newGrid = [[grid[i][j] for j in range(c)] for i in range(r)]
    changeHappen = False
    for i in range(r):
        for j in range(c):
            if grid[i][j] == '.':
                continue

            adj = 0
            adj += i and j and grid[i-1][j-1] == '#'
            adj += i and grid[i-1][j] == '#'
            adj += i and j + 1 < c and grid[i-1][j+1] == '#'
            adj += j and grid[i][j-1] == '#'
            adj += j + 1 < c and grid[i][j+1] == '#'
            adj += i + 1 < r and j and grid[i+1][j-1] == '#'
            adj += i + 1 < r and grid[i+1][j] == '#'
            adj += i + 1 < r and j + 1 < c and grid[i+1][j+1] == '#'
            
            if grid[i][j] == 'L' and adj == 0:
                changeHappen = True
                newGrid[i][j] = '#'
            elif grid[i][j] == '#' and adj >= 4:
                changeHappen = True
                newGrid[i][j] = 'L'
    return newGrid, changeHappen


h = g
tt = g

while True:
    h = g
    for i in range(len(g)):
        for j in range(len(g[0])):
            next_turn(i,j)
    tt = g.copy()
    k  = 0
    for i in g:
        k+= i.count("#")
    print(k)
