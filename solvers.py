"""
Python program to solve the N Queen Problem in different ways:

    Constraint Propagation and Backtracking
    Local optimization (hill climbing)
    Global optimization (simulated annealing)
    Global optimization (genetic)

This is the solver implementation file.
"""
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
	# Check upper diagonal on left side 
	for i, j in zip(range(row, -1, -1), range(col, -1, -1)): 
		if board[i][j] == 1: 
			return False
	# Check upper diagonal on right side 
	for i, j in zip(range(row, -1, -1), range(col, N, 1)): 
		if board[i][j] == 1: 
			return False
	# Check lower diagonal on left side 
	for i, j in zip(range(row, N, 1), range(col, -1, -1)): 
		if board[i][j] == 1: 
			return False
	# Check lower diagonal on right side 
	for i, j in zip(range(row, N, 1), range(col, N, 1)): 
		if board[i][j] == 1: 
			return False

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


# Solver Functions
def csp_back(N):
    board = [[0 for x in range(N)] for y in range(N)] 

    if solve_recursive(board, 0, N) == False: 
		return {'outcome': 'failure', 'solution': None}

    return board

def steepest_ascent_hill_climb(board):
    return board

def first_choice_hill_climb(board, num_successors=100):
	return board

def random_restart_hill_climb(board, num_restarts=100):
    return board

def simulated_annealing(board):
    return board

def genetic_solver(board):
    return board