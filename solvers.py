"""
Python program to solve the N Queen Problem in different ways:

	Constraint Propagation and Backtracking
	Local optimization (hill climbing)
	Global optimization (simulated annealing)
	Global optimization (genetic)

This is the solver implementation file.
"""
import sys
import copy
import random

# Generate boards with random placed queens
def gen_problem(N):
	board = [[0 for x in range(N)] for y in range(N)]

	from random import randint

	for i in range(N):
		board[randint(0, N-1)][i] = 1	
	return board

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

def count_attacks(board, N):
	h = 0
	for i in range(N):
		for j in range(N):
			# For every Queen on the board
			if board[i][j] == 1: 
				# Sum conflicts 
				h += sum_conflicts(board, i, j, N)
	#print "There are "+str(h)+" of "+str(N)+" queens in conflict."
	return h 

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

def childs(board, N):
	# Swap two random elements
	def swap_random(seq):
		idx = range(len(seq))
		i1, i2 = random.sample(idx, 2)
		seq[i1], seq[i2] = seq[i2], seq[i1]
	
	# Generate index list and scramble
	rand_cols = range(N)
	rand_rows = range(N)
	for k in range(N):
		swap_random(rand_cols)
		swap_random(rand_rows)
	
	# Random pick a colum and move the queen N times randomly
	for j in rand_cols:
		for i in rand_rows:
			if board[i][j] == 1:
				board[i][j] = 0
				board[(i+1)%(N-1)][j] = 1			
			yield board

	raise StopIteration

# Print matrix on screen
def printSolution(board, N): 
	print
	for i in range(N): 
		for j in range(N): 
			print board[i][j], 
		print

# --- Solver Functions ---
def csp_back(N):
	board = [[0 for x in range(N)] for y in range(N)] 

	if solve_recursive(board, 0, N) == False: 
		print "Bad solution found!"

	return board

def first_choice_hill_climb(board, N, num_successors=10):
	if num_successors == 0:
		print "Limit Reached!"
		return board

	best_val = count_attacks(board, N)
	local_board = copy.deepcopy(board)
	best_board = board

	for tmp_board in childs(local_board, N):
		val = count_attacks(tmp_board, N)
		if val < best_val:
			print "Found better board: "+str(val)
			best_val = val
			best_board = copy.deepcopy(tmp_board)
			#printSolution(best_board, N)
			# Found a better one so go on
			return first_choice_hill_climb(best_board, N, num_successors-1)
	
	print "Best board found: "+str(best_val)
	return best_board

def steepest_ascent_hill_climb(board, N):
	best_val = count_attacks(board, N)
	local_board = copy.deepcopy(board)
	best_board = board

	for tmp_board in childs(local_board, N):
		val = count_attacks(tmp_board, N)
		if val <= best_val:
			best_val = val
			best_board = copy.deepcopy(tmp_board)
			#printSolution(best_board, N)
			
	if best_val < count_attacks(board, N):
		print "Best board so far: "+str(best_val)
		return steepest_ascent_hill_climb(best_board, N)
	
	print "Best board found: "+str(best_val)
	return best_board

def random_restart_hill_climb(board, N, num_restarts=10):
	best_board = board

	for restarts in range(num_restarts):
		tmp_board = steepest_ascent_hill_climb(gen_problem(N), N)
		if count_attacks(tmp_board, N) < count_attacks(best_board, N):
			best_board = tmp_board
			print "Best random board so far: "+str(count_attacks(best_board, N))
	
	print "Best board found: "+str(count_attacks(best_board, N))
	return best_board

def simulated_annealing(board, N):
	return board

def genetic_solver(board, N):
	return board