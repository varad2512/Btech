#Non AI technique for tic-tac-toe
import numpy as np
l = np.zeros([3,3])
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
  if l[1][1] == 2:
    return (1,1)

  else:
    for i in (0,2):
      for j in (0,2):
        if l[i,j] == 2:
          return (i,j)
def Poswin(l):
	print "In Poswin function"
	sum_of_col = list(np.product(l,axis = 0))
	sum_of_row = list(np.product(l,axis = 1))
	sum_of_diag1 = list(np.diagonal(l))
	sum_of_diag2 = list(np.diagonal(np.fliplr(l)))
	if 50 in sum_of_col:
  		index = sum_of_col.index(50)
  		row = np.argmin(l[:,index])
  		pos = (row,index)   
  		return 0,1,pos
	elif 50 in sum_of_row:
	  	index = sum_of_row.index(50)
	  	col = np.argmin(l[index,:])
	  	pos = (index,col) 
	  	return 0,1,pos
	elif np.prod(sum_of_diag1) == 50:
		pos = (sum_of_diag1.index(2),sum_of_diag1.index(2))
		return 0,1,pos
	elif np.prod(sum_of_diag2) == 50:
		pos = (sum_of_diag2.index(2),sum_of_diag2.index(2))	
		return 0,1,pos
	sum_of_col = list(np.product(l,axis = 0))
	sum_of_row = list(np.product(l,axis = 1))
	sum_of_diag1 = list(np.diagonal(l))
	sum_of_diag2 = list(np.diagonal(np.fliplr(l)))
	if 18 in sum_of_col:
	  	index = sum_of_col.index(18)
	  	row = np.argmin(l[:,index])
	  	pos = (row,index)
	  	return 1,0,pos     #TODO return statement
	elif 18 in sum_of_row:
		index = sum_of_row.index(18)
	  	col = np.argmin(l[index,:])
	  	pos = (index,col) 
	  	return 1,0,pos    #TODO return statement and diagonal check
	elif np.prod(sum_of_diag1) == 18:
		print "yes1"
		pos = (sum_of_diag1.index(2),sum_of_diag1.index(2))
		return 1,0,pos
	elif np.prod(sum_of_diag2) == 18:
		print "yes2"
		pos = (sum_of_diag2.index(2),sum_of_diag2.index(2))
		if sum_of_diag2[0]==2:
			pos=(0,2)
		elif sum_of_diag2[1]==2:
			pos=(1,1)
		else:
			pos=(2,0)
		return 1,0,pos
	else:
		return 0,0,(0,0)
init(l)
number_of_moves = 0  
print "Initial State :"
board(l)
while(number_of_moves < 9):
	print "Move Number :",number_of_moves
	if number_of_moves%2==0:
		print "User, please make a move:"
		user_move=tuple(int(x) for x in (raw_input().split(',')))
		l[user_move]=3
		board(l)
	else:
		block,result,position=Poswin(l)
		if result==0  and block==0:
			row,col=optimalmove(l)
			l[row][col]=5
			board(l)
		elif result==1:
			l[position]=5
			print "AI wins"
			board(l)
			break
		elif result==0 and block==1:
			l[position]=5
			board(l)
	number_of_moves+=1

'''
while(number_of_moves < 9):
  	print "move number :", number_of_moves
	if number_of_moves % 2 == 0:
			print "Player, please play your move :"
			user_move = tuple(int(x) for x in raw_input())  
			l[user_move] = 3
			board(l)
  
  	else:  		
		block,result,position = poswin(l)
    	if result == 0  and block == 0:
			  	row,col = optimalmove(l)
			  	l[row][col] = 5
			  	board(l)
			
		elif result == 0:
				l[pos] = 5
		  		print "AI wins"
		  		board(l)
		  		break
		
		elif result == 0 and block == 1:
				l[pos] = 5
				board(l)

  	number_of_moves++
'''