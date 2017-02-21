#AI technique for tic tac toe game

import numpy as np 

l = np.ones([3,3],dtype = 'uint8') 

def init(l):
  '''
  for rows in range(3):
    for cols in range(3):
      l[rows,cols] = 2      #blank initialization of tic tac toe board
  '''

  l[0,0] = 2
  l[0,1] = 2
  l[0,2] = 2
  l[1,0] = 2
  l[1,1] = 2
  l[1,2] = 2
  l[2,0] = 2
  l[2,1] = 2
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
	if 27 in sum_of_col:
	  	return 1    
	elif 27 in sum_of_row:
		return 1    
	elif np.prod(sum_of_diag1) == 27:
		return 1
	elif np.prod(sum_of_diag2) == 27:
		return 1
	else:
		return 0

def owins(l):
	sum_of_col   = list(np.product(l,axis = 0))
	sum_of_row   = list(np.product(l,axis = 1))
	sum_of_diag1 = list(np.diagonal(l))
	sum_of_diag2 = list(np.diagonal(np.fliplr(l)))
	if 125 in sum_of_col:
	  	return 1    
	elif 125 in sum_of_row:
		return 1    
	elif np.prod(sum_of_diag1) == 125:
		return 1
	elif np.prod(sum_of_diag2) == 125:
		return 1
	else:
		return 0

def endmoves(l):
	flag = 0
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
	if (xwins(l)) == 1:
		
		return 10
	if (owins(l)) == 1:
		return -10
	if endmoves(l) == 1:
		return 0

	if (player == 'X'):
		bestmove = -9999
		for states in findopenpositions(l):
			l[states] = 3
			bestmove  = max(bestmove, minimax(l, 'O'))
			l[states] = 2
		return bestmove

	if (player == 'O'):
		bestmove = 9999
		for states in findopenpositions(l):
			l[states] = 5
			bestmove  = ssssmin(bestmove, minimax(l, 'X'))
			l[states] = 2
		return bestmove 
init(l)
board(l)
move  = 0
while(True):
	
	if move > 8:
		print "draw"
		break

	elif (xwins(l)):
		print "x wins"
		break

	elif (owins(l)):
		print "o wins"
		break

	else :
		if move % 2 == 0:
			open_positions_list = findopenpositions(l)
			moves_and_scores 	= dict()
			for x in open_positions_list:
				
				l[x] = 3
				moves_and_scores[x] = minimax(l, 'O')
				l[x] = 2
			print moves_and_scores
			moves_and_scores_1 = sorted(moves_and_scores, key = moves_and_scores.__getitem__, reverse = True)
			print moves_and_scores_1
			new_move = moves_and_scores_1[0]
			l[new_move] = 3

		else:
			print "Please enter move:"
			row = input()
			col = input()
			l[row][col] = 5

		print ""
		print ""
		board(l)
		move = move + 1