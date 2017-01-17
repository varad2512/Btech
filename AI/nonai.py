#Non AI technique for tic-tac-toe
import numpy as np
l = np.zeros([3,3])

def init(l):
  for rows in range(3):
    for cols in range(3):
      l[rows,cols] = 2         #blank initialization of tic tac toe board

def board(l):
  for x in range(3):
    for y in range(3):
      print int(l[x,y]),
    print ""


def Poswin(player,l):
	print "In Poswin function"
  if player == 'x':
    sum_of_col = list(np.sum(l,axis = 0))
    sum_of_row = list(np.sum(l,axis = 1))
    if 18 in sum_of_col:
      index = sum_of_col.index(18)
      row = np.argmin(l[:,index])
      pos = (row,index)     #TODO return statement
    elif 18 in sum_of_row:
      index = sum_of_row.index(18)
      col = np.argmin(l[index,:])
      pos = (index,col)     #TODO return statement and diagonal check
  #TODO for player x to block

  #TODO everything for player o
  
    

def optimalmove():
  if l[1][1] == 2:
    return (1,1)

  else:
    for i in (0,2):
      for j in (0,2):
        if l[i,j] == 2:
          return (i,j)


init(l)
number_of_moves = 0  
print "Initial State :"
board(l)
'''
while(number_of_moves < 9):
  
  print "move number :", number_of_moves
  
  if number_of_moves == 0:
    l[1][1] = 3
  
  else:
    
    if number_of_moves % 2 == 0:
      block,result,position = poswin('x')
      flag = 0
    
    else:
      block,result,position = poswin('o')
      flag = 1
    
    if result == 0  and block == 0:
      
      row,col = optimalmove()
      
      if flag == 0:
        l[row][col] = 3

      if flag == 1:
        l[row][col] = 5

    if result == 1:
      
      if flag == 0:
        l[pos] = 3
        print "Player wins"
        break

      if flag == 1:
        l[pos] = 5
        print "AI wins"
        break
  number_of_moves++
'''