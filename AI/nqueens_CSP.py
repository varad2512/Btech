#nqueens CSP (4 queen's initially)
import numpy as np 
board = np.zeros([4,4], dtype = int)
def isSafe(row,col):
	for i in range(col):
		if(board[row,i]):
			return False
	for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
		if(board[i,j]):
			return False
	for i,j in zip(range(row,4),range(col,-1,-1)):
		if(board[i,j]):
			return False
	return True
def simulate(column):
	if column >= 4:
		return True
	for x in range(4):
		if(isSafe(x,column)):
			board[x,column] = 1
			if(simulate(column + 1)):
				return True
			board[x,column] = 0
	return False
if(simulate(0)):
	for x in range(4):
		print 
		for y in range(4):
			print board[x,y],
else:
	print "No Solution"
