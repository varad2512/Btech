#robot navigation using best first search 
import numpy as np
openlist = []
closedlist = []
board = np.zeros([5,5], dtype = 'uint8')
print "Please enter the source position :"
start = tuple(int(x) for x in raw_input().split(","))
print "Please enter the destination position :"
destination = tuple(int(x) for x in raw_input().split(","))

def show():
	for x in range(5):
		for y in range(5):
			print board[x,y],
		print ""

def hammington(board):
	for x in range(5):
		for y in range(5):
			board[x,y] = (abs(x - destination[0]) + abs(y - destination[1]))

def neighbours(pos):
	return_list = []
	if (board[pos[0],pos[1]-1]):
		return_list.append(board[pos[0],pos[1]-1])
	if (board[pos[0],pos[1]+1]):
		return_list.append(board[pos[0],pos[1]+1])
	if (board[pos[0]-1,pos[1]]):
		return_list.append(board[pos[0]-1,pos[1]])
	if (board[pos[0]+1,pos[1]]):
		return_list.append(board[pos[0]+1,pos[1]])
	return return_list

def shortest(a):
	#TODO if a not in closed list add to open list
	if a == destination:
		return


hammington(board)
show()
shortest(start)


