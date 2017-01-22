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

def scorecalculate(l):
	#TODO count winning positions

def minimax(l):
	#TODO if x wins return 10
	#TODO if o wins return -10
	#if end of moves return 0
	q = Queue(maxsize = 0)
	open_positions_list = findopenpositions(l)
	for x in l:
		q.put_nowait(x)
	
			
			l[x] = 3

			score_of_x = scorecalculate(l)
			func1(l)

	
init(l)
board(l)
move = 0
while(True):
	#TODO if x wins break AI
	#TODO if o wins break user
	#TODO end of moves then draw
	if move == 0:
		l[1,1] = 3
	if move % 2 == 0 and move != 0:
		next_position = minimax(l)
		l[next_position] = 3
	else:
		print "User, please enter the next move:"
		next_position = tuple(raw_input())
		l[next_position] = 5
	move = move + 1
