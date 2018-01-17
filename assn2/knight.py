# knight.py 
# Jefferson Zhumi 
# 11/12 
# 
# Note: This script tries to solve the Knight's tour board by luck. 
# functions:
# createdBoard() -> creates board and fills it with 'xs'
# avaliableMoves() -> checks for all avaliable moves that knight can make and
#			returns it as a list					
# validMoves() -> checks for valid moves and visited moves and returns it as
#			a list
# printBoard() -> prints board  
import random
import string
import sys

def createBoard(x, y):
	#create board and fill with xs  
	board = [['x' for j in range(y)] for i in range(x)]
	
	return board

def avaliableMoves(x, y):
	#knights move (8)
	list = []
	list.append([x-2,y+1])
	list.append([x-1,y+2])
	list.append([x+1,y+2])
	list.append([x+2,y+1])
	list.append([x-2,y-1])
	list.append([x-1,y-2])
  	list.append([x+1,y-2])
  	list.append([x+2,y-1])
 	#return list of avaliable moves
  	return list
  
def validMoves(board, list, x, y):
    
  	newList = []
  
  	for pt in list:
    		cx = pt[0]
    		cy = pt[1]
   		#checks for out of bounds 
    		if cx >= 0 and cx < x and cy >= 0 and cy < y:
      		#keeps track of visited moves    
      			if board[cx][cy] == 'x':
        			newList.append([cx, cy])
        
 	 #return list of valid moves      
  	return newList


def printBoard(board, x, y):
  
  	for cy in range(y):
    		for cx in range(x):
        		print string.rjust(str(board[cx][cy]), 2),
    		print
        
#main function
def main():
	#command line arguments
	rowarg = int(sys.argv[1])
  	colarg = int(sys.argv[2])
  	attemptarg = int(sys.argv[3])
 
  	attempts = attemptarg 
  	
	#loop for attemps 
  	while (attempts != 0):
      
      
      		row = rowarg
      		col = colarg
                
		#start board with (0, 0) coordinates 
     		cx = 0
     		cy = 0
      		
		#count	
     	 	count = 1
     		
		#create board
      		board = createBoard(row,col)

      		# (0, 0) coordinates to 1 
      		board[cx][cy] = count
      		
		# loop to walk the knight
		# checks for avaliable moves and valid moves 
		# print if sucess knight tour	
      		for k in range(row * col):
        		
			#coordinate to keep track of location of point and to update 
        		coordinate = [cx, cy]
        
        		avalMoves = avaliableMoves(cx, cy)
    
        		valMoves = validMoves(board, avalMoves, row, col)
        
        		if valMoves:
            
            			rand = random.randint(0, len(valMoves)-1)
				#update coordinate 
            			coordinate  = valMoves[rand]
            			count += 1
        
        		cx = coordinate[0]
        		cy = coordinate[1]
    			
			#walk knight
        		board[cx][cy] = count

			#if knight tour solved print sucess board
        		if not any('x' in bcor for bcor in board):
				print "success:"
				printBoard(board, row, col)
				return	
				      
      		#decrement attemps
     		attempts -= 1

	#return last attemp
	if any('x' in bcor for bcor in board):
		print "fail:"
		printBoard(board, row, col)
      			
main()

