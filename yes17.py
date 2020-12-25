f = open("202017.txt", "r")
lines = f.read().split("\n")
lines = [l for l in lines if len(l) > 0]

cubes = set()
for y in range(len(lines)):
  for x in range(len(lines[0])):
    if lines[y][x] == "#":
      cubes.add((x, y, 0, 0))

def neighbors(p):
  x, y, z, w = p
  for nx in range(x - 1, x + 2):
    for ny in range(y - 1, y + 2):
      for nz in range(z - 1, z + 2):
        for nw in range(w - 1, w + 2):
          if nx == x and ny == y and nz == z and nw == w:
            continue
          yield (nx, ny, nz, nw)

for i in range(6):
  nextcubes = set()
  xs = [t[0] for t in cubes]
  ys = [t[1] for t in cubes]
  zs = [t[2] for t in cubes]
  ws = [t[3] for t in cubes]
  for x in range(min(xs) - 1, max(xs) + 2):
    for y in range(min(ys) - 1, max(ys) + 2):
      for z in range(min(zs) - 1, max(zs) + 2):
        for w in range(min(ws) - 1, max(ws) + 2):
          active_n = 0
          for n in neighbors((x, y, z, w)):
            if n in cubes:
              active_n += 1
          if (x, y, z, w) in cubes:
            if active_n == 2 or active_n == 3:
              nextcubes.add((x, y, z, w))
          else:
            if active_n == 3:
              nextcubes.add((x, y, z, w))
  cubes = nextcubes

print(len(cubes))

