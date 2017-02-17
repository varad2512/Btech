#Robot Navigation using A*
import numpy as np 
from Queue import *
import collections
print "Enter the height:"
height = int(raw_input())
print "Enter the width:"
width = int(raw_input())
source = (0,0)
dest   = (2,0)
board = np.zeros([height,width], dtype = 'uint8')
board[source] = 2
board[dest] = 2
h = collections.defaultdict()
g = collections.defaultdict()
f = collections.defaultdict()
def show():
	for x in range(height):
		for y in range(width):
			print board[x,y],
		print ""

def hammington(board):
	for x in range(height):
		for y in range(width):
			h[(x,y)] = (abs(x - dest[0]) + abs(y - dest[1]))
			g[(x,y)] = 9999
			f[(x,y)] = 9999
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

def A(source,dest):
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
			return reconstructpath(current,camefrom)
		neighbours_list = neighbours(current)
		for x in neighbours_list:
			if x in closed_list:
				continue
			tentative_distance = g[current] + 1
			if tentative_distance >= g[x]:
				continue
			g[x] = tentative_distance
			f[x] = g[x] + h[x]
			open_list.put_nowait((f[x],x))
			camefrom[x] = current

def reconstructpath(current, camefrom):
	if current == source:
		return [current]
	else:
		path = [current]
		while(True):
			if current == source:
				return path
			else:	
				current = camefrom[current]
				path.append(current)

hammington(board)
show()
result = A(source,dest)
print result






















hammington(board)
show()