#AI technique for tic tac toe game
from Queue import *
import numpy as np 
l = np.array([3,3]) 
def init(l):
  for rows in range(3):
    for cols in range(3):
      l[rows,cols] = 2      #blank initialization of tic tac toe board

def board(l):
  for x in range(3):
    for y in range(3):
      print int(l[x,y]),
    print ""

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

def func1(player, l):
	#TODO complete the function (Recursive)	
	if player == 'X':
			l[x] = 3
			score_of_x = scorecalculate('X',l)
			func1('O',l)

	if player == 'O':
			list_of_open_positions_for_o = findopenpositions(l)
			for x in list_of_open_positions_for_o:
				l[x] = 5
				score_of_y.append(scorecalculate('O',l))   #TODO Dictionary
				





init(l)
board(l)

while(True):
	#TODO if x wins break
	#TODO if o wins break
	#TODO if no moves left break
	#TODO if even play user
	#else if odd play AI ->
	q = Queue(maxsize = 0)
	list_of_open_positions = findopenpositions(l)
	for x in list_of_open_positions:
		q.put_nowait(x)
	for x in q:
		scores_of_positions.append(minimax(x), 'X')