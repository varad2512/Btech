#AI technique for tic tac toe game
from Queue import *
import numpy as np 

l = np.ones([3,3]) 

def init(l):
  '''
  for rows in range(3):
    for cols in range(3):
      l[rows,cols] = 2      #blank initialization of tic tac toe board
  '''

  l[0,0] = 5
  l[0,1] = 5
  l[0,2] = 3
  l[1,0] = 2
  l[1,1] = 3
  l[1,2] = 2
  l[2,0] = 5
  l[2,1] = 3
  l[2,2] = 2

def board(l):
  for x in range(3):
    for y in range(3):
      print int(l[x,y]),
    print ""

def xwins(l):
	sum_of_col   = list(np.product(l,axis = 0))
	sum_of_row   = list(np.product(l,axis = 1))
	sum_of_diag1 = list(np.diagonal(l))
	sum_of_diag2 = list(np.diagonal(np.fliplr(l)))
	if 18 in sum_of_col:
	  	return 1    
	elif 18 in sum_of_row:
		return 1    
	elif np.prod(sum_of_diag1) == 18:
		return 1
	elif np.prod(sum_of_diag2) == 18:
		return 1
	else:
		return 0

def owins(l):
	sum_of_col   = list(np.product(l,axis = 0))
	sum_of_row   = list(np.product(l,axis = 1))
	sum_of_diag1 = list(np.diagonal(l))
	sum_of_diag2 = list(np.diagonal(np.fliplr(l)))
	if 50 in sum_of_col:
	  	return 1    
	elif 50 in sum_of_row:
		return 1    
	elif np.prod(sum_of_diag1) == 50:
		return 1
	elif np.prod(sum_of_diag2) == 50:
		return 1
	else:
		return 0

def endmoves(l):
	for x in range(3):
		for y in range(3):
			if l[x,y] == 2:
				flag = 1
	if flag == 1:
		return 0
	else:
		return 1

def optimalmove(l):
  #Center or corners are returned	
  if l[1][1] == 2:
    return (1,1)

  else:
    for i in (0,2):
      for j in (0,2):
        if l[i,j] == 2:
          return (i,j)

def findopenpositions(l):
	#Will find all the open positions on the board and will return the list of tuples
	return_list=[]
	for x in range(3):
		for y in range(3):
			if l[x,y] == 2:
				return_list.append((x,y))
	return return_list

def minimax(l, player):
	if xwins(l):
		return 10
	if owins(l):
		return -10
	if endmoves(l):
		return 0

	if (player == 'X'):
		bestmove = -9999
		for states in findopenpositions(l):
			l[states] = 3
			bestmove  = max(bestmove, minimax(l, 'O'))
			print bestmove
			l[states] = 2
		return bestmove

	if (player == 'O'):
		bestmove = 9999
		for states in findopenpositions(l):
			l[states] = 5
			bestmove  = min(bestmove, minimax(l, 'X'))
			l[states] = 2
		return bestmove 
init(l)
board(l)
move = 0
open_positions_list = findopenpositions(l)
moves_and_scores 	= dict()
for x in open_positions_list:
	l[x] = 3
	moves_and_scores[x] = minimax(l, 'O')
	l[x] = 2
print moves_and_scores
max(moves_and_scores)
moves_and_scores = sorted(moves_and_scores, key = moves_and_scores.__getitem__)
new_move = moves_and_scores[0]
l[new_move] = 3
print ""
print ""
board(l)