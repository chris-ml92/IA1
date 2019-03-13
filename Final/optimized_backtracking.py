import random

# Local support class for operations
class chessBoard:
    def __init__(self, N):
		#diagonal from left top to bottom right
        self.diagonals = {}
		#diagonal from bottom left to top right
        self.anti_diagonals = {}
		#rows
        self.rows = {}
		#cols
        self.columns = {}
		#chessboard dimension
        self.N = N
		#create board
        self.board = [[0 for x in range(N)] for y in range(N)]
		
		
def check_position(chessBoard, row, col):
	#check row
	if row in chessBoard.rows:
		return False
	#check col
	if col in chessBoard.columns:
		return False
	#optimization: in a diagonal top to bottom the individuals have the same value row - col
	if row - col in chessBoard.diagonals:
		return False
	#optimization: in a diagonal bottom to top the individuals have the same value row + col	
	if row + col  in chessBoard.anti_diagonals:
		return False
	#return true if element in [row][col] wasn't present
	return True

def set_in_queen(chessBoard, row, col):
    chessBoard.rows[row] = True
    chessBoard.columns[col] = True
    chessBoard.diagonals[row - col] = True
    chessBoard.anti_diagonals[row + col] = True
    chessBoard.board[row][col] = 1

def take_off_queen(chessBoard, row, col):
    del chessBoard.rows[row]
    del chessBoard.columns[col] 
    del chessBoard.diagonals[row - col]
    del chessBoard.anti_diagonals[row + col]
    chessBoard.board[row][col] = 0

#backtracking algorithm
def solve(chessBoard, col):
    if col == chessBoard.N:
       return True
    for i in range(0,chessBoard.N):
        if check_position(chessBoard,i, col):
           set_in_queen(chessBoard,i, col)
           if solve(chessBoard , col + 1) == True:
              return True
           take_off_queen(chessBoard,i, col)
    return False

# Print board on screen
def printSolution(Q, N): 
	print
	for i in range(N): 
		for j in range(N): 
			print (str(Q.board[i][j])+" ", end='')
		print (" ")
	print (" ")

# Main algorithm
def optimized_csp_back(N):
	sol = chessBoard(N)
	solve(sol,0)
	#to generate possible alternative solutions, change the first queen position
	#col = random.randint(0,N-1)
	#set_in_queen(sol,col,0)
	#solve(sol,1)
	printSolution(sol, N)
