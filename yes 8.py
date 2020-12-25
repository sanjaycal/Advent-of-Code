lines = open('202013.txt').read().split('\n')
def p(zz):
  z, i = zz
  return int(z), int(i)
x = int(lines[0])
v = list(map(p, filter(lambda z : z[1] != 'x', enumerate(lines[1].split(',')))))
print(v)

for i, z in v:
  #print(z, i)
  i = -i
  while i < 0:
    i += z
  print('1 {} {}'.format(i, z))
