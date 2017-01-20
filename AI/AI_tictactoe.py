#AI technique for tic tac toe game
import numpy as np 

def findopenpositions(l):
	#Will find all the open positions on the board and will return the list of tuples
	return_list=[]
	for x in range(3):
		for y in range(3):
			if l[x,y] == 2:
				return_list.append((x,y))
	return return_list

def func1(player, l):
	if player == 'X':
		list_of_open_positions = findopenpositions(l)
