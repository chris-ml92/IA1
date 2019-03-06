from random import choice, random
from math import exp
from heapq import heappop, heappush

def partial_attack(board, row, col, N): 
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

def full_attack(board, row, col, N):
    # Check row
	for i in range(N): 
		if board[row][i] == 1: 
			return False
    # Check col
	for i in range(N): 
		if board[i][col] == 1: 
			return False
	# check diagonals
	
	return True

def solve_recursive(board, col, N): 
	if col >= N: 
		return True

	# Consider this column and try placing this queen in all rows one by one 
	for i in range(N): 

		if partial_attack(board, i, col, N): 
			board[i][col] = 1

			if solve_recursive(board, col + 1, N) == True: 
				return True
 
			board[i][col] = 0

	return False

def csp_back(N):
    board = [[0 for x in range(N)] for y in range(N)] 

    if solve_recursive(board, 0, N) == False: 
		return {'outcome': 'failure', 'solution': None}

    return board

def steepest_ascent_hill_climb(problem):
    pass

def first_choice_hill_climb(problem, num_successors=100):
    pass

def random_restart_hill_climb(problem, num_restarts=100):
    pass

def simulated_annealing(problem):
    pass

def genetic_solver(problem):
    pass