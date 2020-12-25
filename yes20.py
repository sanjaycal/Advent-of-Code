from typing import Dict, List, Mapping, Optional, Sequence, Set, Tuple, Union
import re
from collections import defaultdict
from math import ceil
f = open("202020.txt","r")
f = f.read()
input = f

tiles = input.split("\n\n")

orig_tiles = dict()
edges = defaultdict(lambda: [])
tilemap = dict()
n = 10

def flip(x: int):
	ret = 0
	for i in range(n):
		ret <<= 1
		if (x & 1) == 1:
			ret |= 1
		x >>= 1
	return ret

def edge_id(x: int):
	return min(x, flip(x))

for tile in tiles:
	header = tile.splitlines()[0]
	img = tile.splitlines()[1:]

	tile_id = int(header.split(" ")[1][:-1])
	orig_tiles[tile_id] = img

	l = 0
	r = 0

	for line in img:
		l <<= 1
		r <<= 1
		l |= 1 if line[0] == "#" else 0
		r |= 1 if line[-1] == "#" else 0

	t = 0
	b = 0

	for i in range(len(img[0])):
		t <<= 1
		b <<= 1
		t |= 1 if img[0][i] == "#" else 0
		b |= 1 if img[-1][i] == "#" else 0

	l = edge_id(l)
	r = edge_id(r)
	t = edge_id(t)
	b = edge_id(b)

	print(tile_id, bin(l), bin(r), bin(t), bin(b))

	tilemap[tile_id] = (t, l, b, r)
	edges[l] += [tile_id]
	edges[r] += [tile_id]
	edges[t] += [tile_id]
	edges[b] += [tile_id]

corners = []
init_edge = None

for tile_id, tile in tilemap.items():
	match_cnt = 0
	unused = -1
	for edge in tile:
		if len(edges[edge]) == 2:
			match_cnt += 1
		elif len(edges[edge]) == 1:
			unused = edge
	assert match_cnt >= 2
	if match_cnt == 2:
		corners.append(tile_id)
		if init_edge == None:
			init_edge = unused

# uncomment this for part 1
# ans = 1
# for corner in corners:
# 	ans *= corner
# print(ans)

s = 10
tw = 12
th = 12

def rot_cw(img: List[List[int]]):
	return [[img[s - j - 1][i] for j in range(s)] for i in range(s)]

def flip_h(img: List[List[int]]):
	return [[img[i][s - j - 1] for j in range(s)] for i in range(s)]

def top_bit(img: List[List[int]]):
	ret = 0
	for i in range(s):
		ret <<= 1
		ret |= 1 if img[0][i] == "#" else 0
	return ret

def find_top_bit(img: List[List[int]], x: int):
	for i in range(2):
		for j in range(4):
			if top_bit(img) == x:
				return img
			img = rot_cw(img)
		img = flip_h(img)
	assert False

grid: List[List[Optional[List[List[int]]]]] = [[None for j in range(tw)] for i in range(th)]
grid_ids: List[List[Optional[int]]] = [[None for j in range(tw)] for i in range(th)]

print(orig_tiles[corners[0]])
print(bin(init_edge))

def other(l, x):
	for y in l:
		if y != x:
			return y
	assert False

for i in range(th):
	for j in range(tw):
		print(i, j)
		if i == 0 and j == 0:
			grid[i][j] = find_top_bit(orig_tiles[corners[0]], init_edge)
			grid_ids[i][j] = corners[0]
		elif j == 0:
			match_edge = top_bit(flip_h(rot_cw(rot_cw(grid[i-1][j]))))
			grid_ids[i][j] = other(edges[edge_id(match_edge)], grid_ids[i-1][j])
			grid[i][j] = find_top_bit(orig_tiles[grid_ids[i][j]], match_edge)
		else:
			match_edge = top_bit(flip_h(rot_cw(rot_cw(rot_cw(grid[i][j-1])))))
			print(bin(match_edge))
			print(edges[edge_id(match_edge)])
			grid_ids[i][j] = other(edges[edge_id(match_edge)], grid_ids[i][j-1])
			grid[i][j] = rot_cw(rot_cw(rot_cw(find_top_bit(orig_tiles[grid_ids[i][j]], match_edge))))

fin_grid = []
for i in range(th):
	for ii in range(1, s-1):
		ln = ""
		for j in range(tw):
			for jj in range(1, s-1):
				ln += grid[i][j][ii][jj]
		fin_grid.append(ln)
		print(ln)

pattern = """                  #
#    ##    ##    ###
 #  #  #  #  #  #   """.splitlines()

def is_monster(v, di, dj):
	for i in range(len(pattern)):
		for j in range(len(pattern[i])):
			if pattern[i][j] == "#" and v[i+di][j+dj] != "#":
				return False
	return True

# some janky debug or something?  don't really remember
# fin_grid = [[grid[i//s][j//s][i%s][j%s] for j in range(s*tw)] for i in range(s*th)]
# for i in range(len(fin_grid)):
# 	if i % s == 0:
# 		print()
# 	for j in range(len(fin_grid)):
# 		if j % s == 0:
# 			print(" ", end = "")
# 		print(fin_grid[i][j], end="")
# 	print()

s = len(fin_grid)

print("".join(fin_grid))
print("".join(pattern))
print(pattern)

for i in range(2):
	for j in range(4):
		cnt = 0
		for di in range(0, s - len(pattern)):
			# print(di)
			for dj in range(0, s - len(pattern[0])):
				if is_monster(fin_grid, di, dj):
					cnt += 1
		if cnt > 0:
			print(str(fin_grid).count("#") - "".join(pattern).count("#") * cnt)
		fin_grid = rot_cw(fin_grid)
	fin_grid = flip_h(fin_grid)
