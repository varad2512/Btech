#robot navigation using best first search 
import numpy as np
board = np.zeros([5,5])
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
hammington(board)
show()

