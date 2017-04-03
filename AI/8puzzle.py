#hill climbing for 8 puzzle problem
import numpy as np
board = np.zeros([3,3],dtype = int)
print board
ideal = board
counter = 0
for i in range(3):
	for j in range(3):
 		ideal[i,j] = counter+1
 		counter = counter + 1
ideal[3,3] = 0
print ideal
def findDistance():
	manhattan_distance = 0
	for i in range(3):
		for j in range(3):
			row,col = np.where(a == board[i,j])
			manhattan_distance = manhattan_distance + (abs(i-row) + abs(j-col))
	return manhattan_distance			
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
def func1():
	while(1):
		d = dict()
		r,c = np.where(board == 0)
		nList = neighbours((r[0],c[0]))
		for x,y in nList:
			board[r,c],board[x,y] = board[x,y],0
			d[x,y] = findDistance()
			board[r,c],board[x,y] = 0,board[x,y]
		'''
		TODO:
		Find minimum of dictionary and mark the board
		if minimum is zero then break solution found
		if minimum is greater than current's score then break
		else continue 
		'''


