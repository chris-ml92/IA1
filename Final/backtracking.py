import sys
import copy
import random

# Generate a board with random placed queens
def gen_problem(N):
	board = [[0 for x in range(N)] for y in range(N)]

	from random import randint

	for i in range(N):
		board[randint(0, N-1)][i] = 1	
	return board

# Check if the left side of the current queen is safe
def partial_safe(board, row, col, N): 
	# Check row on left side 
	for i in range(col): 
		if board[row][i] == 1: 
			return False
	# Check upper diagonal on left side 
	for i, j in zip(range(row, -1, -1), range(col, -1, -1)): 
		if board[i][j] == 1: 
			return False
	# Check lower diagonal on left side 
	for i, j in zip(range(row, N, 1), range(col, -1, -1)): 
		if board[i][j] == 1: 
			return False

	return True

# Sum for a queen all the conflicts with other queens
def sum_conflicts(board, row, col, N):
	h = 0
	# Check row
	for i in range(N): 
		if board[row][i] == 1 and not i == col: 
			h += 1
	# Check upper diagonal on left side 
	for i, j in zip(range(row, -1, -1), range(col, -1, -1)): 
		if board[i][j] == 1 and not i == row and not j == col: 
			h += 1
	# Check upper diagonal on right side 
	for i, j in zip(range(row, -1, -1), range(col, N, 1)): 
		if board[i][j] == 1 and not i == row and not j == col: 
			h += 1
	# Check lower diagonal on left side 
	for i, j in zip(range(row, N, 1), range(col, -1, -1)): 
		if board[i][j] == 1 and not i == row and not j == col: 
			h += 1
	# Check lower diagonal on right side 
	for i, j in zip(range(row, N, 1), range(col, N, 1)): 
		if board[i][j] == 1 and not i == row and not j == col: 
			h += 1

	return h

# Count for every queen how many conflicts there are in the board
def count_attacks(board, N):
	h = 0
	for i in range(N):
		for j in range(N):
			if board[i][j] == 1: 
				h += sum_conflicts(board, i, j, N)
	return h 

# Backtracking Solver Recursive part
def solve_recursive(board, col, N): 
	if col >= N: 
		return True

	# Consider this column and try placing this queen in all rows one by one 
	for i in range(N): 
		if partial_safe(board, i, col, N): 
			board[i][col] = 1
			if solve_recursive(board, col + 1, N) == True: 
				return True
			board[i][col] = 0
	return False

# Print board on screen
def printSolution(board, N): 
	print
	for i in range(N): 
		for j in range(N): 
			print (str(board[i][j])+" ", end='')
		print (" ")

# Backtracking Solver
def csp_back(N):
	board = [[0 for x in range(N)] for y in range(N)] 

	if solve_recursive(board, 0, N) == False: 
		print ("Bad solution found!")

	return board
