#robot navigation using best first search 
import numpy as np
from Queue import *

height = 2
width = 2

closedlist = []
priority = PriorityQueue()

board = np.zeros([2,2], dtype = 'uint8')
print "Please enter the source position :"
#start = tuple(int(x) for x in raw_input().split(","))
start = (0,0)
print "Please enter the destination position :"
#destination = tuple(int(x) for x in raw_input().split(","))
destination = (1,1)
def show():
	for x in range(2):
		for y in range(2):
			print board[x,y],
		print ""

def hammington(board):
	for x in range(2):
		for y in range(2):
			board[x,y] = (abs(x - destination[0]) + abs(y - destination[1]))

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

def shortest():
	#TODO if a not in closed list add to open list
	if priority.empty():
		return 0
	else:
		a = priority.get_nowait()
		if (a[1],a[2]) == destination:
			print "Solution found"
			return 1
		else:
			closedlist.append((a[1],a[2]))
			neighbours_list = neighbours((a[1],a[2]))
			for x in neighbours_list:
				if x not in closedlist:
					priority.put_nowait((board[x],x[0],x[1]))
			return shortest()

hammington(board)
show()
priority.put_nowait((board[start],start[0],start[1]))
if (shortest()):
	print "Route found"
else:
	print "No route"


print closedlist