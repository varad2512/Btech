#Robot Navigation using A*
import numpy as np 
from Queue import *
import collections
print "Enter the height:"
h = int(raw_input())
print "Enter the width:"
w = int(raw_input())
source = (0,0)
dest   = (1,1)
board = np.array([h,w], dtype = 'uint8')
h = collections.defaultdict()
g = collections.defaultdict()
f = collections.defaultdict()
def show():
	for x in range(2):
		for y in range(2):
			print board[x,y],
		print ""

def hammington(board):
	for x in range(2):
		for y in range(2):
			h[x,y],board[x,y] = (abs(x - destination[0]) + abs(y - destination[1]))
			g[x,y] = 9999
			f[x,y] = 9999
def neighbours(pos):
	return_list = []
	if pos[0] >= 0  and pos[0] < width and (pos[1]-1) >= 0 and (pos[1]-1) < width:
		return_list.append((pos[0],pos[1]-1))													
	if pos[0] >= 0  and pos[0] < width and (pos[1]+1) >= 0 and (pos[1]+1) < width:
		return_list.append((pos[0],pos[1]+1))
	if (pos[0]-1) >= 0  and (pos[0]-1) < width and (pos[1]) >= 0 and (pos[1]) < width:
		return_list.append((pos[0]-1,pos[1]))
	if (pos[0]+1) >= 0  and (pos[0]+1) < width and (pos[1]) >= 0 and (pos[1]) < width:
		return_list.append((pos[0]+1,pos[1]))
	return return_list

def A*(source,dest):
	open_list = PriorityQueue()
	closed_list = []
	
	camefrom = collections.defaultdict()
	g[source] = 0
	f[source] = h[source]
	open_list.put_nowait((f[source],source))

	while open_list:
		current = open_list.get_nowait()[1]
		closed_list.append(current)
		if current == dest:
			return reconstuctpath(current,camefrom)
		neighbours_list = neighbours(cuurent)
		for x in neighbours_list:
			if x in closed_list:
				continue
			tentative_distance = g[current] + 1
			if tentative_distance >= g[x]:
				continue
			g[x] = tentative_distance
			f[x] = g[x] + h[x]
			camefrom[x] = current

























hammington(board)
show()